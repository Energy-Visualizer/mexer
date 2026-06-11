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
from collections.abc import Callable, Iterable
from typing import Any, Literal

import Mexer.models as models
import pandas as pd
from django.conf import settings
from django.db.models import Exists, Model, OuterRef
from django.http import QueryDict

from utils.logging import LOGGER
from utils.lookup import (
    Attribute,
    LookupManager,
    get_attributes,
    get_foreign_attribute,
)
from utils.misc import ShapedQuery

type DatabaseSource = Literal["sandbox", "users", "default"]

type DatabaseTarget = tuple[DatabaseSource, type[Model]]

USER_TABLES: list[type[Model]] = [
    models.PSUTReAllChopAllDsAllGrAll,
    models.AggEtaPFU,
    models.SectorAggEtaFU,
    models.Phivecs,
    models.Etai,
]


def get_dataset_tables(dataset: models.Dataset) -> list[str]:
    """Return the user data tables which include data from the provided dataset."""

    def has_dataset(model: type[Model]) -> bool:
        return model.objects.filter(dataset=dataset.dataset_id).exists()

    return [str(table._meta.object_name) for table in USER_TABLES if has_dataset(table)]


def get_matrix_tables(matrix: models.Matname) -> list[str]:
    """Return the user data tables which include data from the provided matrix."""

    def has_matrix(model: type[Model]) -> bool:
        fields = model._meta.fields
        has_matrix_field = any(field.name == "matname" for field in fields)
        return (
            has_matrix_field
            and model.objects.filter(matname=matrix.matname_id).exists()
        )

    return [str(table._meta.object_name) for table in USER_TABLES if has_matrix(table)]


def get_dataset_mapping(
    datasets: Iterable[models.Dataset],
) -> dict[models.Dataset, list[str]]:
    mapping = {dataset: get_dataset_tables(dataset) for dataset in datasets}
    return mapping


def get_matrix_mapping(
    matrices: Iterable[models.Matname],
) -> dict[models.Matname, list[str]]:
    mapping = {matrix: get_matrix_tables(matrix) for matrix in matrices}
    return mapping


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
        model = (
            models.IEAData
            if table_name == "IEAEWEB2022"
            else models.PSUTReAllChopAllDsAllGrAll
        )

    source = "sandbox" if is_sandbox else "default"
    return source, model


def _valid_database(database_name: str):
    return database_name in settings.DATABASES.keys()


def query_database(target: DatabaseTarget, query: dict, values: list[str]):
    db = target[0]
    model = target[1]

    if not _valid_database(db):
        raise ValueError("Unknown database specified for query")

    LOGGER.info(f"Requested model: {model._meta.model_name}")
    LOGGER.info(f"Query being passed to filter: {query}")
    LOGGER.info(f"Requested columns: {values}")

    data = model.objects.using(db).values_list(*values).filter(**query)

    return data


def get_dataframe(
    target: DatabaseTarget, query: dict[str, Any], columns: list[str]
) -> pd.DataFrame:
    db_source, db_model = target
    if not _valid_database(db_source):
        # Invalid database, empty data frame.
        return pd.DataFrame()

    LOGGER.info(f"Requested model: {db_model._meta.model_name}")
    LOGGER.info(f"Query being passed to filter: {query}")
    LOGGER.info(f"Requested columns: {columns}")

    try:
        qs = list(
            db_model.objects.using(db_source)
            .filter(**query)
            .values(*columns)
            .order_by("year")
        )
        if len(qs) < 20:
            LOGGER.info(f"Raw results: {qs}")
        else:
            LOGGER.info(f"Got {len(qs)} rows")
        return pd.DataFrame.from_records(qs)
    except Exception as e:
        LOGGER.error(f"Query failed: {e}")
        LOGGER.error(f"Raw query dict: {query}")
        return pd.DataFrame()


# TODO: We need to "discover" these columns, not
# hardcode them.

PSUT_COLUMNS = ["value"]
AGGETA_COLUMNS = ["gross_net", "ex_p", "ex_f", "ex_u", "etapf", "etafu", "etapu"]
INCLUDES_NEU_COLUMN = "includes_neu"


def get_dataset_attributes(model: type[Model]) -> dict[str, Attribute]:
    """Get available attribute fields on the given
    dataset model."""

    def has_field(attr_field: str):
        return any(field.name == attr_field for field in model._meta.fields)

    # For all foreign fields, which ones does this model have?
    return {
        field: attr
        for attr in get_attributes().values()
        for field in attr.foreign_fields
        if has_field(field)
    }


def get_userfriendly_dataframe(
    target: DatabaseTarget, query: dict[str, Any], columns: list[str]
) -> pd.DataFrame:
    """Translate database IDs and other numerical values into
    named textual counterparts."""

    df = get_dataframe(target, query, columns)

    if df.empty:
        LOGGER.error("EMPTY: Empty dataframe")
        return df

    database = target[0]
    lookups = LookupManager(database)

    # Translate IDs into names when appropriate.
    for column in df.columns:
        # For accurate type hints:
        assert isinstance(column, str)
        col = column

        if not get_foreign_attribute(col):
            continue

        def transform(value):
            return lookups.translate(model_or_field=col, value=value)

        df[col] = df[col].apply(transform)

    # Handle IncludesNEU separately as it's a boolean.
    if INCLUDES_NEU_COLUMN in df.columns:
        df[INCLUDES_NEU_COLUMN] = df[INCLUDES_NEU_COLUMN].apply(
            lambda inc: "Yes" if inc else "No"
        )

    return df


def get_csv_from_query(target: DatabaseTarget, query: dict, columns: list[str]) -> str:
    INCLUDE_ROW_NUMS = False
    return get_userfriendly_dataframe(target, query, columns).to_csv(
        index=INCLUDE_ROW_NUMS
    )


def get_excel_from_query(
    target: DatabaseTarget, query: dict, columns: list[str]
) -> bytes:
    INCLUDE_ROW_NUMS = False
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        get_userfriendly_dataframe(target, query, columns).to_excel(
            writer, index=INCLUDE_ROW_NUMS
        )
    return buffer.getvalue()


def shape_post_request(
    params: QueryDict,
) -> tuple[ShapedQuery, str | None, DatabaseTarget]:
    """Turn a POST request payload into a ready to use query in a dictionary"""

    # Get rid of security token; it is not part of a query.
    SKIP_PARAMS = ("csrfmiddlewaretoken",)

    # Shaped query extracts items from lists.
    def shaped_value(key: str, value: list[str]) -> str | list[str] | None:
        if key in SKIP_PARAMS:
            return None
        if len(value) == 1:
            return value[0]
        if len(value) > 1:
            return value
        LOGGER.warning(f"Non-string POST param for key {key}")

    shaped_query = {
        key: value
        for key in params
        if (value := shaped_value(key, params.getlist(key))) is not None
    }
    LOGGER.info(f"Shaped post request {shaped_query}")
    plot_type = str(shaped_query.get("plot_type"))
    db_target = get_database_target(shaped_query)
    return shaped_query, plot_type, db_target


def _str_or_all_list[T](value: str | list[str], op: Callable[[str], T]) -> T | list[T]:
    if isinstance(value, str):
        return op(value)
    else:
        return [op(item) for item in value]


def translate_query(target: DatabaseTarget, query: ShapedQuery) -> dict[str, Any]:
    """Turn a query of human readable values from a form
    into a query ready to hit the dataset."""

    final_query: dict[str, Any] = dict()
    db_source, dataset_model = target

    if not _valid_database(db_source):
        raise ValueError("Unknown database specified for translating query")

    lookups = LookupManager(db_source)

    # Clear sandbox prefix from query parameters;
    # translation will not recognize sandbox prefix.
    query = {
        k: _str_or_all_list(query[k], lambda v: v.removeprefix(settings.SANDBOX_PREFIX))
        for k in query
    }

    SPECIAL_CASES: list[type[Model]] = [models.Version, models.Year]

    # Override RUVY for matname query.
    if "matname" in query and query["matname"] == "RUVY":
        query["matname"] = list("RUVY")

    # Translate names to IDs for lookup attributes.

    attributes = get_dataset_attributes(dataset_model)

    LOGGER.info(f"TRANSLATEQUERY: Attributes: {list(attributes.keys())}")

    for param, arg in query.items():
        attribute = attributes.get(param)
        if attribute is None:
            LOGGER.info(f"TRANSLATEQUERY: No attribute found for {param}")
            # Not an attribute; omit from query.
            continue
        if attribute.model in SPECIAL_CASES:
            continue
        lookup = lookups[attribute.model]
        LOGGER.info(f"TRANSLATEQUERY: Attribute found for {param}")

        if isinstance(arg, list):
            param = f"{param}__in"

        final_query[param] = _str_or_all_list(arg, lambda arg: lookup.translator[arg])

    # Special cases handled below.

    final_query["includes_neu"] = int(bool(query.get("includes_neu")))

    # Version range handling.
    if isinstance(v := query.get("version"), str):
        version = lookups[models.Version].translator[v]
        final_query["valid_from_version__lte"] = version
        final_query["valid_to_version__gte"] = version

    # Year range handling.
    if isinstance(v := query.get("to_year"), str):
        final_query["year__lte"] = int(v)
        if isinstance(v := query.get("year"), str):
            final_query["year__gte"] = int(v)
    elif isinstance(v := query.get("year"), str):
        final_query["year"] = int(v)

    LOGGER.debug(f"Translated query: {final_query}")
    return final_query
