from django.http import HttpResponse
from hello_world.models import PSUT
from django.shortcuts import render

# Hello world view
def hello_world_index(request):

    # Get 10 PSUT rows from db
    rows = PSUT.objects.all()[:10]

    context = { "psut_rows": rows }

    return render(request, "./test.html", context)