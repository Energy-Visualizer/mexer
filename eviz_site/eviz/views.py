from eviz.models import PSUT
from django.shortcuts import render
from eviz.utils import time_view, get_matrix, RUVY

def eviz_index(request):

    # Get 10 PSUT rows from db
    rows = PSUT.objects.values("Year", "i", "j", "x", "Country").filter(Country=155, Year__lt=2015)[:10]

    context = { "psut_rows": rows }

    return render(request, "./test.html", context)

@time_view
def _la_extraction(request):

    matrix = get_matrix(
        dataset=2,
        country=49,
        method=1,
        energy_type=2,
        last_stage=2,
        ieamw=1,
        includes_neu=1,
        year=2015,
        matrix_name=RUVY.R
    )

    value = matrix[2023, 10]
    
    context = { "value": value }

    return render(request, "./la_extract.html", context)