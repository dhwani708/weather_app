from weather_app.models import Weather_detail, Statistics_detail
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class WeatherTestCase(APITestCase):
    """
    @params: APITestCase
    @feature: Test our Weather Endpoints
    @return: None
    """

    def test_fetch_weather_data_single_entry(self):
        """
        @params: None
        @feature: Test particular Weather Endpoint for a single entry: station_name="USC001106", date="20000101", max_temp=20, min_temp=19, precipitation=12
        @return: None
        """
        Weather_detail.objects.create(
            station_name="USC001106",
            date="20000101",
            max_temp=20,
            min_temp=19,
            precipitation=12,
        )
        response = self.client.get(reverse("weather-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)

    def test_fetch_weather_data_multiple_entries(self):
        """
        @params: None
        @feature: Test Weather Endpoint for multiple entries
        @return: None
        """
        Weather_detail.objects.create(
            station_name="USC001106",
            date="20000101",
            max_temp=20,
            min_temp=19,
            precipitation=12,
        )
        Weather_detail.objects.create(
            station_name="USC001107",
            date="20000102",
            max_temp=25,
            min_temp=18,
            precipitation=10,
        )
        response = self.client.get(reverse("weather-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 2)
        self.assertEqual(response.data["count"], 2)


class StatisticsTestCase(APITestCase):
    """
    @params: APITestCase
    @feature: Test our Statistics Endpoints
    @return: None
    """

    def test_fetch_statistics_data_single_entry(self):
        """
        @params: None
        @feature: Test particular Statistics Endpoint for a single entry: date='2000-01-01', station_name='Test Station', avg_max_temp=10.0, avg_min_temp=05.0, total_acc_ppt=05.0
        @return: None
        """
        Statistics_detail.objects.create(
            date="2000-01-01",
            station_name="Test Station",
            avg_max_temp=10.0,
            avg_min_temp=05.0,
            total_acc_ppt=05.0,
        )
        response = self.client.get(reverse("stats-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data["count"], 1)

    def test_fetch_statistics_data_multiple_entries(self):
        """
        @params: None
        @feature: Test Statistics Endpoint for multiple entries
        @return: None
        """
        Statistics_detail.objects.create(
            date="2000-01-01",
            station_name="Test Station 1",
            avg_max_temp=10.0,
            avg_min_temp=05.0,
            total_acc_ppt=05.0,
        )
        Statistics_detail.objects.create(
            date="2000-01-02",
            station_name="Test Station 2",
            avg_max_temp=15.0,
            avg_min_temp=06.0,
            total_acc_ppt=08.0,
        )
        response = self.client.get(reverse("stats-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 2)
        self.assertEqual(response.data["count"], 2)
