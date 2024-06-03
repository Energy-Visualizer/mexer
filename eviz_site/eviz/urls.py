from django.urls import path

from . import views

urlpatterns = [
    path("extract/", views.la_extraction, name="extraction"),
    path("", views.get_psut_data, name="index")
]