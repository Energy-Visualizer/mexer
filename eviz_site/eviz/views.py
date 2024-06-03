# Django imports
from django.shortcuts import render

# Eviz imports
from eviz.tests import test_matrix_sum
from eviz.utils import time_view, get_matrix, RUVY, Translator
from eviz.models import PSUT, AggEtaPFU

# Visualization imports
from plotly.offline import plot
import plotly.graph_objects as pgo

# TODO: this is temp
@time_view
def get_psut_data(request):
    
    dataset="CLPFUv2.0a1"
    country="GHA"
    method="PCM"
    energy_type="X"
    last_stage="Final"
    ieamw="IEA"
    includes_neu=True
    year=2015
    choppedmat = "None"
    choppedvar = "None"
    productaggregation = "Grouped"
    industryaggregation = "Despecified"
    mmatrix_name_r = RUVY.R
    matrix_name_u = RUVY.U
    matrix_name_v = RUVY.V
    matrix_name_y = RUVY.Y

    rows_r = (
        PSUT.objects
        .values("i", "j", "x")
        .filter(
            Dataset = Translator.dataset_translate(dataset),
            Country = Translator.country_translate(country),
            Method = Translator.method_translate(method),
            EnergyType = Translator.energytype_translate(energy_type),
            LastStage = Translator.laststage_translate(last_stage),
            IEAMW = Translator.ieamw_translate(ieamw),
            IncludesNEU = Translator.includesNEU_translate(includes_neu),
            Year = 2015,
            ChoppedMat = Translator.matname_translate(choppedmat),
            ChoppedVat = Translator.index_translate(choppedvar),
            ProductAggregation = Translator.productaggregation_translate(productaggregation),
            IndustryAggregation = Translator.productaggregation_translate(industryaggregation),
            matname = mmatrix_name_r.value
        )
    )

    rows_u = (
        PSUT.objects
        .values("i", "j", "x")
        .filter(
            Dataset=Translator.dataset_translate(dataset),
            Country=Translator.country_translate(country),
            Method=Translator.method_translate(method),
            EnergyType=Translator.energytype_translate(energy_type),
            LastStage=Translator.laststage_translate(last_stage),
            IEAMW=Translator.ieamw_translate(ieamw),
            IncludesNEU=Translator.includesNEU_translate(includes_neu),
            Year=year,
            ChoppedMat = Translator.matname_translate(choppedmat),
            ChoppedVat = Translator.index_translate(choppedvar),
            ProductAggregation = Translator.productaggregation_translate(productaggregation),
            IndustryAggregation = Translator.productaggregation_translate(industryaggregation),
            matname=matrix_name_u.value
        )
    )
    
    rows_v = (
        PSUT.objects
        .values("i", "j", "x")
        .filter(
            Dataset=Translator.dataset_translate(dataset),
            Country=Translator.country_translate(country),
            Method=Translator.method_translate(method),
            EnergyType=Translator.energytype_translate(energy_type),
            LastStage=Translator.laststage_translate(last_stage),
            IEAMW=Translator.ieamw_translate(ieamw),
            IncludesNEU=Translator.includesNEU_translate(includes_neu),
            Year=year,
            ChoppedMat = Translator.matname_translate(choppedmat),
            ChoppedVat = Translator.index_translate(choppedvar),
            ProductAggregation = Translator.productaggregation_translate(productaggregation),
            IndustryAggregation = Translator.productaggregation_translate(industryaggregation),
            matname=matrix_name_v.value
        )
    )
    
    rows_y = (
        PSUT.objects
        .values("i", "j", "x")
        .filter(
            Dataset=Translator.dataset_translate(dataset),
            Country=Translator.country_translate(country),
            Method=Translator.method_translate(method),
            EnergyType=Translator.energytype_translate(energy_type),
            LastStage=Translator.laststage_translate(last_stage),
            IEAMW=Translator.ieamw_translate(ieamw),
            IncludesNEU=Translator.includesNEU_translate(includes_neu),
            Year=year,
            ChoppedMat = Translator.matname_translate(choppedmat),
            ChoppedVat = Translator.index_translate(choppedvar),
            ProductAggregation = Translator.productaggregation_translate(productaggregation),
            IndustryAggregation = Translator.productaggregation_translate(industryaggregation),
            matname=matrix_name_y.value
        )
    )
    
    
    context = {  "psut_rows_r": rows_r,
               "psut_rows_u": rows_u,
               "psut_rows_v": rows_v,
               "psut_rows_y": rows_y,}

    return render(request, "./test.html", context)

# TODO: hide this test
@time_view
def la_extraction(request):

    mat_context = {
        "dataset":2, # CLPFU
        "country":49, # GHA
        "method":1, # PCM
        "energy_type":2, # X
        "last_stage":2, # Final
        "ieamw":1, # IEA
        "includes_neu":1, # True
        "year":2015
    }

    test_mat_context = {
        "dataset": "CLPFUv2.0a1",
        "country": "GHA",
        "method": "PCM",
        "energy_type": "E",
        "last_stage": "Final",
        "ieamw": "Both",
        "includes_neu": True,
        "year": 1995
    }

    u = get_matrix(
        **test_mat_context,
        matrix_name=RUVY.U
    )
    v = get_matrix(
        **test_mat_context,
        matrix_name=RUVY.V
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