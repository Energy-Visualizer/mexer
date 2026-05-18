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
import io
from collections.abc import Callable
from typing import Any, Literal, cast

import pandas as pd
import pandas.io.sql as pd_sql  # for getting data into a pandas dataframe
from django.conf import settings
from django.db import connections
from django.http import QueryDict
from Mexer.models import PSUT, AggEtaPFU, IEAData, models

from utils.logging import LOGGER
from utils.misc import ShapedQuery, Silent
from utils.translator import Translator

type DatabaseSource = Literal["sandbox", "users", "default"]

type DatabaseTarget = tuple[DatabaseSource, type[models.Model]]


def get_database_target(query: ShapedQuery) -> DatabaseTarget:
    dataset = query.get("dataset")
    table_name = None
    is_sandbox = False
    if isinstance(dataset, str):
        is_sandbox = dataset.startswith(settings.SANDBOX_PREFIX)
        table_name = dataset.removeprefix(settings.SANDBOX_PREFIX)

    plot_type = query.get("plot_type")
    if plot_type == "xy_plot":
        model = AggEtaPFU
    else:
        model = IEAData if table_name == "IEAEWEB2022" else PSUT

    source = "sandbox" if is_sandbox else "default"
    return source, model


def _valid_database(database_name: str):
    return database_name in settings.DATABASES.keys()


def query_database(target: DatabaseTarget, query: dict, values: list[str]):
    db = target[0]
    model = target[1]

    if not _valid_database(db):
        raise ValueError("Unknown database specified for query")

    data = model.objects.using(db).values_list(*values).filter(**query)

    LOGGER.debug(f"Query is {query}")

    return data


def get_dataframe(target: DatabaseTarget, query: dict, columns: list) -> pd.DataFrame:
    db_source, db_model = target
    if not _valid_database(db_source):
        # Invalid database, empty data frame.
        return pd.DataFrame()

    LOGGER.info(str(query))

    db_query = db_model.objects.filter(**query).values(*columns).query

    # Intercept database connection and read query to a pandas data frame.
    with Silent():
        df = pd_sql.read_sql_query(
            str(db_query),
            con=connections[db_source].cursor().connection,
        )

    return df


# TODO: We need to "discover" these columns, not
# hardcode them.

META_COLUMNS = [
    "dataset",
    "valid_from_version",
    "valid_to_version",
    "country",
    "method",
    "entry_type",
    "last_stage",
    "includes_neu",
    "year",
    "chopped_mat",
    "chopped_var",
    "product_aggregation",
    "industry_aggregation",
]
PSUT_COLUMNS = ["matname", "i", "j", "value"]
AGGETA_COLUMNS = ["gross_net", "ex_p", "ex_f", "ex_u", "etapf", "etafu", "etapu"]


def get_translated_dataframe(
    target: DatabaseTarget, query: dict[str, Any], columns: list
) -> pd.DataFrame:
    df = get_dataframe(target, query, columns)

    # no need to do work if dataframe is empty (no data was found for the query)
    if df.empty:
        return df

    translator = Translator(target[0])  # get a translator for the correct database

    # Translate the DataFrame's column names
    translate_columns = {
        "dataset": translator.dataset_translate,
        "valid_from_version": translator.version_translate,
        "valid_to_version": translator.version_translate,
        "country": translator.country_translate,
        "method": translator.method_translate,
        "entry_type": translator.energytype_translate,
        "last_stage": translator.laststage_translate,
        "chopped_mat": translator.matname_translate,
        "chopped_var": translator.index_translate,
        "product_aggregation": translator.agglevel_translate,
        "industry_aggregation": translator.agglevel_translate,
        "matname": translator.matname_translate,
        "gross_net": translator.grossnet_translate,
        "i": translator.index_translate,
        "j": translator.index_translate,
    }

    # Apply the translation functions to each column if it exists in the DataFrame
    for col, translate_func in translate_columns.items():
        if col in df.columns:
            df[col] = df[col].apply(translate_func)

    # Handle IncludesNEU separately as it's a boolean
    if "includes_neu" in df.columns:
        df["includes_neu"] = df["includes_neu"].apply(lambda x: "Yes" if x else "No")

    return df


def get_csv_from_query(target: DatabaseTarget, query: dict, columns: list) -> str:
    ROW_NUMS = False
    return get_translated_dataframe(target, query, columns).to_csv(index=ROW_NUMS)


def get_excel_from_query(
    target: DatabaseTarget, query: dict, columns=PSUT_COLUMNS
) -> bytes:
    ROW_NUMS = False
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        get_translated_dataframe(target, query, columns).to_excel(
            writer, index=ROW_NUMS
        )
    return buffer.getvalue()


def shape_post_request(
    params: QueryDict,
) -> tuple[ShapedQuery, str | None, DatabaseTarget]:
    """Turn a POST request payload into a ready to use query in a dictionary

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
    """

    # Get rid of security token; it is not part of a query.
    SKIP_PARAMS = ("csrfmiddlewaretoken",)

    # Shaped query extracts items from lists.
    def shaped_value(key: str, value: str | list[object]) -> str | list[str] | None:
        if key in SKIP_PARAMS:
            return None
        if isinstance(value, str):
            return value
        if len(value) == 1 and isinstance(value[0], str):
            return value[0]
        if all(isinstance(item, str) for item in value):
            return cast(list[str], value)
        LOGGER.warning(f"Non-string POST param for key {key}")

    shaped_query = {
        key: value
        for key in params
        if (value := shaped_value(key, params[key])) is not None
    }
    plot_type = str(shaped_query.get("plot_type"))
    db_target = get_database_target(shaped_query)
    return shaped_query, plot_type, db_target


def _str_or_all_list[T](value: str | list[str], op: Callable[[str], T]) -> T | list[T]:
    if isinstance(value, str):
        return op(value)
    else:
        return [op(item) for item in value]


# TODO: rewrite this to use a for loop instead
def translate_query(target: DatabaseTarget, query: ShapedQuery) -> dict[str, Any]:
    """Turn a query of human readable values from a form into a query read to hit the dataset

    Input:

        query, a dict: the query that should be translated

    Output:

        a dictionary of a query ready to hit the database
    """

    translated = dict()
    db_source, _ = target

    if not _valid_database(db_source):
        raise ValueError("Unknown database specified for translating query")

    translator = Translator(db_source)

    # Clear sandbox prefix from query parameters;
    # translation will not recognize sandbox prefix.
    query = {
        k: _str_or_all_list(query[k], lambda v: v.removeprefix(settings.SANDBOX_PREFIX))
        for k in query
    }

    # common query parts
    if v := query.get("dataset"):
        translated["Dataset"] = translator.dataset_translate(v)
    if v := query.get("version"):
        translated["ValidFromVersion__lte"] = translator.version_translate(v)
        translated["ValidToVersion__gte"] = translator.version_translate(v)
    if v := query.get("country"):
        if isinstance(v, list):
            translated["Country__in"] = [
                translator.country_translate(country) for country in v
            ]
        else:
            translated["Country"] = translator.country_translate(v)
    if v := query.get("method"):
        if isinstance(v, list):
            translated["Method__in"] = [
                translator.method_translate(method) for method in v
            ]
        else:
            translated["Method"] = translator.method_translate(v)
    if v := query.get("energy_type"):
        if isinstance(v, list):
            translated["EnergyType__in"] = [
                translator.energytype_translate(energy_type) for energy_type in v
            ]
        else:
            translated["EnergyType"] = translator.energytype_translate(v)
    if v := query.get("last_stage"):
        translated["LastStage"] = translator.laststage_translate(v)
    # includes neu either is in the query or not, it's value does need to be more than empty string, though
    translated["IncludesNEU"] = int(bool(query.get("including_neu")))
    if v := query.get("chopped_mat"):
        translated["ChoppedMat"] = translator.matname_translate(v)
    if v := query.get("chopped_var"):
        translated["ChoppedVar"] = translator.index_translate(v)
    if v := query.get("product_aggregation"):
        translated["ProductAggregation"] = translator.agglevel_translate(v)
    if v := query.get("industry_aggregation"):
        translated["IndustryAggregation"] = translator.agglevel_translate(v)
    if v := query.get("grossnet"):
        translated["GrossNet"] = translator.grossnet_translate(v)
    # plot-specific query parts
    if (v := query.get("to_year")) and isinstance(v, str):
        # if year part is a range of years, i.e. to_year present
        # set up query as range
        translated["Year__lte"] = int(v)
        if (v := query.get("year")) and isinstance(v, str):
            translated["Year__gte"] = int(v)
    elif (v := query.get("year")) and isinstance(v, str):
        # else just have year be one year
        translated["Year"] = int(v)
    if v := query.get("matname"):
        if v == "RUVY":
            translated["matname__in"] = [
                translator.matname_translate("R"),
                translator.matname_translate("U"),
                translator.matname_translate("V"),
                translator.matname_translate("Y"),
            ]
        else:
            translated["matname"] = translator.matname_translate(v)

    LOGGER.debug(f"Translated query: {translated}")
    return translated
