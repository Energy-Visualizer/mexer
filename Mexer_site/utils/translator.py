####################################################################
# translator.py contains the functionality to quickly translate PSUT values
# to and from human readable form and numerical database form
#
# Since the "translation" tables in the database are fairly small,
# it's quicker to load them as dictionaries in memory and use them
# instead of doing foreign key translation database-side.
#
# Any results from the database are globally cached for
# TRANSLATOR_CACHE_TTL number of hours. All users use the same dictionaries
# for translations, so little memory is used for this as possible.
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu
#####################
from collections.abc import Callable
from curses import keyname
from datetime import date, datetime, timedelta

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
TRANSLATOR_CACHE_TTL = timedelta(hours=24.0)

# Some models have a full_name field which represents the name half
# of the translation.
#
# If this field is not present on the model, the model name itself
# should be the name of the name field.
FULLNAME_FIELD_NAME = "full_name"


# Determines if a table is a candidate for translation.
# Returns the table's name field.
def _is_translated(model: type[Model]) -> str | None:
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


# Models eligible for translation are those used to narrow
# DB queries, called "attributes", i.e. they are the targets
# of the many foreign-key columns present in data-source tables.
#
# Derived programatically: all tables that have a full-name
# column or a name column with the same name as themselves,
# and have a single integer primary key column.
ATTRIBUTES = {
    model: name
    for model in mexer_config.get_models()
    if (name := _is_translated(model))
}


type _QueryOverride = Callable[[type[Model]], QuerySet]


def _get_entry_key(
    database: DatabaseSource, model: type[Model], key_name_override: str | None
) -> str:
    model_name = key_name_override if key_name_override else model._meta.object_name
    return f"{database}:{model_name}"


class TranslatorEntry:
    attribute: type[Model]
    created_at: datetime
    translations: bidict[str, int]

    def __init__(
        self,
        attribute: type[Model],
        translations: bidict[str, int],
        created_at: datetime | None = None,
    ):
        self.attribute = attribute
        self.translations = translations
        self.created_at = created_at or datetime.now()

    @property
    def age(self) -> timedelta:
        return datetime.now() - self.created_at

    @property
    def options(self) -> list[str]:
        """Return the valid options (names) for this attribute."""
        return list(self.translations.keys())

    def expired(self, ttl=TRANSLATOR_CACHE_TTL) -> bool:
        return self.age > ttl


class Translator:
    # A dictionary where keys are model names and
    # values are tuples of date times and bidict objects
    # the date times mark when the entry was cached
    # the bidict has the translation information
    _translations: dict[str, TranslatorEntry] = {}

    # A tuple of a datetime of when this entry was cached
    # and a list of strings for all the public datasets
    _public_datasets: TranslatorEntry | None = None

    db: DatabaseSource

    def __init__(self, database: DatabaseSource = "default"):
        self.db = database

    @staticmethod
    def _get_entry(
        database: DatabaseSource,
        model: type[Model],
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> TranslatorEntry:
        """
        Load translations for a specific model if not already loaded.

        Args:
            model_name (str): The name of the model to load translations for.
            id_field (str): The name of the ID field in the model.
            name_field (str): The name of the field containing the human-readable name.

        Returns:
            bidict: A bidirectional dictionary of translations for the model.
        """

        def new_entry():
            return Translator._generate_entry(
                database, model, key_name_override, query_override
            )

        translation_key = _get_entry_key(database, model, key_name_override)
        if translation_key not in Translator._translations:
            # Reload, translation key not present.
            entry = new_entry()
        else:
            # Load cached translation.
            entry = Translator._translations[translation_key]
            if entry.expired():
                # Refresh.
                entry = new_entry()
        return entry

    @staticmethod
    def _generate_entry(
        database: DatabaseSource,
        model: type[Model],
        key_name_override: str | None = None,
        query_override: _QueryOverride | None = None,
    ) -> TranslatorEntry:
        if model not in ATTRIBUTES:
            raise ValueError(f"Model kind {model} ineligible for translation")

        translation_key = _get_entry_key(database, model, key_name_override)
        LOGGER.info(f"Loading and caching {translation_key}")

        name_field = ATTRIBUTES[model]

        # Create a mapping between the value of the model's
        # name field and the value of the model's ID field.
        query_set = (
            query_override(model)
            if query_override
            else model.objects.using(database).values_list(name_field, "pk")
        )
        name_id_mapping = bidict(query_set)
        translation = TranslatorEntry(model, name_id_mapping)

        # Create a bidict with name:id pairs
        Translator._translations[translation_key] = translation
        return translation

    def translate_id(self, *, attribute: type[Model] | str, id: int) -> str:
        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)
        model_name = attribute._meta.object_name
        entry = self._get_entry(self.db, attribute)
        try:
            return entry.translations.inverse[id]
        except KeyError:
            raise KeyError(f"Unrecognized ID {id} for {model_name}")

    def translate_name(self, *, attribute: type[Model] | str, name: str) -> int:
        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)
        model_name = attribute._meta.object_name
        entry = self._get_entry(self.db, attribute)
        try:
            return entry.translations[name]
        except KeyError:
            raise KeyError(f"Unrecognized entry '{name}' for {model_name}")

    def translate(self, *, attribute: type[Model] | str, value: str | int) -> str | int:
        if isinstance(value, str):
            return self.translate_name(attribute=attribute, name=value)
        else:
            return self.translate_id(attribute=attribute, id=value)

    def get_translations(self, attribute: type[Model] | str) -> TranslatorEntry:
        """Get all possible name/id pairs for a given attribute."""

        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)

        translations = Translator._get_entry(self.db, attribute)
        return translations

    @property
    def public_datasets(self):
        key_name_override = "public_datasets"

        def query_override(model: type[Model]):
            return model.objects.filter(Public=True).values_list("Dataset", "pk")

        return self._get_entry(self.db, Dataset, key_name_override, query_override)

    @staticmethod
    def admin_dataset_names():
        mexer = Translator("default")
        sandbox = Translator("sandbox")

        mexer_datasets = mexer.get_translations(Dataset)
        sandbox_datasets = sandbox.get_translations(Dataset)

        # Combine them and add the sandbox prefix
        # onto the sandbox datasets to differentiate.
        return mexer_datasets.options + [
            settings.SANDBOX_PREFIX + dataset for dataset in sandbox_datasets.options
        ]

    # TODO: This needs to be finished...
    @staticmethod
    def get_all_available(attribute: type[Model] | str):
        """Get all available values for a given attribute from the PSUT model."""

        if isinstance(attribute, str):
            attribute = mexer_config.get_model(attribute)

        _translations = Translator._get_entry(
            "default", attribute
        )  # TODO... which database?

        # Print distinct values for the attribute from the PSUT model
        # print(PSUT.objects.order_by().values_list(model_name, flat=True).distinct())
