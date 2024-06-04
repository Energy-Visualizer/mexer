from django.urls import path

from . import views

urlpatterns = [
    # path("extract/", views.la_extraction, name="extraction"),
    # path("", views.get_psut_data, name="index"),
    # path("viz", views.temp_viz, name="index"),
    # path("register/", views.account, name="register"),
    # path("sign_up/", views.signup, name="sign_up")
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]