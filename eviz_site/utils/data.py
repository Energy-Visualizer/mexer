####################################################################
# data.py includes all functions related to getting data from the databases
# 
# The general flow of getting data from a query is
#   shape_post_request(raw post request) -> cleaned_query
#   translate_query(cleaned_query) -> translated_query
# Then the "get" functions can be used:
#   get_sankey(translated_query)
#   OR get_translated_dataframe(translated_query)
#   OR get_xy(translated_query)
#   ETC.
# 
# One of the main parts abstracted by that flow is
# the database target. A database target is the combination
# of the database name and which model on the database for
# which a user is looking. This file includes all the logic
# to figure out the database target.
#
# The database target can be recieved from
#   shape_post_request(ret_database_target = True)
# And is passed to the "get" functions
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
from eviz.models import models, PSUT, IEAData, AggEtaPFU
from pandas import DataFrame
from utils.misc import Silent
import pandas.io.sql as pd_sql  # for getting data into a pandas dataframe
from django.db import connections
from utils.translator import Translator
from eviz_site.settings import DATABASES, SANDBOX_PREFIX

DatabaseTarget = tuple[str, models.Model]

def _get_database_target(query: dict) -> DatabaseTarget:
    dataset = query.get("dataset")

    plot_type = query.get("plot_type")
    if plot_type == "xy_plot":
        model = AggEtaPFU
    else:
        model = IEAData if dataset == "IEAEWEB2022" else PSUT
    
    return "sandbox" if dataset.startswith(SANDBOX_PREFIX) else "default", model

def _query_database(target: DatabaseTarget, query: dict, values: list[str]):
    db = target[0]
    model = target[1]

    if not _valid_database(db):
        raise ValueError("Unknown database specified for query")

    data = (
        model.objects
        .using(db)
        .values_list(*values)
        .filter(**query)
    )

    return data

def _valid_database(database_name: str):
    return database_name in DATABASES.keys()

def get_dataframe(target: DatabaseTarget, query: dict, columns: list) -> DataFrame:
    if not _valid_database(target[0]):
        return DataFrame() # empty data frame if database is wrong
    
    # get the data from database
    db_query = target[1].objects.filter(**query).values(*columns).query
    with Silent():
        df = pd_sql.read_sql_query(
            str(db_query),
            con=connections[target[0]].cursor().connection # get the connection associated with the requested database
        )
    
    return df

META_COLUMNS = ["Dataset", "ValidFromVersion", "ValidToVersion", "Country", "Method", "EnergyType", "LastStage", "IEAMW", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation"]
PSUT_COLUMNS = ["matname", "i", "j", "value"]
AGGETA_COLUMNS = ["GrossNet", "EXp", "EXf", "EXu", "etapf", "etafu", "etapu"]
def get_translated_dataframe(target: DatabaseTarget, query: dict, columns: list) -> DataFrame:
    df = get_dataframe(target, query, columns)

    # no need to do work if dataframe is empty (no data was found for the query)
    if df.empty: return df

    translator = Translator(target[0]) # get a translator for the correct database
    
    # Translate the DataFrame's column names
    translate_columns = {
        'Dataset': translator.dataset_translate,
        'ValidFromVersion': translator.version_translate,
        'ValidToVersion': translator.version_translate,
        'Country': translator.country_translate,
        'Method': translator.method_translate,
        'EnergyType': translator.energytype_translate,
        'LastStage': translator.laststage_translate,
        'IEAMW': translator.ieamw_translate,
        'ChoppedMat': translator.matname_translate,
        'ChoppedVar': translator.index_translate,
        'ProductAggregation': translator.agglevel_translate,
        'IndustryAggregation': translator.agglevel_translate,
        'matname': translator.matname_translate,
        'grossnet': translator.grossnet_translate,
        'i': translator.index_translate,
        'j': translator.index_translate
    }

    # Apply the translation functions to each column if it exists in the DataFrame
    for col, translate_func in translate_columns.items():
        if col in df.columns:
            df[col] = df[col].apply(translate_func)
    
    # Handle IncludesNEU separately as it's a boolean
    if 'IncludesNEU' in df.columns:
        df['IncludesNEU'] = df['IncludesNEU'].apply(lambda x: 'Yes' if x else 'No')
    
    return df

def get_csv_from_query(target: DatabaseTarget, query: dict, columns: list):
    
    # index false to not have column of row numbers
    return get_translated_dataframe(target, query, columns).to_csv(index=False)

def get_excel_from_query(target: DatabaseTarget, query: dict, columns = PSUT_COLUMNS):

    # index false to not have column of row numbers
    return get_translated_dataframe(target, query, columns).to_excel(index=False)

def shape_post_request(
    payload, ret_plot_type = False, ret_database_target = False
) -> tuple[dict, str, DatabaseTarget]:
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

    # get rid of security token, is not part of a query
    shaped_query.pop("csrfmiddlewaretoken", None)

    for k, v in shaped_query.items():
        # convert from list (if just one item in list)
        if len(v) == 1:
            shaped_query[k] = v[0]
    
    if ret_plot_type:
        plot_type = shaped_query.get("plot_type")

    if ret_database_target:
        # to be returned at the end
        db_target = _get_database_target(shaped_query)

    return tuple(
        [shaped_query]
        + ([plot_type] if ret_plot_type else [])
        + ([db_target] if ret_database_target else [])
    )

# TODO: rewrite this to use a for loop instead
def translate_query(
    target: DatabaseTarget,
    query: dict
) -> dict:
    '''Turn a query of human readable values from a form into a query read to hit the dataset

    Input:

        query, a dict: the query that should be translated

    Output:

        a dictionary of a query ready to hit the database
    '''

    translated_query = dict()  # set up to build and return at the end

    if not _valid_database(target[0]):
        raise ValueError("Unknown database specified for translating query")
    
    translator = Translator(target[0]) # get a translator for the correct database

    # get rid of sandbox prefix on the query parameter
    # or else it won't be recognized for translation
    for k in query.keys():
        query[k] = query[k].removeprefix(SANDBOX_PREFIX)

    # common query parts
    if v := query.get("dataset"):
        translated_query["Dataset"] = translator.dataset_translate(v)
    if v := query.get("version"):
        translated_query["ValidFromVersion__gte"] = translator.version_translate(v)
        translated_query["ValidToVersion__lte"] = translator.version_translate(v)
    if v := query.get("country"):
        if type(v) == list:
            translated_query["Country__in"] = [
                translator.country_translate(country) for country in v]
        else:
            translated_query["Country"] = translator.country_translate(v)
    if v := query.get("method"):
        if type(v) == list:
            translated_query["Method__in"] = [
                translator.method_translate(method) for method in v]
        else:
            translated_query["Method"] = translator.method_translate(v)
    if v := query.get("energy_type"):
        if type(v) == list:
            translated_query["EnergyType__in"] = [
                translator.energytype_translate(energy_type) for energy_type in v]
        else:
            translated_query["EnergyType"] = translator.energytype_translate(v)
    if v := query.get("last_stage"):
        translated_query["LastStage"] = translator.laststage_translate(v)
    if v := query.get("ieamw"):
        if type(v) == list:
            # both were selected, use the both option in the table
            translated_query["IEAMW"] = translator.ieamw_translate("Both")
        else:
            translated_query["IEAMW"] = translator.ieamw_translate(v)
    # includes neu either is in the query or not, it's value does need to be more than empty string, though
    translated_query["IncludesNEU"] = translator.includesNEU_translate(
        bool(query.get("includes_neu")))
    if v := query.get("chopped_mat"):
        translated_query["ChoppedMat"] = translator.matname_translate(v)
    if v := query.get("chopped_var"):
        translated_query["ChoppedVar"] = translator.index_translate(v)
    if v := query.get("product_aggregation"):
        translated_query["ProductAggregation"] = translator.agglevel_translate(v)
    if v := query.get("industry_aggregation"):
        translated_query["IndustryAggregation"] = translator.agglevel_translate(v)
    if v := query.get("grossnet"):
        translated_query["GrossNet"] = translator.grossnet_translate(v)
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
            translated_query["matname__in"] = [
                translator.matname_translate("R"),
                translator.matname_translate("U"),
                translator.matname_translate("V"),
                translator.matname_translate("Y")
            ]
        else:
            translated_query["matname"] = translator.matname_translate(v)

    return translated_query