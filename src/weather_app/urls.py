from django.urls import path, re_path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version="v1",
        description="Weather API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r"weather/", Weather_view.as_view(), name="weather-list"),
    path(r"weather/stats/", Statistics_view.as_view(), name="stats-list"),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
