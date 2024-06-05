from django.urls import path

from . import views

urlpatterns = [
    path("psut_data", views.get_psut_data),
    path("viz", views.temp_viz),
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout')
]