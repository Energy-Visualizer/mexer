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
import time

from altair.utils.data import MaxRowsError  # for catching with matrices are too big
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Mexer.models import AggEtaPFU, EvizUser, Version
from plotly.offline import plot
from utils.data import (
    AGGETA_COLUMNS,
    META_COLUMNS,
    PSUT_COLUMNS,
    DatabaseTarget,
    ShapedQuery,
    get_csv_from_query,
    get_excel_from_query,
    shape_post_request,
    translate_query,
)
from utils.history import update_user_history
from utils.logging import LOGGER
from utils.lookup import LookupManager
from utils.matrix import get_matrix, get_ruvy_matrix, visualize_matrix
from utils.misc import get_plot_title, iea_valid, time_view
from utils.sankey import get_sankey
from utils.xy_plot import get_xy


@login_required(login_url="/login")
@time_view
def visualizer(request):
    """Render the visualizer page with all necessary data for the user interface.

    This view requires user authentication and is timed for performance monitoring.

    Inputs:
        request: The HTTP request object

    Outputs:
        Rendered HTML response of the visualizer page with context data
    """

    LOGGER.info("Visualizer page visted.")

    # see if the user is iea approved
    iea_user = request.user.is_authenticated and request.user.has_perm("eviz.get_iea")

    # see if the user is an admin to get access to SandboxDB table
    try:
        admin_user = EvizUser.objects.get_by_natural_key(request.user.username).is_staff
    except Exception as e:
        print(e)
        admin_user = False

    # Fetch all available options for various parameters from the Translator
    if admin_user:
        datasets = LookupManager.attribute("datasets:admin")
    else:
        datasets = LookupManager.attribute("datasets:public")

    countries = LookupManager.attribute("country")
    countries.sort()
    versions = LookupManager.attribute("version")
    if admin_user:
        sandbox_versions = [
            settings.SANDBOX_PREFIX + ver
            for ver in Version.objects.using("sandbox").values_list(
                "Version", flat=True
            )
        ]
    else:
        sandbox_versions = []
    # methods = Translator.get_all('method')
    methods = ["PCM"]  # override, we don't show all the options
    energy_types = LookupManager.attribute("energytype")
    # last_stages = Translator.get_all('laststage')
    last_stages = ["Final", "Useful"]  # override, we don't show all the options
    grossnets = LookupManager.attribute("grossnet")
    product_aggregations = LookupManager.attribute("agglevel")
    industry_aggregations = LookupManager.attribute("agglevel")
    matnames = LookupManager.attribute("matname")
    matnames.sort()

    # Prepare the context dictionary for the template
    context = {
        "datasets": datasets,
        "default_dataset": "CL-PFU MW",
        "versions": versions,
        "default_version": "v2.0",
        "sandbox_versions": sandbox_versions,
        "default_sandbox_version": settings.SANDBOX_PREFIX + "v2.0a7",
        "countries": countries,
        "default_country": "Ghana",
        "methods": methods,
        "default_method": methods[0],
        "energy_types": energy_types,
        "default_energy_type": energy_types[0],
        "last_stages": last_stages,
        "default_last_stage": last_stages[0],
        "grossnets": grossnets,
        "default_grossnet": grossnets[0],
        "matnames": matnames,
        "default_matname": matnames[0],
        "product_aggregations": product_aggregations,
        "default_product_aggregation": product_aggregations[0],
        "industry_aggregations": industry_aggregations,
        "default_industry_aggregation": industry_aggregations[0],
        "iea_user": iea_user,
        "site_version": settings.SITE_VERSION,  # version of the site to be displayed to users
    }

    return render(request, "visualizer.html", context)


def generate_sankey_html(target: DatabaseTarget, query: ShapedQuery) -> str:
    translated_query = translate_query(target, query)
    nodes, links, options, num_columns = get_sankey(target, translated_query)

    if nodes is None:
        return "Error: No cooresponding data"
    return f"<script>createSankey({nodes},{links},{options},\"{get_plot_title(query)}\",{num_columns})</script>\
                    <button onclick='downloadSankey()' class='absolute top-2 right-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>Download Sankey</button>"


def generate_xy_html(target: DatabaseTarget, query: ShapedQuery) -> str:
    # Extract specific parameters for xy_plot
    efficiency_metric = str(query.get("efficiency"))
    color_by = str(query.get("color_by"))
    line_by = str(query.get("line_by"))
    facet_col_by = str(query.get("facet-col-by"))
    facet_row_by = str(query.get("facet-row-by"))
    energy_type = str(query.get("energy_type"))

    # Handle combined Energy and Exergy case
    if "Energy" in energy_type and "Exergy" in energy_type:
        energy_type = "Energy, Exergy"

    translated_query = translate_query(target, query)
    xy = get_xy(
        efficiency_metric,
        target,
        translated_query,
        color_by,
        line_by,
        facet_col_by,
        facet_row_by,
        energy_type,
    )
    if xy is None:
        return "Error: No corresponding data"

    xy.update_layout(
        title=get_plot_title(
            query, exclude=[color_by, line_by, facet_col_by, facet_row_by, energy_type]
        )
    )
    LOGGER.info("XY plot made")
    # Remove the <div> wrapper for consistency with other plot types
    return (
        plot(xy, output_type="div", include_plotlyjs=False)
        .removeprefix("<div>")
        .removesuffix("</div>")
    )


def generate_matrix_html(target: DatabaseTarget, query: ShapedQuery) -> str:
    # Extract specific parameters for matrices
    matrix_name = str(query.get("matname"))
    color_scale = str(query.get("color_scale", "inferno"))

    # Retrieve the matrix
    coloring_method = str(query.get("coloring_method", "weight"))
    translated_query = translate_query(target, query)

    matname = None
    if matrix_name == "RUVY" and coloring_method == "ruvy":
        matrix, matname = get_ruvy_matrix(target, translated_query)
    else:
        matrix = get_matrix(target, translated_query)

    if matrix is None:
        return "Error: No corresponding data"

    heatmap = visualize_matrix(target, matrix, matname, color_scale, coloring_method)
    heatmap = heatmap.properties(
        title=matrix_name + " Matrix: " + get_plot_title(query),
        autosize={"type": "fit", "contains": "padding"},
    )

    try:
        LOGGER.info("Matrix visualization made")
        return heatmap.to_html()
    except MaxRowsError:
        LOGGER.error("Overly large matrix attempted")
        return "Error: Query results in overly large dataset. Please try a different visualization method or download the raw data."


@csrf_exempt  # TODO: why is this exempt?
@time_view
def get_plot(request: HttpRequest):
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

    if request.method != "POST":
        return HttpResponse(status=405)

    query, plot_type, target = shape_post_request(request.POST)

    try:
        dataset = str(query["dataset"])
        version = str(query["version"])
        is_dataset_sandbox = dataset.startswith(settings.SANDBOX_PREFIX)
        is_version_sandbox = version.startswith(settings.SANDBOX_PREFIX)
        if is_dataset_sandbox ^ is_version_sandbox:
            return HttpResponse(
                b"Error: Dataset and version must both be from sandbox or both not be from sandbox!"
            )
    except Exception:
        pass

    separate_window = query.get("separate_window") == "on"

    # Check if the user has access to IEA data.
    # TODO: make this work with status = 403, problem is HTMX won't show anything.
    if not iea_valid(request.user, query):
        LOGGER.warning(
            f"IEA data requested by unauthorized user {request.user.get_username() or 'anonymous user'}"
        )
        return HttpResponse(
            b"You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
            b"You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>."
        )

    plot_div: str  # Result HTML.

    # Use match-case to handle different plot types
    match plot_type:
        case "sankey":
            plot_div = generate_sankey_html(target, query)

        case "xy_plot":
            plot_div = generate_xy_html(target, query)

        case "matrices":
            plot_div = generate_matrix_html(target, query)

        case _:  # default
            plot_div = "Error: Plot type not specified or supported"
            LOGGER.warning("Unrecognized plot type requested")

    # stop early if an error occured, and send error message to client
    if plot_div.startswith("Error"):
        return HttpResponse(plot_div.encode())

    # Add functions to call on the client side
    plot_div = plot_div + "<script>refreshHistory();</script>"
    if separate_window:
        plot_div = plot_div + "<script>plotInNewWindow();</script>"
    response = HttpResponse(plot_div.encode())  # the final response to be returned

    # Set ploy history cookie to expire in 7 days
    serialized_data = update_user_history(request, plot_type, query)
    response.set_cookie("user_history", serialized_data.hex(), max_age=7 * 24 * 60 * 60)

    return response


@time_view
def get_data(request: HttpRequest):
    """Handle data retrieval requests and return CSV data based on the query.

    Inputs:
        request (HttpRequest): The HTTP request object.

    Outputs:
        HttpResponse: A response containing CSV data or an error message.
    """

    # if user is not logged in their username is empty string
    # mark them as anonymous in the logs
    LOGGER.info(f"Data requested by {request.user.get_username() or 'anonymous user'}")

    if request.method != "POST":
        return HttpResponse(status=405)

    data_format = request.POST.get("returnDataType")
    if data_format is None:
        return HttpResponse("Data format unspecified", status=400)

    query, _, target = shape_post_request(request.POST)

    if not iea_valid(request.user, query):
        LOGGER.warning(
            f"IEA data requested by unauthorized user {request.user.get_username() or 'anonymous user'}"
        )
        return HttpResponse(
            "You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions. \
                            You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.".encode()
        )

    query = translate_query(target, query)

    LOGGER.info(query)

    columns: list[str] = []
    if target[1] is AggEtaPFU:
        # get xy info
        columns = META_COLUMNS + AGGETA_COLUMNS
    else:
        # get psut (sankey and matrix) info
        columns = META_COLUMNS + PSUT_COLUMNS

    final_response = HttpResponse()
    filename = f"mexer-data-{time.strftime('%H-%M_%d-%m-%Y')}"

    if data_format == "csv":
        final_response.write(get_csv_from_query(target, query, columns).encode())
        final_response.headers["Content-Type"] = "text/csv"
        final_response.headers["Content-Disposition"] = (
            f'attachment; filename="{filename}.csv"'
        )
        LOGGER.info("Made CSV data")
    elif data_format == "excel":
        final_response.write(get_excel_from_query(target, query, columns))
        final_response.headers["Content-Type"] = (
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        final_response.headers["Content-Disposition"] = (
            f'attachment; filename="{filename}.xlsx"'
        )
        LOGGER.info("Made Excel data")

    return final_response
