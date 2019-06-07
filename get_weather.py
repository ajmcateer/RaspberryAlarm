import json
import pyowm
from PyQt5.QtCore import QTimer

class GetWeather():
    def __init__(self, model):
        self._model = model
        self.get_weather()
        self.weather_timer = QTimer()
        self.weather_timer.timeout.connect(self.get_weather)
        self.weather_timer.start(10800000)

    def get_weather(self):
        owm = pyowm.OWM('c66e6922d1f3479ff5baf9c794fbe933')
        observation = owm.weather_at_place("Harleysville, US")
        weather = observation.get_weather()
        self._model.current_temp = "Current: " + str(int(weather.get_temperature('fahrenheit')["temp"]))
        self._model.temp_range = "Hi: " + str(int(weather.get_temperature('fahrenheit')["temp_max"])) + " | Low: " + str(int(weather.get_temperature('fahrenheit')["temp_min"]))
        self._model.status = weather.get_status()
        print(weather.get_status())

        print("Done")


if __name__ == '__main__':
    test = GetWeather("")
    test.get_weather()
