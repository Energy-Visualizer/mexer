import plotly.graph_objects as pgo
from scipy.sparse import coo_matrix
from utils.data import query_database, DatabaseTarget
from eviz.models import PSUT, Index
from utils.translator import Translator

def get_matrix(target: DatabaseTarget, query: dict) -> coo_matrix:
    '''Collects, constructs, and returns one of the RUVY matrices

    Inputs:
        a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Outputs:
        A scipy coo_matrix containing all the values from the specified query
        or None if the given query related to no data 
    '''

    # Get the sparse matrix representation
    # i, j, x for row, column, value
    # in 3-tuples
    sparse_matrix = query_database(target, query, ["i", "j", "value"])

    # if nothing was returned
    if not sparse_matrix:
        return None

    # Get dimensions for a matrix (rows and columns will be the same)
    # len() would evaluate the query set, so use count() instead for better performance
    matrix_nrow = Index.objects.all().count()

    # For each 3-tuple in sparse_matrix
    # Put together all the first values, all the second, etc.
    # All first values across the tupes are rows, second are columns, etc.
    row, col, val = zip(*sparse_matrix)

    # Make and return the sparse matrix
    return coo_matrix(
        (val, (row, col)),
        shape=(matrix_nrow, matrix_nrow),
    )


def visualize_matrix(target: DatabaseTarget, mat: coo_matrix, color_scale: str = 'viridis') -> pgo.Figure:
    """Visualize a sparse matrix as a heatmap using Plotly.

    Inputs:
        mat (coo_matrix): A scipy sparse matrix in COOrdinate format.
        color_scale (str, optional): The color scale to use for the heatmap. Defaults to 'viridis'.

    Outputs:
        pgo.Figure: A Plotly graph object Figure containing the heatmap.
    """

    # Convert the matrix to a format suitable for Plotly's heatmap
    rows, cols, vals = mat.row, mat.col, mat.data

    translator = Translator(target[0])
    # Translate row and column indices to human-readable labels
    row_labels = [translator.index_translate(i) for i in rows]
    col_labels = [translator.index_translate(i) for i in cols]
    
    # Create a Plotly Heatmap object
    heatmap = pgo.Heatmap(
        z=vals,
        x=col_labels,
        y=row_labels,
        text=vals,
        texttemplate="%{text:.2f}",
        showscale=False,
        colorscale=color_scale,
    )

    # convert to a more general figure
    return pgo.Figure(data=heatmap)