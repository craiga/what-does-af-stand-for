"""URL configuration"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

import debug_toolbar

from what_does_af_stand_for import views

urlpatterns = [
    path("", views.FrontPageView.as_view(), name="front_page"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
