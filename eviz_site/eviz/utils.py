from scipy.sparse import coo_matrix
from eviz.models import AggEtaPFU
from json import loads as json_from_string
from django.contrib.auth.models import User
import plotly.express as px  # for making the scatter plot
import pandas.io.sql as pd_sql  # for getting data into a pandas dataframe
from eviz.models import *
import sys
from os import devnull
from django.db import connection
import plotly.graph_objects as pgo


from time import time
def time_view(v):
    '''Wrapper to time how long it takes to deliver a view

    Inputs:
        v, function: the view to time

    Outputs:
        A function which wil prints how long the given view took to run
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

    translated_query = dict()  # set up to build and return at the end

    # common query parts
    if v := query.get("dataset"):
        translated_query["Dataset"] = Translator.dataset_translate(v)
    if v := query.get("country"):
        if type(v) == list:
            translated_query["Country__in"] = [
                Translator.country_translate(country) for country in v]
        else:
            translated_query["Country"] = Translator.country_translate(v)
    if v := query.get("method"):
        if type(v) == list:
            translated_query["Method__in"] = [
                Translator.method_translate(method) for method in v]
        else:
            translated_query["Method"] = Translator.method_translate(v)
    if v := query.get("energy_type"):
        if type(v) == list:
            translated_query["EnergyType__in"] = [
                Translator.energytype_translate(energy_type) for energy_type in v]
        else:
            translated_query["EnergyType"] = Translator.energytype_translate(v)
    if v := query.get("last_stage"):
        translated_query["LastStage"] = Translator.laststage_translate(v)
    if v := query.get("ieamw"):
        if type(v) == list:
            # both were selected, use the both option in the table
            translated_query["IEAMW"] = Translator.ieamw_translate("Both")
        else:
            translated_query["IEAMW"] = Translator.ieamw_translate(v)
    # includes neu either is in the query or not, it's value does need to be more than empty string, though
    translated_query["IncludesNEU"] = Translator.includesNEU_translate(
        bool(query.get("includes_neu")))
    if v := query.get("chopped_mat"):
        translated_query["ChoppedMat"] = Translator.matname_translate(v)
    if v := query.get("chopped_var"):
        translated_query["ChoppedVar"] = Translator.index_translate(v)
    if v := query.get("product_aggregation"):
        translated_query["ProductAggregation"] = Translator.agglevel_translate(
            v)
    if v := query.get("industry_aggregation"):
        translated_query["IndustryAggregation"] = Translator.agglevel_translate(
            v)
    if v := query.get("grossnet"):
        translated_query["GrossNet"] = Translator.grossnet_translate(
            v)
    # plot-specific query parts
    if v := query.get("to_year"):
        # if year part is a range of years, i.e. to_year present
        # set up query as range
        translated_query["Year__lte"] = int(v)
        if v := query.get("year"):
            translated_query["Year__gte"] = int(v)
    elif v := query.get("year"):
        # else just have year be one year
        translated_query["Year"] = int(v)
    if v := query.get("matname"):
        if v == "RUVY":
            translated_query["matname__in"] = [Translator.matname_translate("R"), Translator.matname_translate("U"), Translator.matname_translate("V"), Translator.matname_translate("Y")]
        else:
            translated_query["matname"] = Translator.matname_translate(v)

    return translated_query

def shape_post_request(
    payload, get_plot_type = False
) -> tuple[str, dict]:
    '''Turn a POST request payload into a ready to use query in a dictionary

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
    '''

    shaped_query = dict(payload)

    if get_plot_type:
        try:
            # to be returned at the end
            plot_type = shaped_query.pop("plot_type")[0]
        except KeyError:
            plot_type = None

    # get rid of security token, is not part of a query
    shaped_query.pop("csrfmiddlewaretoken", None)

    for k, v in shaped_query.items():

        # convert from list (if just one item in list)
        if len(v) == 1:
            shaped_query[k] = v[0]

    if get_plot_type:
        return (plot_type, shaped_query)
    return shaped_query


def iea_valid(user: User, query: dict) -> bool:
    '''Ensure that a give user's query does not give out IEA data if not authorized

    Inputs:

        user, user info from the HTTP request (for Django requsests: request.user): the user whose authorizations need to be checked

        query, a dict: the query to investigate

    Output:

        the boolean value of if a user's query is valid (True) or not (False)
    '''

    # will short curcuit if the data is free,
    # so everything past the "or" will not be checked if not neccessary
    return (
        # free data
        (
            query.get("dataset", None) != "IEAEWEB2022"
            and query.get("ieamw", None) == "MW"
        )
        or
        # authorized to get proprietary data
        (user.is_authenticated and user.has_perm("eviz.get_iea"))
    )

# TODO: is this all temp? do we want to keep all the data in seperate db's or will we actually use the dataset column?
def get_database(query: dict) -> str:
    """Determine the appropriate database to use based on the query parameters.

    Input:
        query (dict): A dictionary containing query parameters, including a 'Dataset' key.

    Output:
        str or None: The name of the database to use, or None if the database is invalid.
    """
    
    # Translate the 'Dataset' value from the query to a database identifier
    db = Translator.dataset_translate(query["Dataset"])
    
    # TODO: this is missing IEA, we have to get where that is
    if db not in ["CLPFUv2.0a1", "CLPFUv2.0a2", "CLPFUv2.0a3"]:
        return None # database is invalid
    return db

from pathlib import Path
with open(f"{Path(__file__).resolve().parent.parent}/internal_resources/sankey_color_scheme.json") as f:
    colors_data = f.read()
SANKEY_COLORS: dict[str, str] = json_from_string(colors_data)
def get_sankey(query: dict) -> pgo.Figure:
    ''' Gets a sankey diagram for a query

    Input:

        query, dict: a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Outputs:

        a plotly Figure with the sankey data

        or None if there is no cooresponding data for the query
    '''

    # we do a little shaping
    if "matname" in query.keys():
        del query["matname"]

    if (db := get_database(query)) == None:
        return None

    # get all four matrices to make the full RUVY matrix
    data = PSUT.objects.using(db).values_list("i", "j", "x").filter(
        **query, matname__in = [
            Translator.matname_translate("R"),
            Translator.matname_translate("U"),
            Translator.matname_translate("V"),
            Translator.matname_translate("Y")
        ]
    )

    # if no cooresponding data, return as such
    if not data:
        return None

    # get rid of any duplicate i,j,x combinations (many exist)
    data = set(data)

    # begin constructing the sankey
    label_to_index = dict() # used to know which human-readable label is where in the label list
    next_index = 0 # used to keep track of where a new label is added in the label list

    labels = list() # used to keep track of all the labels
    sources = list() # used to keep track of all the sources (from-nodes)
    targets = list() # used to keep track of all the targets (to-nodes)
    magnitudes = list() # used to keep track of all the magnitudes between the nodes

    flow_colors = list()

    # TODO: the columns of R V, rows of U Y, should be invisible nodes
    # also colors are based on the prefix of the node name
    # e.g. "Hydro [from ...]" should be considered "Hydro" in the color scheme
    for row, col, magnitude in data:
        translated_row = Translator.index_translate(row)
        translated_col = Translator.index_translate(col)

        # Get the row (source) label's index and make the start of a connection
        idx = label_to_index.get(translated_row, -1)

        if idx == -1:  # label is new
            labels.append(translated_row)
            label_to_index[translated_row] = idx = next_index
            next_index += 1

        sources.append(idx)

        # Get the col (target) label's index and make the end of a connection
        idx = label_to_index.get(translated_col, -1)
        if idx == -1:  # label is new
            labels.append(translated_col)
            label_to_index[translated_col] = idx = next_index
            next_index += 1

        targets.append(idx)

        # Finish the connection with the magnitude of the connection
        magnitudes.append(magnitude)

        # make in-flow special color if node has special color
        #     i.e. if current target node has color besides default node color
        # only on targets (columns) because only targets can have in-flows
        # if ((assoc_color := node_colors[idx]) != "wheat"):
        #     flow_color = assoc_color

        # flow_colors.append(flow_color)

    return pgo.Figure(data=[pgo.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            label=labels,
            # color=node_colors
        ),
        link=dict(
            source=sources,
            target=targets,
            value=magnitudes,
            color="rgba(100,100,100,0.5)"
        ))])


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def get_xy(efficiency_metric, query: dict, color_by: str, line_by: str, facet_col_by: str = None, facet_row_by: str = None, energy_type: str = None) -> go.Figure:
    """ Generate a line plot based on the given efficiency metric and query parameters.

    Inputs:
        efficiency_metric: The efficiency metric to plot on the y-axis.
        query: A dictionary containing filter parameters for the database query.
        color_by: The field to use for coloring the lines.
        line_by: The field to use for line dash styles.
        facet_col_by: The field to use for faceting columns.
        facet_row_by: The field to use for faceting rows.
        energy_type: The type of energy (Energy, Exergy, or both) for y-axis label.

    Outputs:
        go.Figure: A Plotly figure object containing the generated plot.
    """
    
    # Retrieve the database based on the query
    db = get_database(query)
    if db is None:
        return go.Figure().add_annotation(text="No database found", showarrow=False)

    # Create a list of fields to select, always including 'Year' and the efficiency metric
    fields_to_select = ["Year", efficiency_metric]

    # Map the names to the actual database field names
    field_mapping = {
        'country': 'Country',
        'energy_type': 'EnergyType',
        'includes_neu': 'IncludesNEU',
        'last_stage': 'LastStage'
    }
    
    # Add color_by, line_by, facet_col_by, and facet_row_by fields to the selection list
    for field in [color_by, line_by, facet_col_by, facet_row_by]:
        if field in field_mapping:
            fields_to_select.append(field_mapping[field])
        
    # Query the database
    agg_query = AggEtaPFU.objects.using(db).filter(**query).values(*fields_to_select)

    # Convert query results to a pandas DataFrame
    df = pd.DataFrame(list(agg_query))

    if df.empty:
        return go.Figure().add_annotation(text="No data found for the given query", showarrow=False)

    try:
        # Create the line plot using Plotly Express
        fig = px.line(
            df, x="Year", y=efficiency_metric, 
            color=field_mapping.get(color_by, color_by),
            line_dash=field_mapping.get(line_by, line_by),
            facet_col=field_mapping.get(facet_col_by,facet_col_by),
            facet_row=field_mapping.get(facet_row_by,facet_row_by),
            facet_col_spacing=0.05,
        )
        
        # Set the y-axis title based on the energy type
        if 'Energy' in energy_type and 'Exergy' in energy_type:
            y_title = f"EX<sub>{efficiency_metric[-1]}</sub> [TJ]"
        elif energy_type == 'Exergy':
            y_title = f"X<sub>{efficiency_metric[-1]}</sub> [TJ]"
        elif energy_type == 'Energy':
            y_title = f"E<sub>{efficiency_metric[-1]}</sub> [TJ]"
        else:
            y_title = efficiency_metric

        # Update layout with axis lines
        fig.update_xaxes(
            showgrid=False,
            zeroline=False,
            ticklen=10,
            ticks="inside",
            title=None,
            linecolor='black',
            linewidth=1,
            mirror=False
        )
        fig.update_yaxes(
            showgrid=False,
            zeroline=False,
            ticklen=10,
            ticks="inside",
            title=y_title,
            linecolor='black',
            linewidth=1,
            mirror=False,
            showticklabels=True
        )

        # Force x-axis to bottom and y-axis to left for all subplots (used because of faceting)
        fig.update_xaxes(position=0)
        fig.update_yaxes(position=0)

        # Update overall layout
        fig.update_layout(
            plot_bgcolor="white",
            showlegend=False,
            margin=dict(l=50, r=50, t=50, b=50),
        )
        
        # Remove y-axis titles for all but the first column when using facet columns
        if facet_col_by:
            for i in range(2, len(fig.data) + 1):
                fig.update_yaxes(title_text="", col=i)

        return fig
    
    except Exception as e:
        # Return a message if plot fails.
        return go.Figure().add_annotation(text=f"Error creating plot: {str(e)}", showarrow=False)



def get_matrix(query: dict) -> coo_matrix:
    '''Collects, constructs, and returns one of the RUVY matrices

    Inputs:
        a query ready to hit the database, i.e. translated as neccessary (see translate_query())

    Outputs:
        A scipy coo_matrix containing all the values from the specified query
        or None if the given query related to no data 
    '''
    print(query)
    if db := get_database(query) == None:
        return None

    # Get the sparse matrix representation
    # i, j, x for row, column, value
    # in 3-tuples
    sparse_matrix = (
        PSUT.objects
        .using(db)
        .values_list("i", "j", "x")
        .filter(**query)
    )

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


def visualize_matrix(mat: coo_matrix, color_scale: str = 'viridis') -> pgo.Figure:
    """Visualize a sparse matrix as a heatmap using Plotly.

    Inputs:
        mat (coo_matrix): A scipy sparse matrix in COOrdinate format.
        color_scale (str, optional): The color scale to use for the heatmap. Defaults to 'viridis'.

    Outputs:
        pgo.Figure: A Plotly graph object Figure containing the heatmap.
    """
    # Convert the matrix to a format suitable for Plotly's heatmap
    rows, cols, vals = mat.row, mat.col, mat.data
    # Translate row and column indices to human-readable labels
    row_labels = [Translator.index_translate(i) for i in rows]
    col_labels = [Translator.index_translate(i) for i in cols]
    
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


COLUMNS = ["Dataset", "Country", "Method", "EnergyType", "LastStage", "IEAMW", "IncludesNEU", "Year", "ChoppedMat", "ChoppedVar", "ProductAggregation", "IndustryAggregation", "matname", "i", "j", "x"]
def get_translated_dataframe(query: dict, columns: list):
    """Retrieve and translate data from the database based on the given query and columns.

    Inputs:
        query (dict): A dictionary containing filter parameters for the database query.
        columns (list): A list of column names to retrieve from the database.

    Outputs:
        pandas.DataFrame or None: A DataFrame containing the translated data, or None if the database is not found.
    """
    # Get the database name based on the query
    if db := get_database(query) == None:
        return None
    
    # get the data from database
    db_query = PSUT.objects.using(db).filter(**query).values(*columns).query
    with Silent():
        # Use pandas to read the SQL query result into a DataFrame
        df = pd_sql.read_sql_query(str(db_query), con=connection.cursor().connection)
    
    # Translate the DataFrame's column names
    translate_columns = {
        'Dataset': Translator.dataset_translate,
        'Country': Translator.country_translate,
        'Method': Translator.method_translate,
        'EnergyType': Translator.energytype_translate,
        'LastStage': Translator.laststage_translate,
        'IEAMW': Translator.ieamw_translate,
        'ChoppedMat': Translator.matname_translate,
        'ChoppedVar': Translator.index_translate,
        'ProductAggregation': Translator.agglevel_translate,
        'IndustryAggregation': Translator.agglevel_translate,
        'matname': Translator.matname_translate,
        'grossnet': Translator.grossnet_translte,
        'i': Translator.index_translate,
        'j': Translator.index_translate
    }

    # Apply the translation functions to each column if it exists in the DataFrame
    for col, translate_func in translate_columns.items():
        if col in df.columns:
            df[col] = df[col].apply(translate_func)
    
    # Handle IncludesNEU separately as it's a boolean
    if 'IncludesNEU' in df.columns:
        df['IncludesNEU'] = df['IncludesNEU'].apply(lambda x: 'Yes' if x else 'No')
    
    return df

def get_csv_from_query(query: dict, columns: list = COLUMNS):
    
    # index false to not have column of row numbers
    return get_translated_dataframe(query, columns).to_csv(index=False)

def get_excel_from_query(query: dict, columns = COLUMNS):

    # index false to not have column of row numbers
    return get_translated_dataframe(query, columns).to_excel(index=False)

from bidict import bidict
from django.apps import apps
class Translator:
    # A dictionary where keys are model names and values are bidict objects
    __translations = {}

    @staticmethod
    def __load_bidict(model_name, id_field, name_field) -> bidict:
        """
        Load translations for a specific model if not already loaded.
        
        Args:
            model_name (str): The name of the model to load translations for.
            id_field (str): The name of the ID field in the model.
            name_field (str): The name of the field containing the human-readable name.
        
        Returns:
            bidict: A bidirectional dictionary of translations for the model.
        """
        if model_name not in Translator.__translations:
            # Get the model class dynamically
            model = apps.get_model(app_label='eviz', model_name=model_name)
            # Create a bidict with name:id pairs
            Translator.__translations[model_name] = bidict({getattr(item, name_field): getattr(item, id_field) for item in model.objects.all()})
        return Translator.__translations[model_name]

    @staticmethod
    def _translate(model_name, value, id_field, name_field):
        # Translate a value between its ID and name for a specific model.
        # value: The value to translate (can be either an ID or a name).
        # Returns: The translated value (either ID or name, depending on input).
        translations = Translator.__load_bidict(model_name, id_field, name_field)
        return translations.get(value) or translations.inverse.get(value, value)

    # The following methods are specific translation functions for different models
    # They all use the _translate method with appropriate parameters
    @staticmethod
    def index_translate(value):
        return Translator._translate('Index', value, 'IndexID', 'Index')

    @staticmethod
    def dataset_translate(value):
        return Translator._translate('Dataset', value, 'DatasetID', 'Dataset')

    @staticmethod
    def country_translate(value):
        return Translator._translate('Country', value, 'CountryID', 'FullName')

    @staticmethod
    def method_translate(value):
        return Translator._translate('Method', value, 'MethodID', 'Method')

    @staticmethod
    def energytype_translate(value):
        return Translator._translate('EnergyType', value, 'EnergyTypeID', 'FullName')

    @staticmethod
    def laststage_translate(value):
        return Translator._translate('LastStage', value, 'ECCStageID', 'ECCStage')

    @staticmethod
    def ieamw_translate(value):
        return Translator._translate('IEAMW', value, 'IEAMWID', 'IEAMW')

    @staticmethod
    def matname_translate(value):
        return Translator._translate('matname', value, 'matnameID', 'matname')
    @staticmethod
    def grossnet_translate(value):
        return Translator._translate('GrossNet', value, 'GrossNetID', 'GrossNet')

    @staticmethod
    def agglevel_translate(value):
        return Translator._translate('AggLevel', value, 'AggLevelID', 'AggLevel')

    @staticmethod
    def includesNEU_translate(value):
        return int(value) if isinstance(value, bool) else int(bool(value))

    @staticmethod
    def get_all(attribute):
        """
        Get all possible values for a given attribute.
        
        Inputs:
            attribute (str): The name of the attribute to get values for.
        
        Outputs:
            list: A list of all possible values (names) for the attribute.
        """
        # Dictionary mapping attribute names to model details
        model_mappings = {
            'dataset': ('Dataset', 'DatasetID', 'Dataset'),
            'country': ('Country', 'CountryID', 'FullName'),
            'method': ('Method', 'MethodID', 'Method'),
            'energytype': ('EnergyType', 'EnergyTypeID', 'FullName'),
            'laststage': ('LastStage', 'ECCStageID', 'ECCStage'),
            'ieamw': ('IEAMW', 'IEAMWID', 'IEAMW'),
            'matname': ('matname', 'matnameID', 'matname'),
            'agglevel': ('AggLevel', 'AggLevelID', 'AggLevel'),
            'grossnet': ('GrossNet', 'GrossNetID', 'GrossNet'),
        }
        
        if attribute not in model_mappings:
            raise ValueError(f"Unknown attribute: {attribute}")
        
        # Get model details and load translations
        model_name, id_field, name_field = model_mappings[attribute]
        translations = Translator.__load_bidict(model_name, id_field, name_field)
        return list(translations.keys())

    @staticmethod
    def get_all_available(attribute):
        """Get all available values for a given attribute from the PSUT model.
        
        Inputs:
            attribute (str): The name of the attribute to get values for.
        
        Outputs:
            A list of distinct values for the attribute from the PSUT model.
        """
        # Dictionary mapping attribute names to model details
        model_mappings = {
            'dataset': ('Dataset', 'DatasetID', 'Dataset'),
            'country': ('Country', 'CountryID', 'FullName'),
            'method': ('Method', 'MethodID', 'Method'),
            'energytype': ('EnergyType', 'EnergyTypeID', 'FullName'),
            'laststage': ('LastStage', 'ECCStageID', 'ECCStage'),
            'ieamw': ('IEAMW', 'IEAMWID', 'IEAMW'),
            'matname': ('matname', 'matnameID', 'matname'),
            'agglevel': ('AggLevel', 'AggLevelID', 'AggLevel'),
            'grossnet': ('GrossNet', 'GrossNetID', 'GrossNet'),
        }
        
        if attribute not in model_mappings:
            raise ValueError(f"Unknown attribute: {attribute}")
        
        model_name, id_field, name_field = model_mappings[attribute]
        translations = Translator.__load_bidict(model_name, id_field, name_field)

        # Print distinct values for the attribute from the PSUT model
        print(PSUT.objects.order_by().values_list(model_name, flat=True).distinct())

    @staticmethod
    def get_includesNEUs():
        return [True, False]

# TODO: this needs to be fixed...
# def temp_add_get():

#     def mat_get(self, row, col):
#             if type(row) != str or type(col) != str:
#                 raise ValueError("Getting item from RUVY matrix must be as follows: matrix['row_name', 'column_name'] or matrix[row_number, col_number]")

#             if type(self) == csc_matrix:
#                 return self[Translator.index_translate(col), Translator.index_translate(row)]
#             return self[Translator.index_translate(row), Translator.index_translate(col)]

#     if not hasattr(csr_matrix, "get"): csr_matrix.get = mat_get

#     if not hasattr(csc_matrix, "get"): csc_matrix.get = mat_get


# Silent context manager


class Silent():
    '''Used as a context manager to silence anything in its block'''

    real_stdout = sys.stdout # Store the original stdout
    real_stderr = sys.stderr # Store the original stderr
    instance = None # Class variable to store the singleton instance

    def __new__(cls):
        '''Implement the Singleton pattern to ensure only one instance of Silent is created.
        
        Outputs:
            Silent: The single instance of the Silent class.
        '''
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __enter__(self):
        '''Called when entering the context manager block.
        Redirects stdout and stderr to /dev/null.
        '''
        self.dn = open(devnull, "w") # Open /dev/null for writing
        sys.stdout = self.dn  # Redirect stdout to /dev/null
        sys.stderr = self.dn # Redirect stderr to /dev/null

    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''
        Called when exiting the context manager block.
        Restores the original stdout and stderr, and closes the /dev/null file.

        Inputs:
            exc_type: The type of the exception that caused the context to be exited.
            exc_value: The instance of the exception that caused the context to be exited.
            exc_traceback: A traceback object encoding the stack trace.
        '''
        self.dn.close()  # Close the /dev/null file
        sys.stdout = self.real_stdout # Restore the original stdout
        sys.stderr = self.real_stderr # Restore the original stderr

from uuid import uuid4
import pickle
def new_email_code(form) -> str:
    """Generate a new email verification code and save associated account information.

    Inputs:
        form: A form object containing cleaned account setup information.

    Outputs:
        str: A unique verification code.
    """
    # Generate a unique code using UUID
    code = str(uuid4())
    account_info = pickle.dumps(form.clean()) # get the cleaned form (a map) serialized
    EmailAuthCodes(code=code, account_info=account_info).save() # save account setup info to database
    return code

def get_user_history(request) -> list:
    """Retrieve the user's plot history from cookies.

    Inputs:
        request: The HTTP request object containing cookies.

    Outputs:
        list: The user's plot history, or an empty list if no history exists.
    """
    # Get the serialized user history from cookies
    serialized_data = request.COOKIES.get('user_history')

    if serialized_data:
        user_history = pickle.loads(bytes.fromhex(serialized_data)) # Deserialize the data if it exists
    else:
        user_history = list() # Return an empty list if no history exists

    return user_history

MAX_HISTORY = 5 # Maximum number of items to keep in the user's history
def update_user_history(request, plot_type, query):
    """Update the user's plot history with a new plot query.

    Inputs:
        request: The HTTP request object.
        plot_type (str): The type of plot being added to the history.
        query (dict): The query parameters for the plot.

    Outputs:
        bytes: Serialized updated user history.
    """
    # Get the current user history
    user_history = get_user_history(request)

    # Create a dictionary with the new history data
    history_data = {
        'plot_type': plot_type,
        **query
    }

    # Check if user_history is not empty
    if user_history:

        # if query is already in history, remove it to move it to the top
        try:
            user_history.remove(history_data)
        except ValueError: pass # don't care if not in, trying to remove anyways

        user_history.insert(0, history_data) # finally, add the new query to the top of the history

        # if the queue is full, take the end off
        if len(user_history) > MAX_HISTORY: user_history.pop()

    else:
        # If user_history is empty, append the new history_data
        user_history.append(history_data)

    # Serialize the updated user history
    serialized_data = pickle.dumps(user_history)
    return serialized_data
