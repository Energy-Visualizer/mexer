# Django imports
from django.shortcuts import render
from django.db import connection # for low-level psycopg2 connection. to access other db connections, import connections

# Eviz imports
from eviz.utils import time_view, get_matrix, Silent
from eviz.models import AggEtaPFU

# Visualization imports
from plotly.offline import plot
import plotly.express as px
import pandas.io.sql as pd_sql

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