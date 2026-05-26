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

import Mexer.models as models
import pandas as pd
import pandas.io.sql as pd_sql  # for getting data into a pandas dataframe
from django.conf import settings
from django.db import connections
from django.db.models import Model
from django.http import QueryDict

from Mexer_site.devscripts.generate_models import column_field_name
from utils.logging import LOGGER
from utils.lookup import LookupManager, get_attribute
from utils.misc import ShapedQuery, Silent

type DatabaseSource = Literal["sandbox", "users", "default"]

type DatabaseTarget = tuple[DatabaseSource, type[Model]]


def get_database_target(query: ShapedQuery) -> DatabaseTarget:
    dataset = query.get("dataset")
    table_name = None
    is_sandbox = False
    if isinstance(dataset, str):
        is_sandbox = dataset.startswith(settings.SANDBOX_PREFIX)
        table_name = dataset.removeprefix(settings.SANDBOX_PREFIX)

    plot_type = query.get("plot_type")
    if plot_type == "xy_plot":
        model = models.AggEtaPFU
    else:
        model = models.IEAData if table_name == "IEAEWEB2022" else models.PSUT

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


def get_dataframe(
    target: DatabaseTarget, query: dict[str, Any], columns: list
) -> pd.DataFrame:
    db_source, db_model = target
    if not _valid_database(db_source):
        # Invalid database, empty data frame.
        return pd.DataFrame()

    LOGGER.info(f"Query being passed to filter: {query}")

    # Default sort: chronological.
    # Expand on sorting options in the future.
    db_query = (
        db_model.objects.using(db_source)
        .filter(**query)
        .values(*columns)
        .order_by("Year")
        .query
    )

    try:
        sql = str(db_query)
    except Exception as e:
        LOGGER.error(f"Query compilation failed: {e}")
        LOGGER.error(f"Raw query dict: {query}")
        return pd.DataFrame()

    # Intercept database connection and read query to a pandas data frame.
    with Silent():
        df = pd_sql.read_sql_query(
            sql,
            con=connections[db_source].cursor().connection,
        )

    return df


# TODO: We need to "discover" these columns, not
# hardcode them.

PSUT_COLUMNS = ["matname", "i", "j", "value"]
AGGETA_COLUMNS = ["gross_net", "ex_p", "ex_f", "ex_u", "etapf", "etafu", "etapu"]


def get_userfriendly_dataframe(
    target: DatabaseTarget, query: dict[str, Any], columns: list
) -> pd.DataFrame:
    """Translate database IDs and other numerical values into
    named textual counterparts."""

    df = get_dataframe(target, query, columns)

    if df.empty:
        return df

    database = target[0]
    lookups = LookupManager(database)

    # Translate IDs into names when appropriate.
    for column in df.columns:
        if not get_attribute(column):
            continue

        def transform(value):
            return lookups.lookup(attribute=column, value=value)

        df[column] = df[column].apply(transform)

    # Handle IncludesNEU separately as it's a boolean.
    if "IncludesNEU" in df.columns:
        df["IncludesNEU"] = df["IncludesNEU"].apply(lambda inc: "Yes" if inc else "No")

    return df


def get_csv_from_query(target: DatabaseTarget, query: dict, columns: list) -> str:
    ROW_NUMS = False
    return get_userfriendly_dataframe(target, query, columns).to_csv(index=ROW_NUMS)


def get_excel_from_query(
    target: DatabaseTarget, query: dict, columns=PSUT_COLUMNS
) -> bytes:
    ROW_NUMS = False
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        get_userfriendly_dataframe(target, query, columns).to_excel(
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


def translate_query(target: DatabaseTarget, query: ShapedQuery) -> dict[str, Any]:
    """Turn a query of human readable values from a form into a query read to hit the dataset

    Input:

        query, a dict: the query that should be translated

    Output:

        a dictionary of a query ready to hit the database
    """

    final_query: dict[str, Any] = dict()
    db_source, _ = target

    if not _valid_database(db_source):
        raise ValueError("Unknown database specified for translating query")

    lookups = LookupManager(db_source)

    # Clear sandbox prefix from query parameters;
    # translation will not recognize sandbox prefix.
    query = {
        k: _str_or_all_list(query[k], lambda v: v.removeprefix(settings.SANDBOX_PREFIX))
        for k in query
    }

    SPECIAL_CASES = (models.Version, models.Year)

    # Override RUVY for matname query.
    if "matname" in query and query["matname"] == "RUVY":
        query["matname"] = list("RUVY")

    # Translate names to IDs for lookup attributes.
    for param, arg in query.items():
        attribute = get_attribute(param)
        if not attribute:
            final_query[param] = arg
            continue
        if attribute in SPECIAL_CASES:
            continue

        # The column name is derived from the Python-ified DB table name.
        column_name = column_field_name(str(attribute._meta.db_table))

        lookup = lookups[attribute]
        if isinstance(arg, list):
            final_query_constraint = f"{column_name}__in"
            final_arg = [lookup[item] for item in arg]
        else:
            final_query_constraint = column_name
            final_arg = lookup[arg]
        final_query[final_query_constraint] = final_arg

    # Special query parameters.

    final_query["includes_neu"] = int(bool(query.get("IncludesNEU")))

    # Version range handling.
    if isinstance(v := query.get("version"), str):
        version = lookups[models.Version][v]
        final_query["valid_from_version__lte"] = version
        final_query["valid_to_version__gte"] = version

    # Year handling.
    if isinstance(v := query.get("to_year"), str):
        final_query["year__lte"] = int(v)
        if isinstance(v := query.get("year"), str):
            final_query["year__gte"] = int(v)
    elif isinstance(v := query.get("year"), str):
        final_query["year"] = int(v)

    LOGGER.debug(f"Translated query: {final_query}")
    return final_query
