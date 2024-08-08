####################################################################
# misc.py includes all miscellaneous views for Mexer
# 
# Most pages are simply delivering static HTML
# Some make short queries to the database to display
# information like the Databases available
#
# The static handling view is also included in this file
# 
# Authors:
#       Kenny Howes - kmh67@calvin.edu
#       Edom Maru - eam43@calvin.edu 
#####################
from utils.misc import time_view
from utils.logging import LOGGER
from django.shortcuts import render
from eviz.models import Dataset, matname
from eviz.views.error_pages import *
from django.http import HttpResponse


@time_view
def index(request):
    '''Render the home page.'''

    LOGGER.info("Home page visted.")
    return render(request, "index.html")

def about(request):
    ''' Render the 'About' page.'''
    LOGGER.info("About page visted.")
    return render(request, 'about.html')

def plot_stage(request):
    ''' Give the plot stage, for plotting in a separate window '''
    return render(request, 'plot_stage.html')

def terms_and_conditions(request):
    ''' Render the 'Terms and Conditions' page.'''
    LOGGER.info("TOS page visted.")
    return render(request, 'terms_and_conditions.html')

def data_info(request):
    ''' Render the 'Data Information' page.'''
    LOGGER.info("Data info page visted.")
    # Retrieve all Dataset objects from the database
    datasets = Dataset.objects.all()
    return render(request, 'data_info.html', context = {"datasets":datasets})

def matrix_info(request):
    ''' Render the 'Matrix Information' page.'''
    LOGGER.info("Matrix info page visted.")
    # Retrieve all Dataset objects from the database
    matricies = matname.objects.all()
    return render(request, 'matrix_info.html', context = {"matricies":matricies})

from eviz_site.settings import STATIC_BASE
def handle_static(request, filepath):
    """Serve CSS static files directly from a specified directory.

    This function reads a CSS file from a static files directory
    and serves it as an HTTP response with the appropriate content type.

    Inputs:
        request: The HTTP request object (not used in this function, but typically included for view functions)
        filepath: The path to the CSS file relative to the static files directory

    Outputs:
        HttpResponse containing the contents of the CSS file
    """
    # example filepath: css/toolbar.css OR admin/css/toolbar.css
    
    # the type of static file to serve is used in the match case
    # so that the correct mime type is attached
    # other than that, the whole filepath asked for (besides static/) is used to find the file
    file_type = filepath.split("/")[0] if filepath.split("/")[0] != "admin" else filepath.split("/")[1]
    match(file_type):
        case "css":
            mime_type = "text/css"
        
        case "images" | "img":
            mime_type = "image"
            
        case "js":
            mime_type = "text/javascript"
        
        case _:
            return error_404(request, f"Couldn't figure out content type of {filepath}")
    
    try:
        with open(f"{STATIC_BASE}/{filepath}", "rb") as f:
                return HttpResponse(f.read(), headers = {"Content-Type": mime_type})
    except Exception as e:
        return error_404(request, e)