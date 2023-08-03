from rest_framework import generics
from rest_framework.pagination import PageNumberPagination as pnp
from django_filters.rest_framework import DjangoFilterBackend as dfb
from .models import Weather_detail, Statistics_detail
from .serializers import (
    WeatherDetailSerializers as wms,
    StatisticsDetailSerializers as sms,
)


class Weather_view(generics.ListAPIView):
    """
    @params: generics.ListAPIView
    @feature: Create Weather View Model
    @return: None
    """

    queryset = Weather_detail.objects.all().order_by("-date")
    serializer_class = wms
    pagination_class = pnp
    filter_backends = [dfb]
    filterset_fields = ["date", "station_name"]


class Statistics_view(generics.ListAPIView):
    """
    @params: generics.ListAPIView
    @feature: Create Statistics View Model
    @return: None
    """

    queryset = Statistics_detail.objects.all().order_by("-date")
    serializer_class = sms
    pagination_class = pnp
    filter_backends = [dfb]
    filterset_fields = ["date", "station_name"]
