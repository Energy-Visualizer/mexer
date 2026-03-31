"""
URL configuration for Mexer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import Mexer.views.error_pages as error_pages
from django.contrib import admin
from django.urls import include, path

handler400 = error_pages.error_400
handler403 = error_pages.error_403
handler404 = error_pages.error_404
handler500 = error_pages.error_500

# change small visuals on the admin site
admin.site.site_header = "Mexer Admin"
admin.site.site_title = "Mexer Admin Portal"
admin.site.index_title = "Mexer Admin"

urlpatterns = [
    path("", include("Mexer.urls")),
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
]
