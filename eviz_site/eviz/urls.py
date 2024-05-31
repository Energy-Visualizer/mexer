from django.urls import path

from . import views

urlpatterns = [
    path("", views.eviz_index, name="index"),
    path("extract/", views._la_extraction, name="extraction")
]