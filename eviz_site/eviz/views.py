# Django imports
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives # for email verification
from django.views.decorators.csrf import csrf_exempt

# Eviz imports
from eviz.utils import *
from eviz.forms import SignupForm, LoginForm
from eviz.logging import LOGGER

# Visualization imports
from plotly.offline import plot

@time_view
def index(request):
    LOGGER.info("Home page visted.")
    return render(request, "index.html")

@time_view
def get_data(request):
    # if user is not logged in their username is empty string
    # mark them as anonymous in the logs
    LOGGER.info(f"Data requested by {request.user.get_username() or "anonymous user"}")

    if request.method == "POST":
        
        # set up query and get csv from it
        query = shape_post_request(request.POST)

        if not iea_valid(request.user, query):
            LOGGER.warning(f"IEA data requested by unauthorized user {request.user.get_username() or "anonymous user"}")
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.", code=403)

        query = translate_query(query)

        csv = get_csv_from_query(query)

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
    # if user is not logged in their username is empty string
    # mark them as anonymous in the logs
    LOGGER.info(f"Plot requested by {request.user.get_username() or "anonymous user"}")

    plot_div = None
    if request.method == "POST":
        plot_type, query = shape_post_request(request.POST, get_plot_type = True)

        if not iea_valid(request.user, query):
            LOGGER.warning(f"IEA data requested by unauthorized user {request.user.get_username() or "anonymous user"}")
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.") # TODO: make this work with status = 403, problem is HTMX won't show anything
        
        match plot_type:
            case "sankey":
                query = translate_query(query)
                sankey_diagram = get_sankey(query)

                if sankey_diagram is None:
                    plot_div = "No cooresponding data"

                else:
                    sankey_diagram.update_layout(title_text="Test Sankey", font_size=10)
                    plot_div = plot(sankey_diagram, output_type="div", include_plotlyjs=False)
                    LOGGER.info("Sankey plot made")

            case "xy_plot":
                efficiency_metric = query.pop('efficiency')
                query = translate_query(query)
                xy = get_xy(efficiency_metric, query)

                if xy is None:
                    plot_div = "No corresponding data"
                else:
                    plot_div = plot(xy, output_type="div", include_plotlyjs=False)
                    LOGGER.info("XY plot made")

            case "matrices":
                matrix_name = query.get("matname")
                # Retrieve the matrix
                query = translate_query(query)
                matrix = get_matrix(query)
                
                if matrix is None:
                    plot_div = "No corresponding data"
                
                else:
                    heatmap= visualize_matrix(matrix)

                    heatmap.update_layout(
                        title = matrix_name + " Matrix",
                        yaxis = dict(title=''),
                        xaxis = dict(title=''),
                        xaxis_side = "top",
                        xaxis_tickangle = -45, 
                        scattermode = "overlay"
                        
                    )

                    # Render the figure as an HTML div
                    plot_div = plot(heatmap, output_type="div", include_plotlyjs="False")
                    LOGGER.info("Matrix visualization made")
        

            case _: # default
                plot_div = "Plot type not specified or supported"
                LOGGER.warning("Unrecognized plot type requested")
                
        response = HttpResponse(plot_div)
        
        plot_type, query = shape_post_request(request.POST, get_plot_type = True)
        serialized_data = update_user_history(request, plot_type, query)
        response.set_cookie('user_history', serialized_data.hex(), max_age=30 * 24 * 60 * 60)
            
    return response

from json import dumps as json_dumps
def render_history(request):
    user_history = get_user_history(request)
    history_html = ''
    if user_history:
        # This next line will destroy the queue, but we don't need it again
        for history_item in user_history:
            history_html += f'''
            <button type="button" hx-vals='{json_dumps(history_item)}' hx-indicator="#plot-spinner" hx-post="/plot" hx-target="#plot-section" hx-swap="innerHTML" onclick='document.getElementById("plot-section").scrollIntoView();' class="history-button">
                Plot Type: {history_item["plot_type"].capitalize()}<br>
                Dataset: {history_item["dataset"]}<br>
                Country: {history_item["country"]}
            </button><br><br>
            '''
    else:
        history_html = '<p>No history available.</p>'
    return HttpResponse(history_html)


@login_required(login_url="/login")
@time_view
def visualizer(request):
    LOGGER.info("Visualizer page visted.")
    datasets = Translator.get_all('dataset')
    countries = Translator.get_all('country')
    countries.sort()
    methods = Translator.get_all('method')
    energy_types = Translator.get_all('energytype')
    last_stages = Translator.get_all('laststage')
    ieamws = Translator.get_all('ieamw')
    try:
        ieamws.remove("Both")
    except ValueError:
        pass # don't care if it's not there, we're trying to remove it anyways
    matnames = Translator.get_all('matname')
    matnames.sort(key=len)  # sort matrix names by how long they are... seems reasonable
    
    context = {
        "datasets":datasets, "countries":countries, "methods":methods,
        "energy_types":energy_types, "last_stages":last_stages, "ieamws":ieamws,
        "matnames":matnames,
        "iea":request.user.is_authenticated and request.user.has_perm("eviz.get_iea")
        }

    return render(request, "visualizer.html", context)

def about(request):
    LOGGER.info("About page visted.")
    return render(request, 'about.html')

def terms_and_conditions(request):
    LOGGER.info("TOS page visted.")
    return render(request, 'terms_and_conditions.html')

def data_info(request):
    LOGGER.info("Data info page visted.")
    datasets = Dataset.objects.all()
    return render(request, 'data_info.html', context = {"datasets":datasets})

def user_signup(request):
    LOGGER.info("Signup page visted.")

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user_email = form.cleaned_data["email"]

            # handle the email construction and sending
            code = new_email_code(form)
            msg = EmailMultiAlternatives(
                subject="New EVIZ Account",
                body=f"Please visit the following link to verify your account:\neviz.cs.calvin.edu/verify?code={code}",
                from_email="eviz.site@outlook.com",
                to=[new_user_email]
            )
            msg.attach_alternative(
                content = f"<p>Please <a href='https://eviz.cs.calvin.edu/verify?code={code}'>click here</a> to verify your new account!</p>",
                mimetype = "text/html"
            )
            msg.send()

            LOGGER.info(f"{form.cleaned_data["username"]} signed up for account. Email sent to {new_user_email}. (Code: {code})")

            # send the user to a page explaining what to do next (check email)
            return render(request, 'verify_explain.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from pickle import loads as pickle_loads
def verify_email(request):
    if request.method == "GET":
        code = request.GET.get("code")
        new_user = EmailAuthCodes.objects.get(code = code) # try to get associated user from code
        if new_user:
            # if there is an associated user, set up their account
            # load the serialized account info from the database and save it
            account_info = pickle_loads(new_user.account_info)
            SignupForm(account_info).save()
            new_user.delete() # get rid of row in database
            messages.add_message(request, messages.INFO, "Verification was successful!")
            LOGGER.info(f"{account_info.get("username")} account created.")
        else:
            messages.add_message(request, messages.INFO, "Bad verification code!")

    return redirect("login")

def user_login(request):
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
    LOGGER.info(f"{request.user.get_username()} logged off.")
    logout(request)
    return redirect('home')


# Static handling
from django.conf import settings
def handle_css_static(request, filepath):
    with open(f"{settings.STATICFILES_DIRS[1]}/{filepath}", "rb") as f:
        return HttpResponse(f.read(), headers = {"Content-Type": "text/css"})
    