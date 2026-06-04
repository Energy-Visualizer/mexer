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
from django.conf import settings
from django.shortcuts import render
from Mexer.models import Dataset, Matname, Papers, Version
from Mexer.views import error_pages
from utils.logging import LOGGER
from utils.misc import time_view


@time_view
def index(request):
    """Render the home page."""

    LOGGER.info("Home page visted.")

    related_papers = Papers.objects.all().order_by("-year")
    return render(request, "index.html", context={"related_papers": related_papers})


def about(request):
    """Render the 'About' page."""
    LOGGER.info("About page visted.")
    return render(
        request, "about.html", context={"site_version": settings.SITE_VERSION}
    )


def plot_stage(request):
    """Give the plot stage, for plotting in a separate window"""
    return render(request, "plot_stage.html")


def terms_and_conditions(request):
    """Render the 'Terms and Conditions' page."""
    LOGGER.info("TOS page visted.")
    return render(request, "terms_and_conditions.html")


def data_info(request):
    """Render the 'Data Information' page."""
    LOGGER.info("Data info page visted.")
    # Retrieve all Dataset objects from the database
    datasets = Dataset.objects.all()
    public_versions = Version.objects.filter(public=True)
    return render(
        request,
        "data_info.html",
        context={"datasets": datasets, "public_versions": public_versions},
    )


def matrix_info(request):
    print("TEST PRINT", flush=True)

    """Render the 'Matrix Information' page."""
    LOGGER.info("Matrix info page visted.")
    # Retrieve all Dataset objects from the database
    matrices = Matname.objects.all()
    return render(request, "matrix_info.html", context={"matrices": matrices})


def __test_render_page(request, template_name: str):
    """Render a template that matches the path name from the request."""
    try:
        return render(request, template_name)
    except Exception as e:
        print(f"Error rendering template {template_name}: {e}")
        return error_pages.error_404(request, f"Template {template_name} not found.")
