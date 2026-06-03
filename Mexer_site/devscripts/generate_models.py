import re
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from typing import Literal

import pandas as pd

type SpreadsheetDataType = Literal[
    "int",
    "text",
    "boolean",
    "double precision",
]


@dataclass
class Column:
    pk: bool
    data_type: SpreadsheetDataType
    fk_table: str | float  # Can be NaN.
    fk_column: str | float  # Can be NaN.


def generate_models(
    *, src: str, dest: str, base_models: str, output: Callable[[str], None]
):
    with open(base_models, "r") as file:
        base_code = file.read()

    schema = pd.read_excel(src, sheet_name="Schema")

    tables: defaultdict[str, dict[str, Column]] = defaultdict(dict)

    for row in schema.itertuples():
        (_, table, col_name, is_pk, col_data_type, fk_table, fk_column) = row

        tables[table][col_name] = Column(
            pk=is_pk,
            data_type=col_data_type,
            fk_table=fk_table,
            fk_column=fk_column,
        )

    code = (
        base_code
        + "\n"
        + "\n\n\n".join(
            _format_model(table, columns) for table, columns in tables.items()
        )
    )

    with open(dest, "w") as file:
        file.write(code)

    output(f"Done creating {len(tables)} models at {dest}")


def table_class_name(name: str) -> str:
    return name[:1].upper() + name[1:]


def column_field_name(name: str) -> str:
    s = re.sub(r"([A-Z]+)([A-Z][a-z]{2,})", r"\1_\2", name)
    s = re.sub(r"([A-Z]{2,})([a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()


def _django_field_type(dt: SpreadsheetDataType) -> str:
    match dt:
        case "int":
            return "IntegerField"
        case "boolean":
            return "BooleanField"
        case "double precision":
            return "FloatField"
        case "text":
            return "TextField"


def _format_column(column_name: str, column: Column) -> str:
    # TODO: docs for columns?
    field_name = column_field_name(column_name)
    args = {"db_column": f'"{column_name}"'}

    # Current models.py ignores foreign-key columns
    # if isinstance(column.fk_column, str) and isinstance(column.fk_table, str):
    #     field_type = "ForeignKey"
    #     args["to"] = _table_class_name(column.fk_table)
    #     args["on_delete"] = "models.DO_NOTHING"
    # else:

    field_type = _django_field_type(column.data_type)
    if column.pk:
        args["primary_key"] = "True"
    args_list = ", ".join(f"{param}={value}" for param, value in args.items())

    return f"{field_name} = models.{field_type}({args_list})"


def _format_model(table_name: str, columns: dict[str, Column]) -> str:
    class_name = table_class_name(table_name)
    # TODO, once table-of-tables added, derive docstring.
    docs = f"Model for the '{table_name}' database table."

    return f"""class {class_name}(models.Model):
    \"\"\"{docs}\"\"\"

    class Meta:
        db_table = "{table_name}"
        managed = False

    {"\n    ".join(_format_column(name, data) for name, data in columns.items())}"""


if __name__ == "__main__":
    SRC = "./Mexer_site/internal_resources/SchemaAndFKTables.xlsx"
    DEST = "./Mexer_site/Mexer/models.py"
    BASE_MODELS = "./Mexer_site/internal_resources/base_models.py"
    generate_models(src=SRC, dest=DEST, base_models=BASE_MODELS, output=print)
