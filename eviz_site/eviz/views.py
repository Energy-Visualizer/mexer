from eviz.models import PSUT
from django.shortcuts import render
from eviz.utils import time_view, get_matrix, RUVY, IndexTranslator
from django.core.cache import cache

@time_view
def eviz_index(request):

    rows = (
        PSUT.objects
        .values("i", "j", "x")
        .filter(
            Dataset = 2,
            Country = 49,
            Method = 1,
            EnergyType = 2,
            LastStage = 2,
            IEAMW = 1,
            IncludesNEU = 1,
            Year = 2015,
            matname = RUVY.R.value
        )
    )

    context = { "psut_rows": rows }

    return render(request, "./test.html", context)

def test_matrix_sum(m):
    
    assert(m.size == 23)
    assert(int(IndexTranslator.translate(m, "Charcoal", "Charcoal production plants")) == 16108)

    return "Passed all tests"

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
    print(sum)

    product = u * v
    # print(product)

    context = { "value": test_matrix_sum(sum) }

    return render(request, "./la_extract.html", context)
