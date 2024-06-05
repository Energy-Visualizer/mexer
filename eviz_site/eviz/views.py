# Django imports
from django.shortcuts import render, redirect
from django.db import connection # for low-level psycopg2 connection. to access other db connections, import connections
from django.contrib.auth import authenticate, login, logout 

# Eviz imports
from eviz.utils import time_view, get_matrix, Silent
from eviz.models import AggEtaPFU
from eviz.forms import SignupForm, LoginForm

# Visualization imports
from plotly.offline import plot
import plotly.express as px
import pandas.io.sql as pd_sql

@time_view
def index(request):

    return render(request, "index.html", context={})


# TODO: this is temp
from random import choice
@time_view
def get_psut_data(request):
    
    query0 = dict(
        dataset = "CLPFUv2.0a2",
        country = "KEN",
        method = "PCM",
        energy_type = "E",
        last_stage = "Final",
        ieamw = "Both",
        includes_neu = False,
        year = 1985,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Specified",
        industry_aggregation = "Specified"
    )

    query1 = dict(
        dataset = "CLPFUv2.0a2",
        country = "FRA",
        method = "PCM",
        energy_type = "E",
        last_stage = "Useful",
        ieamw = "Both",
        includes_neu = False,
        year = 1985,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Despecified",
        industry_aggregation = "Despecified"
    )

    query2 = dict(
        dataset = "CLPFUv2.0a2",
        country = "LTU",
        method = "PCM",
        energy_type = "E",
        last_stage = "Useful",
        ieamw = "IEA",
        includes_neu = False,
        year = 2019,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Despecified",
        industry_aggregation = "Despecified"
    )

    query3 = dict(
        dataset = "CLPFUv2.0a2",
        country = "JAM",
        method = "PCM",
        energy_type = "X",
        last_stage = "Final",
        ieamw = "Both",
        includes_neu = False,
        year = 2002,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Grouped",
        industry_aggregation = "Despecified"
    )

    query4 = dict(
        dataset = "CLPFUv2.0a2",
        country = "UnDEU",
        method = "PCM",
        energy_type = "X",
        last_stage = "Useful",
        ieamw = "IEA",
        includes_neu = True,
        year = 1961,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Despecified",
        industry_aggregation = "Despecified"
    )

    query = choice([query0, query1, query2, query3, query4])

    rows_r = get_matrix(**query, matrix_name="R")

    rows_u = get_matrix(**query, matrix_name="U")
    
    rows_v = get_matrix(**query, matrix_name="V")
    
    rows_y = get_matrix(**query, matrix_name="Y")
    
    context = {
        "query": query,
        "r_mat": rows_r,
        "u_mat": rows_u,
        "v_mat": rows_v,
        "y_mat": rows_y,
    }

    return render(request, "./test.html", context)

# TODO: this is temp
@time_view
def temp_viz(request):

    agg_query = AggEtaPFU.objects.filter(
        Dataset = 3,
        Country = 5,
        Method = 1,
        EnergyType = 2,
        LastStage = 2,
        IEAMW = 1,
        IncludesNEU = 0,
        ChoppedMat = 28,
        ChoppedVar = 2728,
        ProductAggregation = 1,
        IndustryAggregation = 1,
        GrossNet = 1
    ).values("Year", "EXp", "EXf", "EXu", "etapf", "etafu", "etapu").query

    # TODO: pandas only defines support for SQLAlechemy connection, it currently works with psycopg2, but could be dangerous
    with Silent():
        df = pd_sql.read_sql_query(str(agg_query), con=connection.cursor().connection) # clunky, but gives access to the low-level psycopg2 connection

    scatterplot = px.scatter(
        df, x = "Year", y = "etapu",
        title="Efficiency of primary to useful by year for random query",
        template="plotly_dark"
    )
    
    # idea for visualization rendering from this site: https://www.codingwithricky.com/2019/08/28/easy-django-plotly/
    p = plot(scatterplot, output_type="div", include_plotlyjs="cdn")
    
    return render(request, "viz.html", context={"plot":p})

def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            instance =form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')