from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_psut_data, name="index"),
    path("extract/", views.la_extraction, name="extraction")
    
]