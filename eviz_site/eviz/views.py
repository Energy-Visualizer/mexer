from eviz.models import PSUT
from django.shortcuts import render
from eviz.tests import test_matrix_sum
from eviz.utils import time_view, get_matrix, RUVY, Translator
from django.core.cache import cache

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
            matname=matrix_name_y.value
        )
    )
    
    
    context = {  "psut_rows_r": rows_r,
               "psut_rows_u": rows_u,
               "psut_rows_v": rows_v,
               "psut_rows_y": rows_y,}

    return render(request, "./test.html", context)

@time_view
def _la_extraction(request):

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
        "dataset":2, # CLPFU
        "country":49, # GHA
        "method":1, # PCM
        "energy_type":1, # E
        "last_stage":2, # Final
        "ieamw":3, # Both
        "includes_neu":1, # True
        "year":1995
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
