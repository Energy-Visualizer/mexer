from time import time
from eviz.models import PSUT, Index, Dataset, Country, Method, EnergyType, LastStage, IEAMW, matname, AggLevel
from scipy.sparse import csr_matrix, csc_matrix
import plotly.graph_objects as pgo

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

def translate_query(
        query: dict
    ) -> dict:
    '''Turn a query of human readable values from a form into a query read to hit the dataset
    
    Input:

        query, a dict: the query that should be translated
    
    Output:

        a dictionary of a query ready to hit the database
    '''

    translated_query = dict() # set up to build and return at the end

    # common query parts

    if v := query.get("dataset"):
        translated_query["Dataset"] = Translator.dataset_translate(v)
    if v := query.get("country"):
        translated_query["Country"] = Translator.country_translate(v)
    if v := query.get("method"):
        translated_query["Method"] = Translator.method_translate(v)
    if v := query.get("energy_type"):
        translated_query["EnergyType"] = Translator.energytype_translate(v)
    if v := query.get("last_stage"):
        translated_query["LastStage"] = Translator.laststage_translate(v)
    if v := query.get("ieamw"):
        translated_query["IEAMW"] = Translator.ieamw_translate(v)
    if v := query.get("includes_neu"):
        translated_query["IncludesNEU"] = Translator.includesNEU_translate(v)
    if v := query.get("chopped_mat"):
        translated_query["ChoppedMat"] = Translator.matname_translate(v)
    if v := query.get("chopped_var"):
        translated_query["ChoppedVar"] = Translator.index_translate(v)
    if v := query.get("product_aggregation"):
        translated_query["ProductAggregation"] = Translator.agglevel_translate(v)
    if v := query.get("industry_aggregation"):
        translated_query["IndustryAggregation"] = Translator.agglevel_translate(v)

    # plot-specific query parts

    if v := query.get("to_year"):
        # if year part is a range of years, i.e. to_year present
        # set up query as range
        translated_query["Year__lte"] = v
        if v := query.get("year"):
            translated_query["Year__gte"] = v

    elif v := query.get("year"):
        # else just have year be one year
        translated_query["Year"] = v
    
    if v := query.get("matname"):
        translated_query["matname"] = Translator.matname_translate(v)

    return translated_query



def get_matrix(
        query: dict
    ) -> csr_matrix:
    '''Collects, constructs, and returns one of the RUVY matrices
    
    Inputs:
        dataset, country, method, energy_type, last_stage, ieamw, matrix_name:
        strings of their database names to specify metadata for which matrix to get
        all use abbreviations, except for country, which uses the FullName

        inclues_neu, bool: metadata for which matrix

        year, int: metadata for which matrix

    Outputs:
        A scipy csr_matrix containing all the values from the specified query
        or None if the given query related to no data 
    '''

    # set up the query
    # a dictionary that will have all the keyword arguments for the filter function below
    query = translate_query(query)

    # Get the sparse matrix representation
    # i, j, x for row, column, value
    # in 3-tuples
    sparse_matrix = (
        PSUT.objects
        .values_list("i", "j", "x")
        .filter(**query)
    )
    
    # if nothing was returned
    if not sparse_matrix:
        return None

    # Get dimensions for a matrix (rows and columns will be the same)
    matrix_nrow = Index.objects.all().count() # len() would evaluate the query set, so use count() instead for better performance

    # For each 3-tuple in sparse_matrix
    # Put together all the first values, all the second, etc.
    # All first values across the tupes are rows, second are columns, etc.
    row, col, val = zip(*sparse_matrix)

    # TODO: move this to a better place
    temp_add_get()

    # Make and return the sparse matrix
    return csr_matrix(
        (val, (row, col)),
        shape = (matrix_nrow, matrix_nrow),
    )

def shape_post_request(
        payload
    ) -> tuple[str, dict]:
    '''Turn a POST request payload into a ready to use query in a dictionary

    Input:

        payload, some dict-like (used with Django HttpRequest POST attributes): 
        the POST payload to shape into a query dictionary

    Output:

        2-tuple containing in top-down order

            a string telling the plot type requested

            a dictionary containing all the associations of a query parts and their values
    '''

    shaped_query = dict(payload)
    plot_type = shaped_query.pop("plot_type")[0] # to be returned at the end

    del shaped_query["csrfmiddlewaretoken"] # get rid of security token, is not part of a query

    for k, v in shaped_query.items():

        # convert from list (if just one item in list)
        if len(v) == 1: shaped_query[k] = v[0]

        # if empty choice, get rid of it for the query
        if shaped_query[k] == '': shaped_query[k] = None

    # special typed metadata
    # TODO: perhaps move to translate_query() ??
    if shaped_query.get("includes_neu") != None:
        shaped_query["includes_neu"] = bool(shaped_query["includes_neu"])
    if shaped_query.get("year") != None:
        # year is both single year and from year
        shaped_query["year"] = int(shaped_query["year"])
    if shaped_query.get("to_year") != None:
        shaped_query["to_year"] = int(shaped_query["to_year"])

    return (plot_type, shaped_query)

from django.contrib.auth.models import User
def iea_valid(user: User, query: dict) -> bool:
    '''Ensure that a give user's query does not give out IEA data if not authorized
    
    Inputs:

        user, user info from the HTTP request (for Django requsests: request.user): the user whose authorizations need to be checked

        query, a dict: the query to investigate

    Output:

        the boolean value of if a user's query is valid (True) or not (False)
    '''

    # will short curcuit if the data is free,
    # so everything past the or will not be checked if not neccessary
    return (
        # free data
        (query.get("dataset", None) != "IEAEWEB2022" and query.get("ieamw", None) == "MW")
        or
        # authorized to get proprietary data
        (user.is_authenticated and user.has_perm("eviz.get_iea"))
    )

from json import loads as json_from_string
with open("internal_resources/sankey_color_scheme.json") as f: colors_data = f.read()
SANKEY_COLORS: dict[str, str] = json_from_string(colors_data)
def get_sankey(query: dict) -> pgo.Figure:
    '''Gets a sankey diagram for a query
    
    Input:

        query, dict: a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Output:

        a plotly Figure with the sankey data

        or None if there is no cooresponding data for the query
    '''
    
    # we do a little shaping
    if "matname" in query.keys(): del query["matname"]

    # get all four matrices to make the full RUVY matrix
    data = PSUT.objects.values_list("i", "j", "x").filter(**query, matname__in = [Translator.matname_translate("R"),Translator.matname_translate("U"),Translator.matname_translate("V"),Translator.matname_translate("Y")])

    # if no cooresponding data, return as such
    if not data: return None

    # get rid of any duplicate i,j,x combinations (many exist)
    data = set(data)

    # begin constructing the sankey
    label_to_index = dict() # used to know which human-readable label is where in the label list
    next_index = 0 # used to keep track of where a new label is added in the label list

    labels = list() # used to keep track of all the labels
    sources = list() # used to keep track of all the sources (from-nodes)
    targets = list() # used to keep track of all the targets (to-nodes)
    magnitudes = list() # used to keep track of all the magnitudes between the nodes

    node_colors = list()
    flow_colors = list()

    for row, col, magnitude in data:
        translated_row = Translator.index_reverse_translate(row)
        translated_col = Translator.index_reverse_translate(col)

        flow_color = "rgba(100,100,100,0.5)" # default flow color

        # Get the row (source) label's index and make the start of a connection
        idx = label_to_index.get(translated_row, -1)
        if idx == -1: # label is new
            labels.append(translated_row)
            label_to_index[translated_row] = idx = next_index
            next_index += 1

            # get the associated color for the source, if there is one and apply it
            # if not, the color is wheat
            node_colors.append(SANKEY_COLORS.get(translated_col, "wheat"))

        sources.append(idx)

        # Get the col (target) label's index and make the end of a connection
        idx = label_to_index.get(translated_col, -1)
        if idx == -1: # label is new
            labels.append(translated_col)
            label_to_index[translated_col] = idx = next_index
            next_index += 1

            # same as above
            node_colors.append(SANKEY_COLORS.get(translated_col, "wheat"))

        targets.append(idx)

        # make in-flow special color if node has special color
        #     i.e. if current target node has color besides default node color
        # only on targets (columns) because only targets can have in-flows
        if((assoc_color := node_colors[idx]) != "wheat"): flow_color = assoc_color

        # Finish the connection with the magnitude of the connection
        magnitudes.append(magnitude)

        flow_colors.append(flow_color)

    return pgo.Figure(data=[pgo.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        label = labels,
        color = node_colors
        ),
        link = dict(
        source = sources,
        target = targets,
        value = magnitudes,
        color = flow_colors
    ))])

from eviz.models import AggEtaPFU
import pandas.io.sql as pd_sql # for getting data into a pandas dataframe
import plotly.express as px # for making the scatter plot
from django.db import connection # for low-level psycopg2 connection. to access other db connections, import connections
def get_xy(efficiency_metric, query: dict) -> pgo.Figure:
    '''Gets an xy plot for a query
    
    Inputs:
        
        efficiency_metric, string: the efficiency matrix to get the plot for

        query, dict: a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Output:

        a plotly Figure with the xy data
    '''
    
    agg_query = AggEtaPFU.objects.filter(**query).values("Year", efficiency_metric).query

    with Silent():
        df = pd_sql.read_sql_query(str(agg_query), con=connection.cursor().connection)

    return px.line(
        df, x="Year", y=efficiency_metric,
        title=f"Efficiency of {efficiency_metric} by year",
        template="plotly_dark"
    )

class Translator():
    '''Contains the tools for translating PSUT metadata

    Translations go from human readable name -> integer representation in the PSUT table

    Reverse translations go from integer representation -> human readable name
    '''

    __index_translations = None
    __index_reverse_translations = None
    __country_translations = None
    __method_translations = None
    __energytype_translations = None
    __laststage_translations = None
    __IEAMW_translations = None
    __matname_translations = None
    __dataset_translations = None
    __productaggregation_translations = None

    @staticmethod
    def index_translate(name: str) -> int:
        if Translator.__index_translations == None:
            indexes = Index.objects.values_list("IndexID", "Index")
            # get both regular and reverse to limit queries
            Translator.__index_translations = {name: id for id, name in indexes}
            Translator.__index_reverse_translations = {id: name for id, name in indexes}
        
        return Translator.__index_translations[name]
    
    @staticmethod
    def index_reverse_translate(number: int) -> str:
        if Translator.__index_reverse_translations == None:
            indexes = Index.objects.values_list("IndexID", "Index")
            # get both regular and reverse to limit queries
            Translator.__index_translations = {name: id for id, name in indexes}
            Translator.__index_reverse_translations = {id: name for id, name in indexes}
        
        return Translator.__index_reverse_translations[number]
    
    @staticmethod
    def dataset_translate(name: str)-> int:
        if Translator.__dataset_translations == None:
            datasets = Dataset.objects.values_list("DatasetID", "Dataset")
            Translator.__dataset_translations = {name: id for id, name in datasets}
        
        return Translator.__dataset_translations[name]
    

    @staticmethod
    def get_datasets() -> list[str]:
        if Translator.__dataset_translations == None:
            datasets = Dataset.objects.values_list("DatasetID", "Dataset")
            Translator.__dataset_translations = {name: id for id, name in datasets}
        
        return Translator.__dataset_translations.keys()
        
    @staticmethod
    def country_translate(name: str)-> int:
        if Translator.__country_translations == None:
            countries = Country.objects.values_list("CountryID", "FullName")
            Translator.__country_translations = {name: id for id, name in countries}
        
        return Translator.__country_translations[name]
    

    @staticmethod
    def get_countries() -> list[str]:
        if Translator.__country_translations == None:
            countries = Country.objects.values_list("CountryID", "FullName")
            Translator.__country_translations = {name: id for id, name in countries}
        
        return Translator.__country_translations.keys()
    
    @staticmethod
    def method_translate(name: str)-> int:
        if Translator.__method_translations == None:
            methods = Method.objects.values_list("MethodID", "Method")
            Translator.__method_translations = {name: id for id, name in methods}
        
        return Translator.__method_translations[name]
    

    @staticmethod
    def get_methods() -> list[str]:
        if Translator.__method_translations == None:
            methods = Method.objects.values_list("MethodID", "Method")
            Translator.__method_translations = {name: id for id, name in methods}
        
        return Translator.__method_translations.keys()
    
    @staticmethod
    def energytype_translate(name: str)-> int:
        if Translator.__energytype_translations == None:
            enerytpyes = EnergyType.objects.values_list("EnergyTypeID", "EnergyType")
            Translator.__energytype_translations = {name: id for id, name in enerytpyes}
        
        return Translator.__energytype_translations[name]
    

    @staticmethod
    def get_energytypes() -> list[str]:
        if Translator.__energytype_translations == None:
            enerytpyes = EnergyType.objects.values_list("EnergyTypeID", "EnergyType")
            Translator.__energytype_translations = {name: id for id, name in enerytpyes}
        
        return Translator.__energytype_translations.keys()
    
    @staticmethod
    def laststage_translate(name: str)-> int:
        if Translator.__laststage_translations == None:
            laststages = LastStage.objects.values_list("ECCStageID", "ECCStage")
            Translator.__laststage_translations = {name: id for id, name in laststages}
        
        return Translator.__laststage_translations[name]
    

    @staticmethod
    def get_laststages() -> list[str]:
        if Translator.__laststage_translations == None:
            laststages = LastStage.objects.values_list("ECCStageID", "ECCStage")
            Translator.__laststage_translations = {name: id for id, name in laststages}
        
        return Translator.__laststage_translations.keys()
    
    @staticmethod
    def ieamw_translate(name: str)-> int:
        if Translator.__IEAMW_translations == None:
            IEAMWs = IEAMW.objects.values_list("IEAMWID", "IEAMW")
            Translator.__IEAMW_translations = {name: id for id, name in IEAMWs}
        
        return Translator.__IEAMW_translations[name]
    

    @staticmethod
    def get_ieamws() -> list[str]:
        if Translator.__IEAMW_translations == None:
            IEAMWs = IEAMW.objects.values_list("IEAMWID", "IEAMW")
            Translator.__IEAMW_translations = {name: id for id, name in IEAMWs}
        
        return Translator.__IEAMW_translations.keys()
    
    @staticmethod
    def includesNEU_translate(name: bool)-> int:
        return int(name)
    
    @staticmethod
    def get_includesNEUs() -> list[str]:
        return ["True", "False"]
    
    @staticmethod
    def agglevel_translate(name: str)-> int:
        if Translator.__productaggregation_translations == None:
            productaggregations = AggLevel.objects.values_list("AggLevelID", "AggLevel")
            Translator.__productaggregation_translations = {name: id for id, name in productaggregations}
        
        return Translator.__productaggregation_translations[name]

    @staticmethod
    def get_agglevels() -> list[str]:
        if Translator.__productaggregation_translations == None:
            productaggregations = AggLevel.objects.values_list("AggLevelID", "AggLevel")
            Translator.__productaggregation_translations = {name: id for id, name in productaggregations}
        
        return Translator.__productaggregation_translations.keys()
    
    
    @staticmethod
    def matname_translate(name: str)-> int:
        if Translator.__matname_translations == None:
            matnames = matname.objects.values_list("matnameID", "matname")
            Translator.__matname_translations = {name: id for id, name in matnames}
        
        return Translator.__matname_translations[name]
    
    @staticmethod
    def get_matnames() -> list[str]:
        if Translator.__matname_translations == None:
            matnames = matname.objects.values_list("matnameID", "matname")
            Translator.__matname_translations = {name: id for id, name in matnames}
        
        return Translator.__matname_translations.keys()
    
def temp_add_get():

    def mat_get(self, row, col):
            if type(row) != str or type(col) != str:
                raise ValueError("Getting item from RUVY matrix must be as follows: matrix['row_name', 'column_name'] or matrix[row_number, col_number]")

            if type(self) == csc_matrix:
                return self[Translator.index_translate(col), Translator.index_translate(row)]
            return self[Translator.index_translate(row), Translator.index_translate(col)]
    
    if not hasattr(csr_matrix, "get"): csr_matrix.get = mat_get
    
    if not hasattr(csc_matrix, "get"): csc_matrix.get = mat_get


# Silent context manager
from os import devnull # for silencing stdout warnings (pandas using psycopg2 connection right now)
import sys

class Silent():
    '''Used as a context manager to silence anything in its block'''

    real_stdout = sys.stdout
    real_stderr = sys.stderr
    instance = None

    def __new__(cls):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __enter__(self):
        self.dn = open(devnull, "w")
        sys.stdout = self.dn
        sys.stderr = self.dn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.dn.close()
        sys.stdout = self.real_stdout
        sys.stderr = self.real_stderr
        