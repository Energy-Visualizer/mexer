from django.urls import path

from . import views

urlpatterns = [
    path("", views.eviz_index, name="index")
]