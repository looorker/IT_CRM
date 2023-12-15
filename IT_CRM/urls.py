from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("cli/", include("cli.urls")),
    path("admin/", admin.site.urls),
]