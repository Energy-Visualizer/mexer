from time import time
from enum import Enum
from eviz.models import PSUT, Index
from scipy.sparse import csr_matrix

def time_view(v):
    '''Wrapper to time how long it takes to deliver a view

    Inputs:
        v, function: the view to time
    
    Outputs:
        A function which will also print how long the given view took to run to stdout
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
        dataset: int,
        country: int,
        method: int,
        energy_type: int,
        last_stage: int,
        ieamw: int,
        includes_neu: int,
        year: int,
        matrix_name,
    ) -> csr_matrix:
    '''Collects, constructs, and returns one of the RUVY matrices
    
    Inputs:
        dataset, country, method, energy_type, last_stage, ieamw, inclues_neu, year:
        ints to specify metadata for which matrix to get

        matrix_name, RUVY enum name: specify which matrix to get

    Outputs:
        A scipy csr_matrix containing all the values from the specified query
    '''

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
    matrix_nrow = Index.objects.all().count() # len() would evaluate the query set, so use count() instead for better performance

    # For each 3-tuple in sparse_matrix
    # Put together all the first values, all the second, etc.
    # All first values across the tupes are rows, second are columns, etc.
    row, col, val = zip(*sparse_matrix)

    # Make and return the sparse matrix
    return csr_matrix(
        (val, (row, col)),
        shape = (matrix_nrow, matrix_nrow),
    )

class IndexTranslator():

    index_translations = None

    @staticmethod
    def translate(mat, row, col):
        if IndexTranslator.index_translations == None:
            indexes = Index.objects.values_list("IndexID", "Index")
            IndexTranslator.index_translations = {name: id for id, name in indexes}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return mat[IndexTranslator.index_translations[col], IndexTranslator.index_translations[row]]
        


# TODO: scrap this idea?
class RUVY_Matrix(csr_matrix):

    index_translations = None

    def __init__(self, data, shape):
        if self.index_translations == None:
            indexes = Index.objects.values_list("IndexID", "Index")
            self.index_translations = {name: id for id, name in indexes}
        super().__init__(data, shape)
    
    def __getitem__(self, key):

        print(key)

        # if key is a string, translate it first
        if type(key) == str:
            return super().__getitem__(self.index_translations[key])
        
        # if key is an integer, run as normal
        return super().__getitem__(key)
