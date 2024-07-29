# Django imports
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives # for email verification
from django.views.decorators.csrf import csrf_exempt

# Eviz imports
from utils.history import *
from utils.misc import *
from utils.translator import *
from utils.data import *
from utils.sankey import get_sankey
from utils.xy_plot import get_xy
from utils.matrix import get_matrix, visualize_matrix
from eviz.models import Dataset, matname
from eviz.forms import SignupForm, LoginForm
from eviz.logging import LOGGER

# Visualization imports
from plotly.offline import plot

@time_view
def index(request):
    '''Render the home page.'''

    LOGGER.info("Home page visted.")
    return render(request, "index.html")

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
    plot_div = None
    if request.method == "POST":
        # Extract plot type and query parameters from the POST request
        query, plot_type, target = shape_post_request(request.POST, ret_plot_type = True, ret_database_target = True)

        # Check if the user has access to IEA data
        # TODO: make this work with status = 403, problem is HTMX won't show anything
        if not iea_valid(request.user, query):
            LOGGER.warning(f"IEA data requested by unauthorized user {request.user.get_username() or 'anonymous user'}")
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.")
        
        # Use match-case to handle different plot types
        match plot_type:
            case "sankey":
                translated_query = translate_query(target, query)
                nodes,links,options = get_sankey(target, translated_query)

                if nodes is None:
                    plot_div = "Error: No cooresponding data"
                else:
                    plot_div =f"<script>createSankey({nodes},{links},{options})</script>"

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
                    plot_div = plot(xy, output_type="div", include_plotlyjs=False)
                    LOGGER.info("XY plot made")

            case "matrices":
                # Extract specific parameters for matrices
                matrix_name = query.get("matname")
                color_scale = query.get('color_scale', "viridis")
                # Retrieve the matrix
                translated_query = translate_query(target, query)
                matrix = get_matrix(target, translated_query)
                
                if matrix is None:
                    plot_div = "Error: No corresponding data"
                
                else:
                    heatmap = visualize_matrix(target, matrix, color_scale)

                    heatmap.update_layout(
                        title = matrix_name + " Matrix",
                        yaxis = dict(title=''),
                        xaxis = dict(title=''),
                        xaxis_side = "top",
                        xaxis_tickangle = -45, 
                        scattermode = "overlay",
                        # plot_bgcolor = "rgba(0, 0, 0, 0)",
                    )

                    # Render the figure as an HTML div
                    plot_div = plot(heatmap, output_type="div", include_plotlyjs=False)
                    LOGGER.info("Matrix visualization made")
        

            case _: # default
                plot_div = "Error: Plot type not specified or supported"
                LOGGER.warning("Unrecognized plot type requested")
                
        response = HttpResponse(plot_div)
        
        # Update user history
        if not plot_div.startswith("Error"):
            serialized_data = update_user_history(request, plot_type, query)
            response.content += b"<script>refreshHistory();</script>"
            # Set cookie to expire in 30 days
            response.set_cookie('user_history', serialized_data.hex(), max_age=30 * 24 * 60 * 60)

    return response

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import pickle  # Make sure this is imported

def render_history(request):
    """
    Render the user's plot history as HTML.
    
    This function retrieves the user's plot history from cookies
    and formats it as HTML buttons with delete functionality for each item.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: An HTTP response containing the HTML representation of the user's plot history.
    """
    # Retrieve the user's plot history from cookies
    user_history = get_user_history(request)
    history_html = get_history_html(user_history)
    return HttpResponse(history_html)

@require_POST
@csrf_exempt
def delete_history_item(request):
    """
    Delete a specific item from the user's plot history.
    
    This function handles POST requests to delete a history item.
    It updates the user's history cookie after deletion.
    
    Inputs:
        request: The HTTP request object containing the index of the item to delete.
    
    Outputs:
        HttpResponse: A response containing the updated history HTML or an error message.
    """
        
    # Get the index of the item to delete from the POST data
    index = int(request.POST.get('index', -1))
    
    if index >= 0:
        # Retrieve the current user history
        user_history = get_user_history(request)
        
        # Check if the index is valid
        if 0 <= index < len(user_history):
            # Remove the item at the specified index
            del user_history[index]
            
            # Serialize the updated history
            serialized_data = pickle.dumps(user_history)
            
            if user_history:
                # If there are still items in the history, render them
                response = HttpResponse(get_history_html(user_history))
            else:
                # If the history is now empty, return a message
                response = HttpResponse('<p>No history available.</p>')
            
            # Update the user's history cookie
            response.set_cookie('user_history', serialized_data.hex(), max_age=30 * 24 * 60 * 60)
            
            return response
    
    # Return an error response if the request is invalid
    return error_400(request, "")


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
    
    # Fetch all available options for various parameters from the Translator
    datasets = Translator.get_all('dataset')

    # get rid of broken dataset
    try:
        datasets.remove("IEAEWEB2022")
    except:
        pass

    countries = Translator.get_all('country')
    countries.sort()
    versions = Translator.get_all('version')
    methods = Translator.get_all('method')
    energy_types = Translator.get_all('energytype')
    last_stages = Translator.get_all('laststage')
    ieamws = Translator.get_all('ieamw')
    grossnets = Translator.get_all('grossnet')
    product_aggregations = Translator.get_all('agglevel')
    industry_aggregations = Translator.get_all('agglevel')
    # Remove 'Both' from ieamws if present
    try:
        ieamws.remove("Both")
    except ValueError:
        pass # don't care if it's not there, we're trying to remove it anyways
    matnames = Translator.get_all('matname')
    matnames.sort(key=len)  # sort matrix names by how long they are... seems reasonable
    
    # Prepare the context dictionary for the template
    context = {
        "datasets":datasets, "versions":versions, "countries":countries, "methods":methods,
        "energy_types":energy_types, "last_stages":last_stages, "ieamws":ieamws, "grossnets":grossnets,
        "matnames":matnames, "product_aggregations":product_aggregations, "industry_aggregations":industry_aggregations,
        "iea":request.user.is_authenticated and request.user.has_perm("eviz.get_iea")
        }

    return render(request, "visualizer.html", context)

def about(request):
    ''' Render the 'About' page.'''
    LOGGER.info("About page visted.")
    return render(request, 'about.html')

def terms_and_conditions(request):
    ''' Render the 'Terms and Conditions' page.'''
    LOGGER.info("TOS page visted.")
    return render(request, 'terms_and_conditions.html')

def data_info(request):
    ''' Render the 'Data Information' page.'''
    LOGGER.info("Data info page visted.")
    # Retrieve all Dataset objects from the database
    datasets = Dataset.objects.all()
    return render(request, 'data_info.html', context = {"datasets":datasets})

def matrix_info(request):
    ''' Render the 'Matrix Information' page.'''
    LOGGER.info("Matrix info page visted.")
    # Retrieve all Dataset objects from the database
    matricies = matname.objects.all()
    return render(request, 'matrix_info.html', context = {"matricies":matricies})

def user_signup(request):
    """ Handle user signup process.

    This function manages both GET and POST requests for user signup.
    For POST requests, it processes the form, sends a verification email,
    and redirects to an explanation page.
    For GET requests, it displays the signup form.

    Inputs:
        request: The HTTP request object

    Outputs:
        Rendered HTML response, either the signup form or a verification explanation page
    """
    LOGGER.info("Signup page visted.")

    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = SignupForm(request.POST)
        if form.is_valid():
            
            # Extract the email from the cleaned form data
            new_user_email = form.cleaned_data.get("email")
            if new_user_email == None:
                return error_400(request, "No email in signup")

            LOGGER.info(f"{form.cleaned_data['username']} signed up for account w/ email {new_user_email}.")

            # handle the email construction and sending
            code = new_email_code(account_info = form.clean())
            url = f"https://mexer.site/verify?code={code}"
            msg = EmailMultiAlternatives(
                subject="New Mexer Account",
                body=f"Please visit the following link to verify your account:\n{url}",
                from_email="signup@mexer.site",
                to=[new_user_email]
            )
            # HTML message
            msg.attach_alternative(
                content = f"<p>Please <a href='{url}'>click here</a> to verify your new Mexer account!</p>",
                mimetype = "text/html"
            )
            
            # send the email and make sure it was successful
            # 0 is failure
            if msg.send() == 0:
                LOGGER.error(f"Couldn't send signup email to {new_user_email}")      
            else:
                LOGGER.info(f"Signup email sent to {new_user_email}.")

            # send the user to a page explaining what to do next (check email)
            return render(request, 'verify_explain.html')
    else:
        # If it's a GET request, create an empty form
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def verify_email(request):
    """ Verify a user's email address using a verification code.

    This function handles the email verification process when a user clicks
    the verification link sent to their email during signup.

    Inputs:
        request: The HTTP request object, expected to contain a 'code' parameter in GET

    Outputs:
        Redirects to the login page with a success or failure message
    """
    if request.method == "GET":
        # Extract the verification code from the GET parameters
        code = request.GET.get("code")

        new_user = None
        try: 
            new_user = EmailAuthCode.objects.get(code = code) # try to get associated user from code
        except Exception as e: 
            return error_400(request, e) # bad request, no new user found

        if new_user:
            # if there is an associated user, set up their account
            # load the serialized account info from the database and save it
            account_info = pickle.loads(new_user.account_info)
            SignupForm(account_info).save()
            new_user.delete() # get rid of row in database
            messages.add_message(request, messages.INFO, "Verification was successful!")
            LOGGER.info(f"{account_info.get('username')} account created.")
        else:
            messages.add_message(request, messages.INFO, "Bad verification code!")

    return redirect("login")

def user_login(request):
    """ Handle user login process.

    This function manages both GET and POST requests for user login.
    It handles cases where users are redirected to login from another page,
    as well as direct login attempts.

    Inputs:
        request: The HTTP request object

    Outputs:
        Rendered login page or redirect to appropriate page after successful login
    """
    LOGGER.info("Logon page visted.")
    
    # for if a user is stopped and asked to log in first
    if request.method == 'GET':
        # get where they were trying to go
        requested_url = request.GET.get("next")
        if requested_url:
            request.session['requested_url'] = requested_url
        form = LoginForm()

    # for if the user submitted their login form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extract username and password from the cleaned form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            # if user was successfully authenticated
            if user:
                login(request, user) # log the user in so they don't have to repeat authentication every time
                LOGGER.info(f"{user.username} logged on.")
                requested_url = request.session.get('requested_url')
                if requested_url: # if user was trying to go somewhere else originally
                    del request.session['requested_url']
                    return redirect(requested_url)
                # else just send them to the home page
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, "Username or password is incorrect!")
    else:
        form = LoginForm()
    
    # giving the normal login page
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    """ Handle user logout process. """
    LOGGER.info(f"{request.user.get_username()} logged off.")
    # Call Django's built-in logout function to log out the current user
    # This function removes the authenticated user's ID from the request and flushes their session data
    logout(request)
    return redirect('home')

def forgot_password(request):

    if request.method == "GET":
        # start the reset process
        return render(request, "reset.html") # page with form to get which user is requesting the reset

    elif request.method == "POST":
        # a user has submitted their username for a password reset
        # get the username given and try to send an email to the
        # account cooresponding inbox
        username: str = request.POST.get("username")

        try:
            user = EvizUser.objects.get_by_natural_key(username)
        except Exception as e:
            # bad request, no user found
            # simply ignore the rest of the process
            LOGGER.error(f"Reset requested for username {username}: {e}")
        else:
            # if a user was found for the given username
            # construct and send the email
            LOGGER.info(f"Sending password reset email for {username}")
            code = new_reset_code(user)
            url = f"https://mexer.site/reset-password?code={code}"
            msg = EmailMultiAlternatives(
                subject="Mexer Password Reset",
                body=f"Please visit the following link to reset your account:\n{url}",
                from_email="reset@mexer.site",
                to=[user.email]
            )

            # HTML message
            msg.attach_alternative(
                content = f"<p>Please <a href='{url}'>click here</a> to reset your Mexer password.</p>",
                mimetype = "text/html"
            )
            msg.send()
            LOGGER.info(f"Successfully sent password reset email for {username}")
        
        # NOTE: this is not in a final block because
        # django will not send any exceptions in the else
        # section to the terminal if there is a final block

        # send success and failure here
        # because we don't want to give away
        # whether accounts exist or not
        return render(request, "reset_explain.html")
        
def reset_password(request):
    
    if request.method == "GET":
        code = request.GET.get("code")
        return render(request, "reset-submit.html", context = {"code": code})
    
    elif request.method == "POST":
        ps1 = request.POST.get("password1")
        ps2 = request.POST.get("password2")
        code = request.POST.get("code")

        if not valid_passwords(ps1, ps2):
            # TODO: have more descriptive messages about why password(s) not valid
            messages.add_message(request, messages.ERROR, "Passwords not valid!")
            return render(request, "reset-submit.html", context = {"code": code})
        
        # try to get the user with the information provided
        try:
            pass_reset_row = PassResetCode.objects.get(code = code)
            user = pass_reset_row.user
        except Exception as e:
            # bad request, no user found
            return error_400(request, e)
        
        user.set_password(ps1)
        user.save()

        # if no errors getting the user,
        # delete the cooresponding row
        pass_reset_row.delete()

        return redirect("login")


# Static handling
from eviz_site.settings import STATIC_BASE
def handle_static(request, filepath):
    """Serve CSS static files directly from a specified directory.

    This function reads a CSS file from a static files directory
    and serves it as an HTTP response with the appropriate content type.

    Inputs:
        request: The HTTP request object (not used in this function, but typically included for view functions)
        filepath: The path to the CSS file relative to the static files directory

    Outputs:
        HttpResponse containing the contents of the CSS file
    """
    # example filepath: css/toolbar.css
    match(filepath.split("/")[0]):
        case "css":
            with open(f"{STATIC_BASE}/{filepath}", "rb") as f:
                return HttpResponse(f.read(), headers = {"Content-Type": "text/css"})
            
        case "images":
            with open(f"{STATIC_BASE}/{filepath}", "rb") as f:
                return HttpResponse(f.read(), headers = {"Content-Type": "image"})
            
        case "js":
            with open(f"{STATIC_BASE}/{filepath}", "rb") as f:
                return HttpResponse(f.read(), headers = {"Content-Type": "text/javascript"})
        
        case _:
            return error_404(request, "")

####################################################################
## Error pages
#####################

# TODO: log messages should be more descriptive
def error_400(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/400.html', status=400)

def error_403(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/403.html', status=403)

def error_404(request, exception: Exception | str):
        LOGGER.error(str(exception))
        return render(request, 'error_pages/404.html', status=404)

def error_500(request):
        return render(request, 'error_pages/500.html', status=500)

def csrf_failure(request, reason=""):
        return error_403(request, reason)