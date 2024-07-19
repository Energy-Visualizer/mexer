# translator.py contains the functionality to quickly translate PSUT values
# to and from human readable form and numerical database form
#
# Authors: Kenny Howes - kmh67@calvin.edu
#          Edom Maru
##################################################

from bidict import bidict
from django.apps import apps
from eviz.models import PSUT

class Translator:
    # A dictionary where keys are model names and values are bidict objects
    __translations = {}

    @staticmethod
    def __load_bidict(model_name: str, id_field: str, name_field: str, db: str) -> bidict:
        """
        Load translations for a specific model if not already loaded.
        
        Args:
            model_name (str): The name of the model to load translations for.
            id_field (str): The name of the ID field in the model.
            name_field (str): The name of the field containing the human-readable name.
        
        Returns:
            bidict: A bidirectional dictionary of translations for the model.
        """
        if (model_name + db) not in Translator.__translations:
            # Get the model class dynamically
            model = apps.get_model(app_label='eviz', model_name=model_name)
            # Create a bidict with name:id pairs
            Translator.__translations[model_name + db] = bidict(
                {getattr(item, name_field): getattr(item, id_field) for item in model.objects.using(db).all()}
            )
        return Translator.__translations[model_name + db]

    @staticmethod
    def _translate(model_name, value, id_field, name_field, db):
        # Translate a value between its ID and name for a specific model.
        # value: The value to translate (can be either an ID or a name).
        # Returns: The translated value (either ID or name, depending on input).
        translations = Translator.__load_bidict(model_name, id_field, name_field, db)
        
        # try to get the translation
        if translation := translations.get(value) or translations.inverse.get(value):
            return translation
        
        # if no translation found
        raise KeyError("Unrecognized key '" + value + "' for " + model_name)

    # The following methods are specific translation functions for different models
    # They all use the _translate method with appropriate parameters
    @staticmethod
    def index_translate(value, db_name: str):
        return Translator._translate('Index', value, 'IndexID', 'Index', db_name)

    @staticmethod
    def dataset_translate(value, db_name: str):
        return Translator._translate('Dataset', value, 'DatasetID', 'Dataset', db_name)

    @staticmethod
    def country_translate(value, db_name: str):
        return Translator._translate('Country', value, 'CountryID', 'FullName', db_name)

    @staticmethod
    def method_translate(value, db_name: str):
        return Translator._translate('Method', value, 'MethodID', 'Method', db_name)

    @staticmethod
    def energytype_translate(value, db_name: str):
        return Translator._translate('EnergyType', value, 'EnergyTypeID', 'FullName', db_name)

    @staticmethod
    def laststage_translate(value, db_name: str):
        return Translator._translate('LastStage', value, 'ECCStageID', 'ECCStage', db_name)

    @staticmethod
    def ieamw_translate(value, db_name: str):
        return Translator._translate('IEAMW', value, 'IEAMWID', 'IEAMW', db_name)

    @staticmethod
    def matname_translate(value, db_name: str):
        return Translator._translate('matname', value, 'matnameID', 'matname', db_name)
    @staticmethod
    def grossnet_translate(value, db_name: str):
        return Translator._translate('GrossNet', value, 'GrossNetID', 'GrossNet', db_name)

    @staticmethod
    def agglevel_translate(value, db_name: str):
        return Translator._translate('AggLevel', value, 'AggLevelID', 'AggLevel', db_name)

    @staticmethod
    def includesNEU_translate(value):
        return int(value) if isinstance(value, bool) else int(bool(value))

    @staticmethod
    def get_all(attribute):
        """
        Get all possible values for a given attribute.
        
        Inputs:
            attribute (str): The name of the attribute to get values for.
        
        Outputs:
            list: A list of all possible values (names) for the attribute.
        """
        # Dictionary mapping attribute names to model details
        model_mappings = {
            'dataset': ('Dataset', 'DatasetID', 'Dataset'),
            'country': ('Country', 'CountryID', 'FullName'),
            'method': ('Method', 'MethodID', 'Method'),
            'energytype': ('EnergyType', 'EnergyTypeID', 'FullName'),
            'laststage': ('LastStage', 'ECCStageID', 'ECCStage'),
            'ieamw': ('IEAMW', 'IEAMWID', 'IEAMW'),
            'matname': ('matname', 'matnameID', 'matname'),
            'agglevel': ('AggLevel', 'AggLevelID', 'AggLevel'),
            'grossnet': ('GrossNet', 'GrossNetID', 'GrossNet'),
        }
        
        if attribute not in model_mappings:
            raise ValueError(f"Unknown attribute: {attribute}")
        
        # Get model details and load translations
        model_name, id_field, name_field = model_mappings[attribute]
        translations = Translator.__load_bidict(model_name, id_field, name_field, "default")
        return list(translations.keys())

    # TODO: This needs to be finished...
    @staticmethod
    def get_all_available(attribute):
        """Get all available values for a given attribute from the PSUT model.
        
        Inputs:
            attribute (str): The name of the attribute to get values for.
        
        Outputs:
            A list of distinct values for the attribute from the PSUT model.
        """
        # Dictionary mapping attribute names to model details
        model_mappings = {
            'dataset': ('Dataset', 'DatasetID', 'Dataset'),
            'country': ('Country', 'CountryID', 'FullName'),
            'method': ('Method', 'MethodID', 'Method'),
            'energytype': ('EnergyType', 'EnergyTypeID', 'FullName'),
            'laststage': ('LastStage', 'ECCStageID', 'ECCStage'),
            'ieamw': ('IEAMW', 'IEAMWID', 'IEAMW'),
            'matname': ('matname', 'matnameID', 'matname'),
            'agglevel': ('AggLevel', 'AggLevelID', 'AggLevel'),
            'grossnet': ('GrossNet', 'GrossNetID', 'GrossNet'),
        }
        
        if attribute not in model_mappings:
            raise ValueError(f"Unknown attribute: {attribute}")
        
        model_name, id_field, name_field = model_mappings[attribute]
        translations = Translator.__load_bidict(model_name, id_field, name_field)

        # Print distinct values for the attribute from the PSUT model
        print(PSUT.objects.order_by().values_list(model_name, flat=True).distinct())

    @staticmethod
    def get_includesNEUs():
        return [True, False]