from django.db import models


class Weather_detail(models.Model):
    """
    @params: models.Model
    @feature: Create Weather Django DB Model
    @return: None
    """

    date = models.CharField(max_length=25)
    precipitation = models.IntegerField()
    station_name = models.CharField(max_length=25)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()

    class Meta:
        unique_together = ("date", "station_name")


class Statistics_detail(models.Model):
    """
    @params: models.Model
    @feature: Create Statistics Django DB Model
    @return: None
    """

    avg_max_temp = models.IntegerField()
    avg_min_temp = models.IntegerField()
    date = models.CharField(max_length=20)
    station_name = models.CharField(max_length=25)
    total_acc_ppt = models.IntegerField()

    class Meta:
        unique_together = ("date", "station_name")
