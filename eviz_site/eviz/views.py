# Django imports
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail # for email verification

# Eviz imports
from eviz.utils import *
from eviz.forms import SignupForm, LoginForm

# Visualization imports
from plotly.offline import plot

# Misc imports
from random import randint

@time_view
def index(request):
    return render(request, "index.html")

@time_view
def get_data(request):
    if request.method == "POST":
        
        # set up query and get csv from it
        query = shape_post_request(request.POST)

        if not iea_valid(request.user, query):
            return HttpResponse("You do not have access to IEA data.") # TODO: make this work with status = 403, problem is HTMX won't show anything

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

        # TODO: excel downloads
        # MIME for workbook is application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
        # file handle is xlsx for workbook 

    return final_response

@time_view
def get_plot(request):

    plot_div = None
    if request.method == "POST":

        plot_type, query = shape_post_request(request.POST, get_plot_type = True)

        if not iea_valid(request.user, query):
            return HttpResponse("You do not have access to IEA data. Please contact <a style='color: #00adb5' :visited='{color: #87CEEB}' href='mailto:matthew.heun@calvin.edu'>matthew.heun@calvin.edu</a> with questions."
                                "You can also purchase WEB data at <a style='color: #00adb5':visited='{color: #87CEEB}' href='https://www.iea.org/data-and-statistics/data-product/world-energy-balances'> World Energy Balances</a>.") # TODO: make this work with status = 403, problem is HTMX won't show anything
        
        match plot_type:
            case "sankey":
                query = translate_query(query)
                sankey_diagram = get_sankey(query)

                if sankey_diagram == None:
                    plot_div = "No cooresponding data"

                else:
                    sankey_diagram.update_layout(title_text="Test Sankey", font_size=10)
                    plot_div = plot(sankey_diagram, output_type="div", include_plotlyjs=False)

                    # add the reset button and start up the plot panning and zomming
                    plot_div += '<button id="plot-reset" onclick="initPlotUtils()">RESET</button>' + '<script>initPlotUtils()</script>'

            case "xy_plot":
                efficiency_metric = query.pop('efficiency')
                query = translate_query(query)
                xy = get_xy(efficiency_metric, query)
                plot_div = plot(xy, output_type="div", include_plotlyjs=False)

            case "matrices":
                matrix_name = query.get("matname")
                # Retrieve the matrix
                query = translate_query(query)
                matrix = get_matrix(query)

                if matrix is None:
                    plot_div = "No corresponding data"
                
                else:
                    heatmap = visualize_matrix(matrix)

                    heatmap.update_layout(
                        title = matrix_name + " Matrix",
                        yaxis = dict(title=''),
                        xaxis = dict(title=''),
                        xaxis_side = "top",
                        xaxis_tickangle = -45
                    )

                    # Render the figure as an HTML div
                    plot_div = plot(heatmap, output_type="div", include_plotlyjs="False")

            case _: # default
                plot_div = "Plot type not specified or supported"
    
    return HttpResponse(plot_div)

@login_required(login_url="/login")
@time_view
def visualizer(request):
    datasets = Translator.get_datasets()
    countries = Translator.get_countries()
    countries.sort()
    methods = Translator.get_methods()
    energy_types = Translator.get_energytypes()
    last_stages = Translator.get_laststages()
    ieamws = Translator.get_ieamws()
    ieamws.remove("Both") # TODO: this should be less hard coded
    matnames = Translator.get_matnames()
    matnames.sort(key=len) # sort matrix names by how long they are... seems reasonable
    
    context = {"datasets":datasets, "countries":countries, "methods":methods,
            "energy_types":energy_types, "last_stages":last_stages, "ieamws":ieamws, "matnames":matnames
            }

    return render(request, "visualizer.html", context)

def about(request):
    return render(request, 'about.html')

def data_info(request):
    datasets = Dataset.objects.all()
    return render(request, 'data_info.html', context = {"datasets":datasets})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user_email = form.cleaned_data["email"]
            print(new_user_email)
            new_user = form.save()
            # immediately deactivate account until their email is authenticated
            new_user.is_active = False
            new_user.save()

            # handle the email construction and sending
            code = new_email_code(new_user)

            send_mail(
                subject="New EVIZ Account",
                # TODO: change this to actual eviz site
                message=f"localhost:8000/verify?code={str(code)}",
                from_email="eviz@eviz.com",
                recipient_list=[new_user_email]
            )
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

email_auth_codes: dict[int, User] = dict[int, User]()
def new_email_code(user: User) -> int:
    code = randint(1000000000, 9999999999)
    email_auth_codes[code] = user
    return code

def verify_email(request):
    if request.method == "GET":
        code = int(request.GET.get("code"))
        new_user = email_auth_codes.get(code)
        # TODO: getting user object is good, code doesn't execute the following
        if new_user != None:
            new_user.is_active = True
            del email_auth_codes[code]

    return redirect("login")


def user_login(request):
    # for if a user is stopped and asked to log in first
    if request.method == 'GET':
        # get where they were trying to go
        requested_url = request.GET.get("next")
        if requested_url:
            request.session['requested_url'] = requested_url
        else:
            request.session['requested_url'] = None
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
    logout(request)
    return redirect('login')


# Static handling
from django.conf import settings
def handle_css_static(request, filepath):
    with open(f"{settings.STATICFILES_DIRS[1]}/{filepath}", "rb") as f:
        return HttpResponse(f.read(), headers = {"Content-Type": "text/css"})