####################################################################
# matrix.py includes all the functions related to matrices
#
# The functions can get a matrix, get special Mexer matix (RUVY)
# and turn those matrices into HTML to display
#
# The matrices are represented by scipy's sparse coo_matrix
#
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu
#####################
from typing import Any

import altair as alt
import pandas as pd
from Mexer import models
from scipy.sparse import coo_matrix

from utils.data import DatabaseTarget, query_database
from utils.lookup import LookupManager

alt.data_transformers.enable("default")


def get_matrix(target: DatabaseTarget, query: dict[str, Any]) -> coo_matrix:
    """Collects, constructs, and returns one of the RUVY matrices

    Inputs:
        a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Outputs:
        A scipy coo_matrix containing all the values from the specified query
        or None if the given query related to no data
    """

    # Get the sparse matrix representation
    # i, j, x for row, column, value
    # in 3-tuples
    sparse_matrix = query_database(target, query, ["i", "j", "value"])

    # if nothing was returned
    if not sparse_matrix:
        return coo_matrix([])  # empty matrix

    # Get dimensions for a matrix (rows and columns will be the same)
    # len() would evaluate the query set, so use count() instead for better performance
    matrix_nrow = models.Index.objects.all().count()

    # For each 3-tuple in sparse_matrix
    # Put together all the first values, all the second, etc.
    # All first values across the tupes are rows, second are columns, etc.
    row, col, val = zip(*sparse_matrix)

    # Make and return the sparse matrix
    return coo_matrix(
        (val, (row, col)),
        shape=(matrix_nrow, matrix_nrow),
    )


def get_ruvy_matrix(
    target: DatabaseTarget,
    query: dict[str, Any],
) -> tuple[coo_matrix, tuple[int, ...]] | None:
    sparse_matrix = query_database(target, query, ["i", "j", "value", "matname"])
    if not sparse_matrix:
        return None
    matrix_nrow = models.Index.objects.all().count()
    row, col, val, matname = zip(*sparse_matrix)
    mat = coo_matrix(
        (val, (row, col)),
        shape=(matrix_nrow, matrix_nrow),
    )

    return mat, matname


def visualize_matrix(
    target: DatabaseTarget,
    mat: coo_matrix,
    matnames: tuple[int, ...] | None = None,
    color_scale: str = "inferno",
    coloring_method: str = "weight",
) -> alt.Chart:
    """Visualize a sparse matrix as a heatmap using Plotly.

    Inputs:
        mat (coo_matrix): A scipy sparse matrix in COOrdinate format.
        color_scale (str, optional): The color scale to use for the heatmap. Defaults to 'viridis'.

    Outputs:
        alt.Chart A chart containing the heatmap.
    """

    lookups = LookupManager(target[0])
    index_lookup = lookups[models.Index]
    matname_lookup = lookups[models.Matname]

    # Create a dictionary mapping index IDs to their orders.
    index_orders: dict[int, int] = {
        index.index_id: index.order for index in index_lookup.objects
    }

    # columns to be used in dataframe
    # frame_columns = {
    df = pd.DataFrame(
        {
            "x": [index_lookup.translator[int(col)] for col in mat.col],
            "y": [index_lookup.translator[int(row)] for row in mat.row],
            "value": mat.data,
            "x_order": [index_orders[int(col)] for col in mat.col],
            "y_order": [index_orders[int(row)] for row in mat.row],
        }
    )

    # Create a Plotly Heatmap object
    if coloring_method == "ruvy" and matnames:
        df = df.assign(matname=[matname_lookup.translator[m] for m in matnames])

        tooltip = [
            alt.Tooltip("y", title="From"),
            alt.Tooltip("x", title="To"),
            alt.Tooltip("value"),
            alt.Tooltip("matname"),
        ]
        colors = "matname:N"
    else:
        tooltip = [
            alt.Tooltip("y", title="From"),
            alt.Tooltip("x", title="To"),
            alt.Tooltip("value"),
        ]
        colors = "value:Q"

    # aggregate on x and y columns
    agg_functions = {"value": "sum"}

    # take care of all other columns. Not pretty, but ignores columns specified
    # in agg_functions and the x, y on which we are already aggregating
    # importantly, matname column should not be clobbered
    # as there should not be unique (x,y) pairs across matrices
    # but *still needs to be listed*, or else pandas will drop it
    agg_functions.update(
        {
            col: "first"
            for col in df.columns
            if col not in agg_functions and col not in ["x", "y"]
        }
    )

    df = df.groupby(["x", "y"]).aggregate(agg_functions).reset_index()

    heatmap = (
        alt.Chart(df)
        .mark_rect(stroke="blue", strokeWidth=1)
        .encode(
            x=alt.X(
                "x",
                axis=alt.Axis(orient="top", labelAngle=-45, title=""),
                sort=alt.EncodingSortField(field="x_order", order="ascending"),
            ),
            y=alt.Y(
                "y",
                axis=alt.Axis(title=""),
                sort=alt.EncodingSortField(field="y_order", order="ascending"),
            ),
            color=alt.Color(colors, scale=alt.Scale(scheme=color_scale)),
            tooltip=tooltip,
        )
    )
    return heatmap
