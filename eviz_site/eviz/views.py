from django.http import HttpResponse
from eviz.models import PSUT
from django.shortcuts import render
from django.db.models import Sum, Avg, Max
from eviz.utils import time_view
from django.core.cache import cache

@time_view
def eviz_index(request):
    
    rows = PSUT.objects.values("Year", "i", "j", "x", "Country").filter(Country=155, Year__lt=2015)[:10]
    
    context = {
        'psut_rows': rows
    }
    return render(request, "./test.html", context)
