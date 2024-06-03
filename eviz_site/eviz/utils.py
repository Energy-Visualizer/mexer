from time import time
from enum import Enum
from eviz.models import PSUT, Index, Dataset, Country, Method, EnergyType, LastStage, IEAMW, IncludesNEU, matname
from scipy.sparse import csr_matrix, csc_matrix

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

# TODO: Probably get rid of this
class RUVY(Enum):
    R = 1
    U = 2
    V = 6
    Y = 7

def get_matrix(
        dataset: str,
        country: str,
        method: str,
        energy_type: str,
        last_stage: str,
        ieamw: str,
        includes_neu: str,
        year: str,
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
            Dataset = Translator.dataset_translate(dataset),
            Country = Translator.country_translate(country),
            Method = Translator.method_translate(method),
            EnergyType = Translator.energytype_translate(energy_type),
            LastStage = Translator.laststage_translate(last_stage),
            IEAMW = Translator.ieamw_translate(ieamw),
            IncludesNEU = Translator.includesNEU_translate(includes_neu),
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

    # TODO: remove
    temp_add_get()

    # Make and return the sparse matrix
    return csr_matrix(
        (val, (row, col)),
        shape = (matrix_nrow, matrix_nrow),
    )

class Translator():

    __index_translations = None
    __country_translations = None
    __method_translations = None
    __energytype_translations = None
    __laststage_translations = None
    __IEAMW_translations = None
    __matname_translations = None
    __dataset_translations = None

    @staticmethod
    def index_translate(name: str)-> int:
        if Translator.__index_translations == None:
            indexes = Index.objects.values_list("IndexID", "Index")
            Translator.__index_translations = {name: id for id, name in indexes}
        
        return Translator.__index_translations[name]
    
    @staticmethod
    def dataset_translate(name: str)-> int:
        if Translator.__dataset_translations == None:
            datasets = Dataset.objects.values_list("DatasetID", "Dataset")
            Translator.__dataset_translations = {name: id for id, name in datasets}
        
        return Translator.__dataset_translations[name]
        
    @staticmethod
    def country_translate(name: str)-> int:
        if Translator.__country_translations == None:
            countries = Country.objects.values_list("CountryID", "Country")
            Translator.__country_translations = {name: id for id, name in countries}
        
        return Translator.__country_translations[name]
    
    @staticmethod
    def method_translate(name: str)-> int:
        if Translator.__method_translations == None:
            methods = Method.objects.values_list("MethodID", "Method")
            Translator.__method_translations = {name: id for id, name in methods}
        
        return Translator.__method_translations[name]
    
    @staticmethod
    def energytype_translate(name: str)-> int:
        if Translator.__energytype_translations == None:
            enerytpyes = EnergyType.objects.values_list("EnergyTypeID", "EnergyType")
            Translator.__energytype_translations = {name: id for id, name in enerytpyes}
        
        return Translator.__energytype_translations[name]
    
    @staticmethod
    def laststage_translate(name: str)-> int:
        if Translator.__laststage_translations == None:
            laststages = LastStage.objects.values_list("ECCStageID", "ECCStage")
            Translator.__laststage_translations = {name: id for id, name in laststages}
        
        return Translator.__laststage_translations[name]
    
    @staticmethod
    def ieamw_translate(name: str)-> int:
        if Translator.__IEAMW_translations == None:
            IEAMWs = IEAMW.objects.values_list("IEAMWID", "IEAMW")
            Translator.__IEAMW_translations = {name: id for id, name in IEAMWs}
        
        return Translator.__IEAMW_translations[name]
    
    @staticmethod
    def includesNEU_translate(name: bool)-> int:
        return int(name)
    
    @staticmethod
    def matname_translate(name: str)-> int:
        if Translator.__matname_translations == None:
            matnames = matname.objects.values_list("matnameID", "matname")
            Translator.__matname_translations = {name: id for id, name in matnames}
        
        return Translator.__matname_translations[name]
        

# TODO: scrap this?
class RUVY_Matrix(csr_matrix):

    def __getitem__(self, key):
        ''' Gets an item from a RUVY matrix
        
        Use is matrix["row_name", "col_name"] or matrix[row_number, col_number]

        Inputs:
            key, tuple: a 2-tuple denoting the desired row name or number followed by the column name or number

        Outputs:
            the value at that key in the cooresponding RUVY matrix
        '''
        
        if type(key) != tuple[str | int] or len(key) != 2:
            raise ValueError("Getting item from RUVY matrix must be as follows: matrix['row_name', 'column_name'] or matrix[row_number, col_number]")

        # if key is strings, translate it first
        if type(key[0]) == str:
            return super()[Translator.index_translate(key[0]), Translator.index_translate(key[1])]
        
        # if key is an integer, run as normal
        return super()[key[0], key[1]]
    
def temp_add_get():

    def mat_get(self, row, col):
            if type(row) != str or type(col) != str:
                raise ValueError("Getting item from RUVY matrix must be as follows: matrix['row_name', 'column_name'] or matrix[row_number, col_number]")

            if type(self) == csc_matrix:
                return self[Translator.index_translate(col), Translator.index_translate(row)]
            return self[Translator.index_translate(row), Translator.index_translate(col)]
    
    if not hasattr(csr_matrix, "get"): csr_matrix.get = mat_get
    
    if not hasattr(csc_matrix, "get"): csc_matrix.get = mat_get
