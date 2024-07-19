from eviz.models import models, PSUT
from pandas import DataFrame
from utils.misc import Silent
import pandas.io.sql as pd_sql  # for getting data into a pandas dataframe
from django.db import connections
from utils.translator import Translator

def get_dataframe(model: models.Model, query: dict, columns: list) -> DataFrame:
    if (db := get_database(query)) is None:
        return DataFrame() # empty data frame if database is wrong
    
    # get the data from database
    db_query = model.objects.filter(**query).values(*columns).query
    with Silent():
        df = pd_sql.read_sql_query(
            str(db_query),
            con=connections[db].cursor().connection # get the connection associated with the requested database
        )
    
    return df

COLUMNS = ["Dataset", "Country", "Method", "EnergyType", "LastStage", "IEAMW", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation", "matname", "i", "j", "x"]
def get_translated_dataframe(model: models.Model, query: dict, columns: list) -> DataFrame:
    df = get_dataframe(model, query, columns)

    # no need to do work if dataframe is empty (no data was found for the query)
    if df.empty: return df
    
    # Translate the DataFrame's column names
    translate_columns = {
        'Dataset': Translator.dataset_translate,
        'Country': Translator.country_translate,
        'Method': Translator.method_translate,
        'EnergyType': Translator.energytype_translate,
        'LastStage': Translator.laststage_translate,
        'IEAMW': Translator.ieamw_translate,
        'ChoppedMat': Translator.matname_translate,
        'ChoppedVar': Translator.index_translate,
        'ProductAggregation': Translator.agglevel_translate,
        'IndustryAggregation': Translator.agglevel_translate,
        'matname': Translator.matname_translate,
        'grossnet': Translator.grossnet_translate,
        'i': Translator.index_translate,
        'j': Translator.index_translate
    }

    # Apply the translation functions to each column if it exists in the DataFrame
    for col, translate_func in translate_columns.items():
        if col in df.columns:
            df[col] = df[col].apply(translate_func)
    
    # Handle IncludesNEU separately as it's a boolean
    if 'IncludesNEU' in df.columns:
        df['IncludesNEU'] = df['IncludesNEU'].apply(lambda x: 'Yes' if x else 'No')
    
    return df

def get_csv_from_query(query: dict, columns: list = COLUMNS):
    
    # index false to not have column of row numbers
    return get_translated_dataframe(PSUT, query, columns).to_csv(index=False)

def get_excel_from_query(query: dict, columns = COLUMNS):

    # index false to not have column of row numbers
    return get_translated_dataframe(PSUT, query, columns).to_excel(index=False)

def translate_query(
    query: dict
) -> dict:
    '''Turn a query of human readable values from a form into a query read to hit the dataset

    Input:

        query, a dict: the query that should be translated

    Output:

        a dictionary of a query ready to hit the database
    '''

    translated_query = dict()  # set up to build and return at the end

    if (database := get_database(query)) is None:
        raise ValueError("Unknown database specified for translating query")

    # common query parts
    if v := query.get("dataset"):
        translated_query["Dataset"] = Translator.dataset_translate(v, database)
    if v := query.get("country"):
        if type(v) == list:
            translated_query["Country__in"] = [
                Translator.country_translate(country, database) for country in v]
        else:
            translated_query["Country"] = Translator.country_translate(v, database)
    if v := query.get("method"):
        if type(v) == list:
            translated_query["Method__in"] = [
                Translator.method_translate(method, database) for method in v]
        else:
            translated_query["Method"] = Translator.method_translate(v, database)
    if v := query.get("energy_type"):
        if type(v) == list:
            translated_query["EnergyType__in"] = [
                Translator.energytype_translate(energy_type, database) for energy_type in v]
        else:
            translated_query["EnergyType"] = Translator.energytype_translate(v, database)
    if v := query.get("last_stage"):
        translated_query["LastStage"] = Translator.laststage_translate(v, database)
    if v := query.get("ieamw"):
        if type(v) == list:
            # both were selected, use the both option in the table
            translated_query["IEAMW"] = Translator.ieamw_translate("Both", database)
        else:
            translated_query["IEAMW"] = Translator.ieamw_translate(v, database)
    # includes neu either is in the query or not, it's value does need to be more than empty string, though
    translated_query["IncludesNEU"] = Translator.includesNEU_translate(
        bool(query.get("includes_neu")))
    if v := query.get("chopped_mat"):
        translated_query["ChoppedMat"] = Translator.matname_translate(v, database)
    if v := query.get("chopped_var"):
        translated_query["ChoppedVar"] = Translator.index_translate(v, database)
    if v := query.get("product_aggregation"):
        translated_query["ProductAggregation"] = Translator.agglevel_translate(
            v, database)
    if v := query.get("industry_aggregation"):
        translated_query["IndustryAggregation"] = Translator.agglevel_translate(
            v, database)
    if v := query.get("grossnet"):
        translated_query["GrossNet"] = Translator.grossnet_translate(
            v, database)
    # plot-specific query parts
    if v := query.get("to_year"):
        # if year part is a range of years, i.e. to_year present
        # set up query as range
        translated_query["Year__lte"] = int(v)
        if v := query.get("year"):
            translated_query["Year__gte"] = int(v)
    elif v := query.get("year"):
        # else just have year be one year
        translated_query["Year"] = int(v)
    if v := query.get("matname"):
        if v == "RUVY":
            translated_query["matname__in"] = [Translator.matname_translate("R", database), Translator.matname_translate("U", database), Translator.matname_translate("V", database), Translator.matname_translate("Y", database)]
        else:
            translated_query["matname"] = Translator.matname_translate(v, database)

    return translated_query

def shape_post_request(
    payload, get_plot_type = False, get_database = False
) -> tuple[str, dict]:
    '''Turn a POST request payload into a ready to use query in a dictionary

    Input:

        payload, some dict-like (used with Django HttpRequest POST attributes): 
        the POST payload to shape into a query dictionary

        get_plot_type, bool: whether or not to get and give the plot type in the payload

    Output:

        a dictionary containing all the associations of a query parts and their values

        IF get_plot_type is True:

            2-tuple containing in top-down order

                a string telling the plot type requested

                a dictionary containing all the associations of a query parts and their values
    '''

    shaped_query = dict(payload)

    if get_plot_type:
        try:
            # to be returned at the end
            plot_type = shaped_query.pop("plot_type")[0]
        except KeyError:
            plot_type = None

    if get_database:
        # to be returned at the end
        db = shaped_query.get("dataset")[0]

    # get rid of security token, is not part of a query
    shaped_query.pop("csrfmiddlewaretoken", None)

    for k, v in shaped_query.items():

        # convert from list (if just one item in list)
        if len(v) == 1:
            shaped_query[k] = v[0]

    return tuple(
        [shaped_query]
        + ([plot_type] if get_plot_type else [])
        + ([db] if get_database else [])
    )

# TODO: is this all temp? do we want to keep all the data in seperate db's or will we actually use the dataset column?
def get_database(query: dict) -> str:
    """Determine the appropriate database to use based on the query parameters.

    Input:
        query (dict): A dictionary containing query parameters, including a 'Dataset' key.

    Output:
        str or None: The name of the database to use, or None if the database is invalid.
    """
    
    # Translate the 'Dataset' value from the query to a database identifier
    db = query.get("dataset")
    if db is None:
        return None
    
    if type(db) is int:
        try:
            db = Translator.dataset_translate(db, "default")
        except:
            raise Exception("Could not translate dataset")
    
    # TODO: this is missing IEA, we have to get where that is
    if db not in ["CLPFUv2.0a1", "CLPFUv2.0a2", "CLPFUv2.0a3"]:
        return None # database is invalid
    return db