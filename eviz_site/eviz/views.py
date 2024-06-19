# Django imports
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Eviz imports
from eviz.utils import *
from eviz.forms import SignupForm, LoginForm

# Visualization imports
from plotly.offline import plot

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

import plotly.graph_objects as go
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
import pickle
from datetime import datetime


def serialize_data(data):
    return pickle.dumps(data)

def deserialize_data(data):
    return pickle.loads(data)


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
        

            case _: # default
                plot_div = "Plot type not specified or supported"
        if plot_div:
            user_history = get_user_history(request)
            print("User history:", user_history)  # Add this print statement
            if not isinstance(user_history, list):
                user_history = [user_history]
            history_data = {
                'query': query,
                'plot_type': plot_type,
                'created_at': str(datetime.now())
            }
            print("History data:", history_data) 
            user_history.append(history_data)
            print("Updated user history:", user_history) 
            serialized_data = serialize_data(user_history)
            response = HttpResponse(plot_div)
            response.set_cookie('user_history', serialized_data.hex(), max_age=30*24*60*60) 
            return response
    
    return HttpResponse(plot_div)

@time_view
def render_history(request):
    user_history = get_user_history(request)
    return render(request, 'history_section.html', {'user_history': user_history})

def get_user_history(request):
    serialized_data = request.COOKIES.get('user_history')
    
    if serialized_data:
        user_history = deserialize_data(bytes.fromhex(serialized_data))
    else:
        user_history = []
    return user_history


#@login_required(login_url="/login")
@time_view
def visualizer(request):
    datasets = Translator.get_datasets()
    countries = Translator.get_countries()
    countries.sort()
    methods = Translator.get_methods()
    energy_types = Translator.get_energytypes()
    last_stages = Translator.get_laststages()
    ieamws = Translator.get_ieamws()
    matnames = Translator.get_matnames()
    matnames.sort(key=len) # sort matrix names by how long they are... seems reasonable
    context = {"datasets":datasets, "countries":countries, "methods":methods,
            "energy_types":energy_types, "last_stages":last_stages, "ieamws":ieamws, "matnames":matnames,
            }

    return render(request, "visualizer.html", context)

def is_iea(request):
    user = request.user
    iea=user.is_authenticated and user.has_perm("eviz.get_iea")
    context={"iea":iea}
    return render(request, "visualizer.html", context)

def about(request):
    return render(request, 'about.html')

def data_info(request):
    return render(request, 'data_info.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    # for if a user is stopped and asked to log in first
    if request.method == 'GET':
        # get where they were trying to go
        requested_url = request.GET.get("next", None)
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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, email=email, password=password)

            # if user was successfully authenticated
            if user:
                login(request, user)
                requested_url = request.session.get('requested_url')
                if requested_url: # if user was trying to go somewhere else originally
                    request.session['requested_url'] = None
                    return redirect(requested_url)
                # else just send them to the home page
                return redirect('home')
            # TODO: else show failure to log in page
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
    