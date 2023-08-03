from rest_framework import serializers
from .models import Weather_detail, Statistics_detail


class WeatherDetailSerializers(serializers.ModelSerializer):
    """
    @params: serializers.ModelSerializer
    @feature: Create Serializers for Weather Module
    @return: None
    """

    class Meta:
        model = Weather_detail
        fields = ["date", "max_temp", "min_temp", "precipitation", "station_name"]


class StatisticsDetailSerializers(serializers.ModelSerializer):
    """
    @params: serializers.ModelSerializer
    @feature: Create Serializers for Statistics Module
    @return: None
    """

    class Meta:
        model = Statistics_detail
        fields = [
            "date",
            "total_acc_ppt",
            "avg_min_temp",
            "avg_max_temp",
            "station_name",
        ]
