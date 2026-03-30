from django.conf import settings
from django.urls import path, re_path

import Mexer.views.history as history_views
import Mexer.views.misc as misc_views
import Mexer.views.user_accounts as accounts_views
import Mexer.views.visualizer as visualizer_views

# build url patterns
__urlpatterns = [
    # main pages
    path("", misc_views.index, name="home"),
    path("visualizer/", visualizer_views.visualizer, name="visualizer"),
    # user accounts management pages
    path("login/", accounts_views.user_login, name="login"),
    path("signup/", accounts_views.user_signup, name="signup"),
    path("logout/", accounts_views.user_logout, name="logout"),
    path("forgot-password", accounts_views.forgot_password, name="forgot_password"),
    path("reset-password", accounts_views.reset_password, name="reset_password"),
    path("verify", accounts_views.verify_email),
    # visualizer tool pages
    path("plot", visualizer_views.get_plot),
    path("data", visualizer_views.get_data),
    # history tool pages
    path("history", history_views.render_history),
    path(
        "delete-history-item/",
        history_views.delete_history_item,
        name="delete_history_item",
    ),
    # misc pages
    path("about/", misc_views.about, name="about"),
    path(
        "terms_and_conditions/",
        misc_views.terms_and_conditions,
        name="terms_and_conditions",
    ),
    path("data-info/", misc_views.data_info, name="data-info"),
    path("matrix-info/", misc_views.matrix_info, name="matrix-info"),
    path("plot-stage/", misc_views.plot_stage),
]

# append testing routes
if settings.DEBUG:
    __urlpatterns.append(re_path(r"test_render/(.*)", misc_views.__test_render_page))

    # TODO: configure a static route in Nginx and remove whitenoise.
    # __urlpatterns += static(
    #     settings.STATIC_URL,
    #     document_root=settings.STATICFILES_DIRS[0],
    # )

# apply, "urlpatterns" is what Django will be given
urlpatterns = __urlpatterns
