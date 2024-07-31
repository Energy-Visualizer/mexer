from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/images/favicon.png', permanent=True)

urlpatterns = [
    # main pages
    path('', views.index, name='home'),
    path("visualizer/", views.visualizer, name="visualizer"),

    # auth related pages
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path("forgot-password", views.forgot_password, name="forgot_password"),
    path("reset-password", views.reset_password, name="reset_password"),

    # misc pages
    path('about/', views.about, name='about'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('data-info/', views.data_info, name="data-info"),
    path('matrix-info/', views.matrix_info, name="matrix-info"),
    re_path(r"static/(.*/[^(\.)]*\..*)", views.handle_static),
    path("favicon.ico", favicon_view),
    path("plot-stage/", views.plot_stage),
    

    # api services
    path("plot", views.get_plot),
    path("data", views.get_data),
    path("verify", views.verify_email),
    path("history", views.render_history),
    path('delete-history-item/', views.delete_history_item, name='delete_history_item'),
]