"""Two way name/id lookups for common query constraints.

The "attribute tables" in the database are those which data rows reference
as part of their composite key (i.e. distinguishing by country). To
speed up queries, this lookup service reduces the number of joins required
for queries by keeping these attribute tables in memory."""

from __future__ import annotations

import typing
from collections.abc import Callable
from datetime import datetime, timedelta
from typing import overload

from devscripts.generate_models import column_field_name
from django.apps import apps
from django.db.models import Model, QuerySet
from Mexer import models
from Mexer.apps import MexerConfig

from utils.logging import LOGGER

if typing.TYPE_CHECKING:
    from utils.data import DatabaseSource

# App config used to get models dynamically.
app_name = MexerConfig.name
mexer_config = apps.get_app_config(app_name)

# How long to cache information from the database.
LOOKUP_CACHE_TTL = timedelta(hours=24.0)

FULLNAME_FIELD_NAME = "full_name"


class Attribute[T: Model]:
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

    model: type[T]
    name: str
    description: str
    foreign_fields: list[str]
    id_field: str
    name_field: str

    def __init__(
        self,
        *,
        model: type[T],
        name_field: str,
        foreign_fields: list[str] | None = None,
        description="",
    ):
        self.model = model
        assert model._meta.object_name is not None
        self.name = model._meta.object_name
        self.description = description
        self.id_field = model._meta.pk.name
        self.name_field = name_field

        def model_has_field(model: type[Model], field_name: str):
            return any(field.name == field_name for field in model._meta.fields)

        if not model_has_field(model, self.name_field):
            raise ValueError(f"name field '{self.name_field}' not found on model")

        column_name = column_field_name(self.name)
        self.foreign_fields = [column_name]
        if foreign_fields is not None:
            # Sanity check: are each of these foreign fields present
            # on at least one model (other than this one)?
            foreign_models = [
                foreign_model
                for foreign_model in mexer_config.get_models()
                if foreign_model is not model
            ]
            for foreign_field in foreign_fields:
                field_exists = any(
                    model_has_field(fm, foreign_field) for fm in foreign_models
                )
                if not field_exists:
                    raise ValueError(
                        f"foreign field '{foreign_field}' not found on other models"
                    )
            self.foreign_fields.extend(foreign_fields)


# Models eligible for LOOKUP are those used to narrow
# DB queries, called "attributes", i.e. they are the targets
# of the many foreign-key columns present in data-source tables.
#
# TODO: These are hardcoded for now, but should be taken from table of attributes.
#
# TODO: foreign_fields can be derived from schema spreadsheet.
ATTRIBUTES: dict[type[Model], Attribute] = {
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
    models.ECCStage: Attribute(
        model=models.ECCStage, name_field="ecc_stage", foreign_fields=["last_stage"]
    ),
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


def get_attribute[T: Model](model: type[T]) -> Attribute[T]:
    return ATTRIBUTES[model]


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


class AttributeLookup[T: Model]:
    """A two-way lookup between names and IDs of one attribute table.

    Attributes:
    - attribute: The model type the lookup is for.
    - created_at: When the lookup was constructed from the DB.
    - pairs: Bidirectional mapping from names to IDs.
    """

    attribute: Attribute[T]
    created_at: datetime
    objects: set[T]
    by_name: dict[str, T]
    by_id: dict[int, T]

    def __init__(
        self,
        attribute: Attribute,
        objects: QuerySet[T],
        created_at: datetime | None = None,
    ):
        self.attribute = attribute

        self.objects = set(objects)
        self.by_name = {}
        self.by_id = {}
        for obj in self.objects:
            name: str = getattr(obj, attribute.name_field)
            id: int = getattr(obj, attribute.id_field)
            self.by_name[name] = obj
            self.by_id[id] = obj

        self.created_at = created_at or datetime.now()

    def get_object(self, value: str | int) -> T | None:
        if isinstance(value, str):
            return self.by_name.get(value)
        else:
            return self.by_id.get(value)

    @overload
    def translate(self, value: str) -> int | None: ...
    @overload
    def translate(self, value: int) -> str | None: ...
    def translate(self, value: str | int) -> str | int | None:
        obj = self.get_object(value)
        if obj is None:
            return None
        if isinstance(value, str):
            # Name provided; return ID.
            return getattr(obj, self.attribute.id_field)
        else:
            # ID provided; return name.
            return getattr(obj, self.attribute.name_field)

    def __getitem__(self, value: str | int) -> T:
        if isinstance(value, str):
            return self.by_name[value]
        else:
            return self.by_id[value]

    @property
    def translator(self):
        return _Translator(self)

    @property
    def age(self) -> timedelta:
        return datetime.now() - self.created_at

    def expired(self, ttl=LOOKUP_CACHE_TTL) -> bool:
        return self.age > ttl


class _Translator[T: Model]:
    lookup: AttributeLookup[T]

    def __init__(self, lookup: AttributeLookup[T]):
        self.lookup = lookup

    @overload
    def get(self, value: str) -> int | None: ...
    @overload
    def get(self, value: int) -> str | None: ...
    def get(self, value: str | int) -> str | int | None:
        return self.lookup.translate(value)

    @overload
    def __getitem__(self, value: str) -> int: ...
    @overload
    def __getitem__(self, value: int) -> str: ...
    def __getitem__(self, value: str | int) -> str | int:
        translated = self.get(value)
        if translated is None:
            raise KeyError(f"invalid lookup key {value}")
        return translated


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
    def _get_lookup[T: Model](
        database: DatabaseSource,
        attribute: Attribute[T],
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup[T]:
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
    def _generate_lookup[T: Model](
        database: DatabaseSource,
        attribute: Attribute[T],
        *,
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup[T]:
        lookup_key = _get_lookup_key(
            database, attribute, key_name_override=key_name_override
        )
        LOGGER.info(f"Loading and caching {lookup_key}")

        objects = (
            query_override(attribute.model)
            if query_override
            else attribute.model.objects.using(database).all()
        )
        lookup = AttributeLookup(attribute, objects)

        # Create a bidict with name:id pairs
        LookupManager._lookups[lookup_key] = lookup
        return lookup

    def get_objects[T: Model](self, *, model: type[T]) -> list[T]:
        attribute = get_attribute(model)
        if attribute is None:
            return []

        lookup = self._get_lookup(self.db, attribute)
        return list(lookup.objects)

    def lookup[T: Model](self, *, model: type[T], value: str | int) -> T | None:
        attribute = get_attribute(model)
        if attribute is None:
            raise ValueError(f"Model kind {model} ineligible for lookup")

        lookup = self._get_lookup(self.db, attribute)
        return lookup.get_object(value)

    @overload
    def translate(
        self, *, model_or_field: type[Model] | str, value: str
    ) -> int | None: ...
    @overload
    def translate(
        self, *, model_or_field: type[Model] | str, value: int
    ) -> str | None: ...
    def translate(
        self, *, model_or_field: type[Model] | str, value: str | int
    ) -> str | int | None:
        if isinstance(model_or_field, str):
            attribute = get_foreign_attribute(model_or_field)
        else:
            attribute = get_attribute(model_or_field)
        if attribute is None:
            raise ValueError(f"Model kind {model_or_field} ineligible for lookup")

        lookup = self._get_lookup(self.db, attribute)
        return lookup.translate(value)

    def attribute[T: Model](
        self, model_or_field: type[T] | str
    ) -> AttributeLookup[T] | None:
        """Get or generate a lookup for a specific attribute."""
        if isinstance(model_or_field, str):
            attribute = get_foreign_attribute(model_or_field)
        else:
            attribute = get_attribute(model_or_field)
        if attribute is None:
            return None

        lookup = LookupManager._get_lookup(self.db, attribute)
        return lookup

    def __getitem__[T: Model](self, model: type[T] | str) -> AttributeLookup[T]:
        attribute = self.attribute(model)
        if attribute is None:
            raise KeyError(f"model {model} is ineligible for attribute lookup")
        return attribute

    def public_datasets(self) -> AttributeLookup[models.Dataset]:
        key_name_override = "public_datasets"

        def query_override(model: type[Model]):
            return model.objects.filter(Public=True).all()

        return self._get_lookup(
            self.db, get_attribute(models.Dataset), key_name_override, query_override
        )

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
