from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("psut_data", views.get_psut_data),
    path("viz", views.temp_viz),
]