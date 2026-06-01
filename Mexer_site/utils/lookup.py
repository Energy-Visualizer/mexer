"""Two way name/id lookups for common query constraints.

The "attribute tables" in the database are those which data rows reference
as part of their composite key (i.e. distinguishing by country). To
speed up queries, this lookup service reduces the number of joins required
for queries by keeping these attribute tables in memory."""

from collections.abc import Callable
from datetime import datetime, timedelta
from typing import overload

from bidict import bidict
from devscripts.generate_models import column_field_name
from django.apps import apps
from django.conf import settings
from django.db.models import Model, QuerySet
from Mexer import models
from Mexer.apps import MexerConfig

from utils.data import DatabaseSource
from utils.logging import LOGGER

# App config used to get models dynamically.
app_name = MexerConfig.name
mexer_config = apps.get_app_config(app_name)

# How long to cache information from the database.
LOOKUP_CACHE_TTL = timedelta(hours=24.0)

FULLNAME_FIELD_NAME = "full_name"


class Attribute:
    """Metadata about a database table that is used as
    an attribute to narrow queries.

    - name: The name of the database model.
    - model: The database model type.
    - foreign_fields: The names of fields on other models that
        reference this table.
    - description: A free text description of the role of the
        attribute in a query.
    - name_field: The name of the field on this model that holds
        the display name of the row, which is shown to the user.
    """

    name: str
    model: type[Model]
    foreign_fields: list[str]
    description: str
    name_field: str

    def __init__(
        self,
        *,
        model: type[Model],
        name_field: str,
        foreign_fields: list[str] | None = None,
        description="",
    ):
        assert model._meta.object_name is not None
        self.name = model._meta.object_name
        self.description = description
        self.name_field = name_field

        def model_has_field(model: type[Model], field_name: str):
            return any(field.name == field_name for field in model._meta.fields)

        if not model_has_field(model, self.name_field):
            raise ValueError(f"name field '{self.name_field}' not found on model")

        if foreign_fields is not None:
            self.foreign_fields = foreign_fields
        else:
            # Since this is unspecified, the other models likely have
            # a field with the same name as this model.
            column_name = column_field_name(self.name)
            self.foreign_fields = [column_name]

        # Sanity check: are each of these foreign fields present
        # on at least one model (other than this one)?
        foreign_models = [
            foreign_model
            for foreign_model in mexer_config.get_models()
            if foreign_model is not model
        ]
        for foreign_field in self.foreign_fields:
            field_exists = any(
                model_has_field(fm, foreign_field) for fm in foreign_models
            )
            if not field_exists:
                raise ValueError(
                    f"foreign field '{foreign_field}' not found on other models"
                )


# Models eligible for LOOKUP are those used to narrow
# DB queries, called "attributes", i.e. they are the targets
# of the many foreign-key columns present in data-source tables.
#
# These are hardcoded for now, but should be taken from table of tables.
ATTRIBUTES = {
    models.Index: Attribute(
        model=models.Index, name_field="index", foreign_fields=["i", "j", "chopped_var"]
    ),
    models.Dataset: Attribute(model=models.Dataset, name_field="dataset"),
    models.Version: Attribute(
        model=models.Version,
        name_field="version",
        foreign_fields=["valid_from_version", "valid_to_version"],
    ),
    models.Country: Attribute(model=models.Country, name_field=FULLNAME_FIELD_NAME),
    models.Method: Attribute(model=models.Method, name_field="method"),
    models.EnergyType: Attribute(
        model=models.EnergyType, name_field=FULLNAME_FIELD_NAME
    ),
    models.ECCStage: Attribute(model=models.ECCStage, name_field="ecc_stage"),
    models.Matname: Attribute(
        model=models.Matname, name_field="matname", foreign_fields=["chopped_mat"]
    ),
    models.GrossNet: Attribute(model=models.GrossNet, name_field="gross_net"),
    models.AggLevel: Attribute(
        model=models.AggLevel,
        name_field="agg_level",
        foreign_fields=["product_aggregation", "industry_aggregation"],
    ),
}


def get_foreign_attribute(field_name: str) -> Attribute | None:
    """Whether this DB column name is eligible for attribute lookup."""
    for attr in ATTRIBUTES.values():
        if field_name in attr.foreign_fields:
            return attr
    return None


type _QueryOverride = Callable[[type[Model]], QuerySet]


def _get_lookup_key(
    database: DatabaseSource, attribute: Attribute, *, key_name_override: str | None
) -> str:
    model_name = key_name_override if key_name_override else attribute.name
    return f"{database}:{model_name}"


class AttributeLookup:
    """A two-way lookup between names and IDs of one attribute table.

    Attributes:
    - attribute: The model type the lookup is for.
    - created_at: When the lookup was constructed from the DB.
    - pairs: Bidirectional mapping from names to IDs.
    """

    attribute: Attribute
    created_at: datetime
    pairs: bidict[str, int]

    def __init__(
        self,
        attribute: Attribute,
        pairs: bidict[str, int],
        created_at: datetime | None = None,
    ):
        self.attribute = attribute
        self.pairs = pairs
        self.created_at = created_at or datetime.now()

    @overload
    def __getitem__(self, value: str) -> int: ...
    @overload
    def __getitem__(self, value: int) -> str: ...
    def __getitem__(self, value: str | int) -> str | int:
        if isinstance(value, str):
            return self.pairs[value]
        else:
            return self.pairs.inv[value]

    @property
    def age(self) -> timedelta:
        return datetime.now() - self.created_at

    @property
    def names(self) -> list[str]:
        return list(self.pairs.keys())

    def expired(self, ttl=LOOKUP_CACHE_TTL) -> bool:
        return self.age > ttl


class LookupManager:
    """A two-way lookup between names and IDs of entries in attribute tables.

    This class lazily creates lookups for requested models.

    Attributes are used to narrow queries to data tables (for example, by country).
    Queries are made with IDs (like 27) but user requests use names (like USA)."""

    # Generated attribute lookups, indexed by a lookup key formed
    # from the source database name (e.g. "default" or "sandbox")
    # and the name of the model.
    _lookups: dict[str, AttributeLookup] = {}

    # Special lookup for public datasets.
    _public_datasets: AttributeLookup | None = None

    db: DatabaseSource

    def __init__(self, database: DatabaseSource = "default"):
        self.db = database

    @staticmethod
    def _get_lookup(
        database: DatabaseSource,
        attribute: Attribute,
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup:
        def new_lookup():
            return LookupManager._generate_lookup(
                database,
                attribute,
                key_name_override=key_name_override,
                query_override=query_override,
            )

        lookup_key = _get_lookup_key(
            database, attribute, key_name_override=key_name_override
        )
        if lookup_key not in LookupManager._lookups:
            # Reload, lookup key not present.
            lookup = new_lookup()
        else:
            # Load cached lookup.
            lookup = LookupManager._lookups[lookup_key]
            if lookup.expired():
                # Refresh.
                lookup = new_lookup()
        return lookup

    @staticmethod
    def _generate_lookup(
        database: DatabaseSource,
        attribute: Attribute,
        *,
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup:
        lookup_key = _get_lookup_key(
            database, attribute, key_name_override=key_name_override
        )
        LOGGER.info(f"Loading and caching {lookup_key}")

        name_field = attribute.name_field

        # Create a mapping between the value of the model's
        # name field and the value of the model's ID field.
        query_set = (
            query_override(attribute.model)
            if query_override
            else attribute.model.objects.using(database).values_list(name_field, "pk")
        )
        name_id_mapping = bidict(query_set)
        lookup = AttributeLookup(attribute, name_id_mapping)

        # Create a bidict with name:id pairs
        LookupManager._lookups[lookup_key] = lookup
        return lookup

    @overload
    def lookup(self, *, model: type[Model] | str, value: int) -> str: ...
    @overload
    def lookup(self, *, model: type[Model] | str, value: str) -> int: ...
    def lookup(self, *, model: type[Model] | str, value: str | int) -> str | int:
        if isinstance(model, str):
            attribute = get_foreign_attribute(model)
        else:
            attribute = ATTRIBUTES.get(model)
        if attribute is None:
            raise ValueError(f"Model kind {model} ineligible for lookup")

        lookup = self._get_lookup(self.db, attribute)
        try:
            return lookup[value]
        except KeyError:
            raise KeyError(f"Unrecognized lookup key '{value}' for {attribute.name}")

    def attribute(self, model: type[Model] | str) -> AttributeLookup:
        """Get or generate a lookup for a specific attribute."""
        if isinstance(model, str):
            attribute = get_foreign_attribute(model)
        else:
            attribute = ATTRIBUTES.get(model)
        if attribute is None:
            raise ValueError(f"Model kind {model} ineligible for lookup")

        lookup = LookupManager._get_lookup(self.db, attribute)
        return lookup

    def __getitem__(self, attribute: type[Model] | str) -> AttributeLookup:
        return self.attribute(attribute)

    @property
    def public_datasets(self):
        key_name_override = "public_datasets"

        def query_override(model: type[Model]):
            return model.objects.filter(Public=True).values_list("Dataset", "pk")

        return self._get_lookup(
            self.db, ATTRIBUTES[models.Dataset], key_name_override, query_override
        )

    @staticmethod
    def admin_dataset_names():
        mexer = LookupManager("default")
        sandbox = LookupManager("sandbox")

        mexer_datasets = mexer[models.Dataset]
        sandbox_datasets = sandbox[models.Dataset]

        # Combine them and add the sandbox prefix
        # onto the sandbox datasets to differentiate.
        return mexer_datasets.names + [
            settings.SANDBOX_PREFIX + dataset for dataset in sandbox_datasets.names
        ]

    # TODO: This needs to be finished...
    @staticmethod
    def get_all_available(model: type[Model] | str):
        """Get all available values for a given attribute from the PSUT model."""

        if isinstance(model, str):
            attribute = get_foreign_attribute(model)
        else:
            attribute = ATTRIBUTES.get(model)
        if attribute is None:
            raise ValueError(f"Model kind {model} ineligible for lookup")

        _lookup = LookupManager._get_lookup(
            "default", attribute
        )  # TODO... which database?

        # Print distinct values for the attribute from the PSUT model
        # print(PSUT.objects.order_by().values_list(model_name, flat=True).distinct())
