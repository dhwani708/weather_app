from django.contrib import admin as weather_administrator
from django.urls import path, include

urlpatterns = [
    path("admin/", weather_administrator.site.urls),
    path("api/", include("weather_app.urls")),
]
