from time import time
from enum import Enum
from eviz.models import PSUT, Index, Dataset, Country, Method, EnergyType, LastStage, IEAMW, IncludesNEU, matname, AggLevel
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
        dataset: str,
        country: str,
        method: str,
        energy_type: str,
        last_stage: str,
        ieamw: str,
        includes_neu: str,
        year: str,
        choppedmat: str,
        choppedvar: str,
        productaggregation: str,
        industryaggregation: str,
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
            Dataset = Translator.index_translate(dataset),
            Country = Translator.country_translate(country),
            Method = Translator.method_translate(method),
            EnergyType = Translator.energytype_translate(energy_type),
            LastStage = Translator.laststage_translate(last_stage),
            IEAMW = Translator.ieamw_translate(ieamw),
            IncludesNEU = Translator.includesNEU_translate(includes_neu),
            Year = year,
            ChoppedMat = Translator.matname_translate(choppedmat),
            ChoppedVar = Translator.index_translate(choppedvar),
            ProductAggregation = Translator.productaggregation_translate(productaggregation),
            IndustryAggregation = Translator.productaggregation_translate(industryaggregation),
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

class Translator():

    __index_translations = None
    __country_translations = None
    __method_translations = None
    __energytype_translations = None
    __laststage_translations = None
    __IEAMW_translations = None
    __matname_translations = None
    __dataset_translations = None
    __productaggregation_translations = None
    @staticmethod
    def index_translate(name: str)-> int:
        if Translator.__index_translations == None:
            indexes = Index.objects.filter("IndexID", "Index").values_list()
            Translator.__index_translations = {name: id for id, name in indexes}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__index_translations[name]
    
    @staticmethod
    def dataset_translate(name: str)-> int:
        if Translator.__dataset_translations == None:
            datasets = Dataset.objects.filter("DatasetID", "Dataset").values_list()
            Translator.__dataset_translations = {name: id for id, name in datasets}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__dataset_translations[name]
        
    @staticmethod
    def country_translate(name: str)-> int:
        if Translator.__country_translations == None:
            countries = Country.objects.filter("CountryID", "Country").values_list()
            Translator.__country_translations = {name: id for id, name in countries}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__country_translations[name]
    
    @staticmethod
    def method_translate(name: str)-> int:
        if Translator.__method_translations == None:
            methods = Method.objects.filter("MethodID", "Method").values_list()
            Translator.__method_translations = {name: id for id, name in methods}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__method_translations[name]
    
    @staticmethod
    def energytype_translate(name: str)-> int:
        if Translator.__energytype_translations == None:
            enerytpyes = EnergyType.objects.filter("EnergyTypeID", "EnergyType").values_list()
            Translator.__energytype_translations = {name: id for id, name in enerytpyes}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__energytype_translations[name]
    @staticmethod
    def laststage_translate(name: str)-> int:
        if Translator.__laststage_translations == None:
            laststages = LastStage.objects.filter("ECCStageID", "ECCStage").values_list()
            Translator.__laststage_translations = {name: id for id, name in laststages}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__laststage_translations[name]
    @staticmethod
    def ieamw_translate(name: str)-> int:
        if Translator.__IEAMW_translations == None:
            IEAMWs = IEAMW.objects.filter("IEAMWID", "IEAMW").values_list()
            Translator.__IEAMW_translations = {name: id for id, name in IEAMWs}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__IEAMW_translations[name]
    @staticmethod
    def includesNEU_translate(name: bool)-> int:
        return int(name)
    
        
    @staticmethod
    def productaggregation_translate(name: str)-> int:
        if Translator.__productaggregation_translations == None:
            productaggregations = matname.objects.filter("ProductAggregationID", "ProductAggregation").values_list("ProductAggregationID", "ProductAggregation")
            Translator.__productaggregation_translations = {name: id for id, name in productaggregations}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__productaggregation_translations[name]
    
    
    @staticmethod
    def matname_translate(name: str)-> int:
        if Translator.__matname_translations == None:
            matnames = matname.objects.filter("matnameID", "matname").values_list("matnameID", "matname")
            Translator.__matname_translations = {name: id for id, name in matnames}
        
        # TODO: this is backwards with col, row... figure out why this is happening
        return Translator.__matname_translations[name]
        


# TODO: scrap this idea?
# class RUVY_Matrix(csr_matrix):

#     index_translations = None

#     def __init__(self, data, shape):
#         if self.index_translations == None:
#             indexes = Index.objects.values_list("IndexID", "Index")
#             self.index_translations = {name: id for id, name in indexes}
#         super().__init__(data, shape)
    
#     def __getitem__(self, key):

#         print(key)

#         # if key is a string, translate it first
#         if type(key) == str:
#             return super().__getitem__(self.index_translations[key])
        
#         # if key is an integer, run as normal
#         return super().__getitem__(key)
