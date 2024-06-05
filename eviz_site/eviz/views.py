# Django imports
from django.shortcuts import render, redirect

# Eviz imports
from eviz.tests import test_matrix_sum
from eviz.utils import time_view, get_matrix, Translator
from eviz.models import PSUT, AggEtaPFU
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm

# Visualization imports
from plotly.offline import plot
import plotly.graph_objects as pgo

# TODO: this is temp
@time_view
def get_psut_data(request):
    
    query = dict(
        dataset="CLPFUv2.0a2",
        country="BGR",
        method="PCM",
        energy_type="X",
        last_stage="Useful",
        ieamw="IEA",
        includes_neu=True,
        year=2016,
        chopped_mat = "None",
        chopped_var = "None",
        product_aggregation = "Grouped",
        industry_aggregation = "Despecified"
    )

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

# TODO: hide this test
@time_view
def la_extraction(request):

    # TODO: broken after moving to a2
    test_mat_context = {
        "dataset": "CLPFUv2.0a1",
        "country": "GHA",
        "method": "PCM",
        "energy_type": "E",
        "last_stage": "Final",
        "ieamw": "Both",
        "includes_neu": True,
        "year": 1995,
    }

    u = get_matrix(
        **test_mat_context
    )
    v = get_matrix(
        **test_mat_context
    )

    sum = u.T + v

    s = str(sum).splitlines()

    context = { "passed": test_matrix_sum(sum), "sum": s }

    return render(request, "./la_extract.html", context)

# TODO: this is temp
@time_view
def temp_viz(request):

    # REQUIRES ALPHA 2!

    agg_data = AggEtaPFU.objects.filter(
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
    ).values_list("Year", "EXp", "EXf", "EXu", "etapf", "etafu", "etapu")

    year, exp, exf, exu, etapf, etafu, etapu = zip(*agg_data)

    scatterplot = pgo.Scatter(x=year,y=etapu)
    
    # idea for visualization rendering from this site: https://www.codingwithricky.com/2019/08/28/easy-django-plotly/
    p = plot([scatterplot], output_type="div", include_plotlyjs="cdn")
    
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

# def account(request):
#     user = User.objects.db_manager('users').create_user(username="username", password="password", email="email", first_name="first_name", last_name="last_name")
#     user.save(using='users')
#     new_user=User.objects.values("email")
#     return render(request, "register.html", context={"new_user": new_user})