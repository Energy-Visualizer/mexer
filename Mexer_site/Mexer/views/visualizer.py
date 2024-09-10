####################################################################
# visualizer.py includes all views that the visualization page utilizes
# 
# The three main views are
# The visualizer page itself - where users make queries and see plots
# The plotting page - the page where, given a post request, plot html will be returned
# The data page - the page where, given a post request, data in csv or excel (wip) will be returned
# 
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from utils.misc import time_view, iea_valid, get_plot_title
from utils.logging import LOGGER
from Mexer.models import EvizUser, Version, AggEtaPFU
from utils.translator import Translator
from Mexer_meta.settings import SANDBOX_PREFIX
from django.shortcuts import render
from utils.data import *
from django.http import HttpResponse
from utils.sankey import get_sankey
from utils.xy_plot import get_xy
from utils.matrix import get_matrix, get_ruvy_matrix, visualize_matrix
from plotly.offline import plot
from utils.history import update_user_history


@login_required(login_url="/login")
@time_view
def visualizer(request):
    """ Render the visualizer page with all necessary data for the user interface.
    
    This view requires user authentication and is timed for performance monitoring.
    
    Inputs:
        request: The HTTP request object

    Outputs:
        Rendered HTML response of the visualizer page with context data
    """
    
    LOGGER.info("Visualizer page visted.")

    # see if the user is iea approved
    iea_user = request.user.is_authenticated and request.user.has_perm("Mexer.get_iea")
    
    # see if the user is an admin to get access to SandboxDB table
    try:
        admin_user = EvizUser.objects.get_by_natural_key(request.user.username).is_staff
    except:
        admin_user = False

    # Fetch all available options for various parameters from the Translator
    if admin_user:
        datasets = Translator.get_all('datasets:admin')
    else:
        datasets = Translator.get_all('datasets:public')
    
    countries = Translator.get_all('country')
    countries.sort()
    versions = Translator.get_all('version')
    if admin_user:
        sandbox_versions = [SANDBOX_PREFIX + ver for ver in Version.objects.using("sandbox").values_list("Version", flat=True)]
    else:
        sandbox_versions = []
    # methods = Translator.get_all('method')
    methods = ["PCM"] # override, we don't show all the options
    energy_types = Translator.get_all('energytype')
    # last_stages = Translator.get_all('laststage')
    last_stages = ["Final", "Useful"] # override, we don't show all the options
    grossnets = Translator.get_all('grossnet')
    product_aggregations = Translator.get_all('agglevel')
    industry_aggregations = Translator.get_all('agglevel')
    matnames = Translator.get_all('matname')
    matnames.sort(key=len)  # sort matrix names by how long they are... seems reasonable
    
    # Prepare the context dictionary for the template
    context = {
        "datasets":datasets,
        "default_dataset": "CL-PFU MW",

        "versions":versions,
        "default_version": "v2.0",

        "sandbox_versions":sandbox_versions,
        "default_sandbox_version": SANDBOX_PREFIX + "v2.0a7",

        "countries":countries,
        "default_country": "Ghana",

        "methods":methods,
        "default_method":methods[0],

        "energy_types":energy_types,
        "default_energy_type":energy_types[0],

        "last_stages":last_stages,
        "default_last_stage":last_stages[0],

        "grossnets":grossnets,
        "default_grossnet":grossnets[0],

        "matnames":matnames,
        "default_matname":matnames[0],
        
        "product_aggregations":product_aggregations,
        "default_product_aggregation":product_aggregations[0],

        "industry_aggregations":industry_aggregations,
        "default_industry_aggregation":industry_aggregations[0],

        "iea_user":iea_user
        }

    return render(request, "visualizer.html", context)

@csrf_exempt
@time_view
def get_plot(request):
    """Generate and return a plot based on the POST request data.
    
    This function handles different types of plot types (sankey, xy_plots, matrices) and manages 
    user access to IEA data. It also updates the user's plot history.
    
    Inputs:
        request (HttpRequest): The HTTP request object.

    Outputs:
        HttpResponse: A response containing the plot HTML or an error message.
    """

    # if user is not logged in their username is empty string
    # mark them as anonymous in the logs
    LOGGER.info(f"Plot requested by {request.user.get_username() or 'anonymous user'}")
    
    if request.method == "POST":
        # Extract plot type and query parameters from the POST request
        query, plot_type, target = shape_post_request(request.POST, ret_plot_type = True, ret_database_target = True)

        try:
            if query["dataset"].startswith(SANDBOX_PREFIX) != query["version"].startswith(SANDBOX_PREFIX):
                return HttpResponse("Error: Dataset and version must both be from sandbox or both not be from sandbox!")
        except:
            pass
        
        # get boolean of if the plot should be
        # in a separate window
        separate_window = query.get("separate_window") == "on"

        # Check if the user has access to IEA data
        # TODO: make this work with status = 403, problem is HTMX won't show anything
        if not iea_valid(request.user, query):
            LOGGER.warning(f"IEA data requested by unauthorized user {request.user.get_username() or 'anonymous user'}")
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.")
        
        plot_div = None # where to store what html will be sent to the user

        # Use match-case to handle different plot types
        match plot_type:
            case "sankey":
                translated_query = translate_query(target, query)
                nodes,links,options = get_sankey(target, translated_query)

                if nodes is None:
                    plot_div = "Error: No cooresponding data"
                else:
                    plot_div = f"<script>createSankey({nodes},{links},{options},'{get_plot_title(query)}')</script>\
                                <button onclick='downloadSankey()' class='sankey-download-button'>Download Sankey</button>"

            case "xy_plot":
                # Extract specific parameters for xy_plot
                efficiency_metric = query.get('efficiency')
                color_by = query.get("color_by")
                line_by = query.get("line_by")
                facet_col_by = query.get("facet-col-by")
                facet_row_by = query.get("facet-row-by")
                energy_type = query.get("energy_type")
                
                # Handle combined Energy and Exergy case
                if 'Energy' in energy_type and 'Exergy' in energy_type:
                    energy_type = 'Energy, Exergy'
                
                translated_query = translate_query(target, query)
                xy = get_xy(efficiency_metric, target, translated_query, color_by, line_by, facet_col_by, facet_row_by, energy_type)
                if xy is None:
                    plot_div = "Error: No corresponding data"
                else:
                    xy.update_layout(
                        title=get_plot_title(query, exclude=[color_by, line_by, facet_col_by, facet_row_by, energy_type])
                    )
                    plot_div = plot(xy, output_type="div", include_plotlyjs=False)
                    LOGGER.info("XY plot made")

            case "matrices":
                # Extract specific parameters for matrices
                matrix_name = query.get("matname")
                color_scale = query.get('color_scale', "inferno")

                # Retrieve the matrix
                coloring_method = query.get('coloring_method', 'weight')
                translated_query = translate_query(target, query)
                
                matname = None
                if matrix_name == "RUVY" and coloring_method == "ruvy":
                    matrix, matname = get_ruvy_matrix(target, translated_query)
                else:
                    matrix = get_matrix(target, translated_query)

                if matrix is None:
                    plot_div = "Error: No corresponding data"
                else:
                    heatmap = visualize_matrix(target, matrix, matname, color_scale, coloring_method)
                    heatmap = heatmap.properties(
                        title=matrix_name + " Matrix: " + get_plot_title(query),
                        autosize = {"type": "fit", "contains": "padding"}
                    )
                    plot_div = heatmap.to_html() # Render the figure as an HTML div
                
                LOGGER.info("Matrix visualization made")
        

            case _: # default
                plot_div = "Error: Plot type not specified or supported"
                LOGGER.warning("Unrecognized plot type requested")
        
        response = HttpResponse(plot_div) # the final response to be returned
        
        # Update user history only if there was no error
        if not plot_div.startswith("Error"):
            serialized_data = update_user_history(request, plot_type, query)
            response.content += b"<script>refreshHistory();</script>"
            if separate_window:
                response.content += b"<script>plotInNewWindow();</script>"
            # Set cookie to expire in 7 days
            response.set_cookie('user_history', serialized_data.hex(), max_age=7 * 24 * 60 * 60)

    return response

@time_view
def get_data(request):
    """ Handle data retrieval requests and return CSV data based on the query.

    Inputs:
        request (HttpRequest): The HTTP request object.

    Outputs:
        HttpResponse: A response containing CSV data or an error message.
    """

    # if user is not logged in their username is empty string
    # mark them as anonymous in the logs
    LOGGER.info(f"Data requested by {request.user.get_username() or 'anonymous user'}")

    if request.method == "POST":
        
        # set up query and get csv from it
        query, target = shape_post_request(request.POST, ret_database_target = True)

        if not iea_valid(request.user, query):
            LOGGER.warning(f"IEA data requested by unauthorized user {request.user.get_username() or 'anonymous user'}")
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.")

        # Translate the query to match database field names
        query = translate_query(target, query)

        # Generate CSV data based on the query
        if target[1] is AggEtaPFU:
            # get xy info
            csv = get_csv_from_query(target, query, columns = META_COLUMNS + AGGETA_COLUMNS)
        else:
            # get psut (sankey and matrix) info
            csv = get_csv_from_query(target, query, columns = META_COLUMNS + PSUT_COLUMNS)

        # set up the response:
        # content is the csv made above
        # then give csv MIME 
        # and appropriate http header
        final_response = HttpResponse(
            content = csv,
            content_type = "text/csv",
            headers = {"Content-Disposition": 'attachment; filename="eviz_data.csv"'} # TODO: make this file name more descriptive
        )
        LOGGER.info("Made CSV data")

        # TODO: excel downloads
        # MIME for workbook is application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
        # file handle is xlsx for workbook 

    return final_response