import forecastio
import datetime
from models.forecast_model import ForecastModel
from PyQt5.QtCore import QTimer
import requests.exceptions
import datetime


class GetWeather():
    def __init__(self, model, forecast):
        self._model = model
        self._forecast = forecast
        self.get_weather()
        self.weather_timer = QTimer()
        self.weather_timer.timeout.connect(self.get_weather)
        self.weather_timer.start(10800000)

    def get_weather(self):
        api_key = "b7ebaabda1d703f09e0684cdcfabf231"
        lat = 40.2363
        lng = -75.296

        try:
            forecast = forecastio.load_forecast(api_key, lat, lng, units="us")
        except ConnectionError as e:
            print("Error: " + e)
            return
        self._forecast.forecast = forecast