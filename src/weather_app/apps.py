from django.apps import AppConfig


class WeatherAppConfig(AppConfig):
    """
    @params: AppConfig
    @feature: Create Weather Application - weather_app
    @return: None
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "weather_app"
