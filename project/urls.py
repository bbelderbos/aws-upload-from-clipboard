from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("files.urls", namespace="files")),
    path("admin/", admin.site.urls),

]
