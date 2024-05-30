from time import time
from enum import Enum
from eviz.models import PSUT, Index
from scipy.sparse import csr_matrix

def time_view(v):
    '''
    Wrapper to time how long it takes to deliver a view

    Results are printed to stdout
    '''

    def wrap(*args, **kwargs):
        t0 = time()
        ret = v(*args, **kwargs)
        t1 = time()
        print(f"Time to run {v.__name__}: {t1 - t0}")
        return ret

    return wrap

class RUVY(Enum):
    R = 1
    U = 2
    V = 6
    Y = 7

def get_matrix(
        dataset,
        country,
        method,
        energy_type,
        last_stage,
        ieamw,
        includes_neu,
        year,
        matrix_name,
    ):
    '''Collects, constructs, and returns one of the RUVY matrices'''

    # Get the sparse matrix representation
    # i, j, x for row, column, value
    # in 3-tuples
    sparse_matrix = (
        PSUT.objects
        .values_list("i", "j", "x")
        .filter(
            Dataset = dataset,
            Country = country,
            Method = method,
            EnergyType = energy_type,
            LastStage = last_stage,
            IEAMW = ieamw,
            IncludesNEU = includes_neu,
            Year = year,
            matname = matrix_name.value
        )
    )

    # Get dimensions for a matrix (rows and columns will be the same)
    matrix_side_length = Index.objects.all().count() # len() would evaluate the query set, so use count() instead for better performance

    # For each 3-tuple in sparse_matrix
    # Put together all the first values, all the second, etc.
    # All first values across the tupes are rows, second are columns, etc.
    row, col, val = zip(*sparse_matrix)

    # Make and return the sparse matrix
    return csr_matrix(
        (val, (row, col)),
        shape = (matrix_side_length, matrix_side_length),
    )