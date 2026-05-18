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
from Mexer.apps import MexerConfig
from Mexer.models import Dataset

from utils.data import DatabaseSource
from utils.logging import LOGGER

# App config used to get models dynamically.
app_name = MexerConfig.name
mexer_config = apps.get_app_config(app_name)

# How long to cache information from the database.
LOOKUP_CACHE_TTL = timedelta(hours=24.0)

# Some models have a full_name field which represents the name half
# of the lookup.
#
# If this field is not present on the model, the model name itself
# should be the name of the name field.
FULLNAME_FIELD_NAME = "full_name"


# Determines if a table is a candidate for lookup.
# Returns the table's name field.
def _is_attribute(model: type[Model]) -> str | None:
    has_single_id = len(model._meta.pk_fields) == 1
    if not has_single_id:
        return None

    model_fields = model._meta.fields
    model_name = model._meta.object_name
    if not model_name:
        return None
    model_name_column = column_field_name(model_name)

    name_field_candidates = (FULLNAME_FIELD_NAME, model_name_column)
    for candidate in name_field_candidates:
        if any(field.name == candidate for field in model_fields):
            return candidate
    return None


# Models eligible for LOOKUP are those used to narrow
# DB queries, called "attributes", i.e. they are the targets
# of the many foreign-key columns present in data-source tables.
#
# Derived programatically: all tables that have a full-name
# column or a name column with the same name as themselves,
# and have a single integer primary key column.
ATTRIBUTES = {
    model: name for model in mexer_config.get_models() if (name := _is_attribute(model))
}


type _QueryOverride = Callable[[type[Model]], QuerySet]


def _get_lookup_key(
    database: DatabaseSource, model: type[Model], key_name_override: str | None
) -> str:
    model_name = key_name_override if key_name_override else model._meta.object_name
    return f"{database}:{model_name}"


class AttributeLookup:
    """A two-way lookup between names and IDs of one attribute table.

    Attributes:
    - attribute: The model type the lookup is for.
    - created_at: When the lookup was constructed from the DB.
    - pairs: Bidirectional mapping from names to IDs.
    """

    attribute: type[Model]
    created_at: datetime
    pairs: bidict[str, int]

    def __init__(
        self,
        attribute: type[Model],
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
        model: type[Model],
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup:
        def new_lookup():
            return LookupManager._generate_lookup(
                database, model, key_name_override, query_override
            )

        lookup_key = _get_lookup_key(database, model, key_name_override)
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
        model: type[Model],
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> AttributeLookup:
        if model not in ATTRIBUTES:
            raise ValueError(f"Model kind {model} ineligible for lookup")

        lookup_key = _get_lookup_key(database, model, key_name_override)
        LOGGER.info(f"Loading and caching {lookup_key}")

        name_field = ATTRIBUTES[model]

        # Create a mapping between the value of the model's
        # name field and the value of the model's ID field.
        query_set = (
            query_override(model)
            if query_override
            else model.objects.using(database).values_list(name_field, "pk")
        )
        name_id_mapping = bidict(query_set)
        lookup = AttributeLookup(model, name_id_mapping)

        # Create a bidict with name:id pairs
        LookupManager._lookups[lookup_key] = lookup
        return lookup

    @overload
    def lookup(self, *, attribute: type[Model] | str, value: int) -> str: ...
    @overload
    def lookup(self, *, attribute: type[Model] | str, value: str) -> int: ...
    def lookup(self, *, attribute: type[Model] | str, value: str | int) -> str | int:
        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)
        model_name = attribute._meta.object_name
        lookup = self._get_lookup(self.db, attribute)
        try:
            return lookup[value]
        except KeyError:
            raise KeyError(f"Unrecognized lookup key '{name}' for {model_name}")

    def attribute(self, attribute: type[Model] | str) -> AttributeLookup:
        """Get or generate a lookup for a specific attribute."""

        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)

        lookup = LookupManager._get_lookup(self.db, attribute)
        return lookup

    @property
    def public_datasets(self):
        key_name_override = "public_datasets"

        def query_override(model: type[Model]):
            return model.objects.filter(Public=True).values_list("Dataset", "pk")

        return self._get_lookup(self.db, Dataset, key_name_override, query_override)

    @staticmethod
    def admin_dataset_names():
        mexer = LookupManager("default")
        sandbox = LookupManager("sandbox")

        mexer_datasets = mexer.attribute(Dataset)
        sandbox_datasets = sandbox.attribute(Dataset)

        # Combine them and add the sandbox prefix
        # onto the sandbox datasets to differentiate.
        return mexer_datasets.names + [
            settings.SANDBOX_PREFIX + dataset for dataset in sandbox_datasets.names
        ]

    # TODO: This needs to be finished...
    @staticmethod
    def get_all_available(attribute: type[Model] | str):
        """Get all available values for a given attribute from the PSUT model."""

        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)

        _lookup = LookupManager._get_lookup(
            "default", attribute
        )  # TODO... which database?

        # Print distinct values for the attribute from the PSUT model
        # print(PSUT.objects.order_by().values_list(model_name, flat=True).distinct())
