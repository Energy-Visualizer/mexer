from django.urls import path, re_path

from . import views

urlpatterns = [
    path("psut_data", views.get_psut_data),
    path("visualizer", views.visualizer, name="visualizer"),
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('about/', views.about, name='about'),
    re_path(r"static/css/([^(\.css)]*\.css)", views.handle_css_static)
]