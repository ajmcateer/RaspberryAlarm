from PyQt5.QtCore import QObject, pyqtSignal
from forecastio.models import Forecast


class ForecastModel(QObject):
    forecast_changed = pyqtSignal(Forecast)

    @property
    def forecast(self):
        return self._forecast

    @forecast.setter
    def forecast(self, value):
        self._forecast = value
        self.forecast_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._forecast = None
