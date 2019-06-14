from base_classes.main_window_base import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from datetime import datetime
import qtmodern.styles
import qtmodern.windows
from models.alarm_model import AlarmModel
from PyQt5.QtCore import QTime, pyqtSlot
from json_storage import JsonStorage
from PyQt5.QtGui import QIcon, QPixmap
from forecastio.models import Forecast
from utils.icon_converter import convert_to_icon


class AlarmClock(QtWidgets.QMainWindow, Ui_MainWindow):
    alarms = {}

    def __init__(self, model, controller, forecast):
        super(AlarmClock, self).__init__()

        self._model = model
        self._forecast = forecast
        self._main_controller = controller

        self.setupUi(self)
        self.lvAlarmList.setVisible(False)
        self.btnAddAlarm.clicked.connect(self._main_controller.show_add_alarm_dialog)
        self.btnShowAlarms.clicked.connect(self.show_alarms)
        self._model.time_changed.connect(self.on_time_change)
        self._model.date_changed.connect(self.on_date_change)

        self._model.temp_ranged_changed.connect(self.on_temp_range_change)

        self.lvAlarmList.setModel(self._model.alarm_list)
        self.lvAlarmList.clicked.connect(self._main_controller.selection_changed)
        self.lblWeatherIcon.setScaledContents(True)
        self._forecast.forecast_changed.connect(self.forecast_changed)
        self.forecast_changed(self._forecast.forecast)

    @pyqtSlot(Forecast)
    def forecast_changed(self, forecast):
        self.lblWeatherIcon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[0].icon,
                                                            forecast.daily().data[0].moonPhase)))
        self.lblCurrent.setText(str(int(forecast.hourly().data[0].temperature)))
        self.lblHiLow.setText(f"Hi: {str(int(forecast.daily().data[0].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[0].temperatureLow))}")

        self.lblHour1Temp.setText(str(int(forecast.hourly().data[0].temperature)))
        self.lblHour1Icon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[0].icon,
                                                            forecast.daily().data[0].moonPhase)))
        self.lblHour1Time.setText(datetime.fromtimestamp(forecast.hourly().data[0].d["time"]).strftime('%I:%M:%S %p'))

        self.lblHour2Temp.setText(str(int(forecast.hourly().data[1].temperature)))
        self.lblHour2Icon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[1].icon,
                                                            forecast.daily().data[1].moonPhase)))
        self.lblHour2Time.setText(datetime.fromtimestamp(forecast.hourly().data[1].d["time"]).strftime('%I:%M:%S %p'))

        self.lblHour3Temp.setText(str(int(forecast.hourly().data[2].temperature)))
        self.lblHour3Icon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[2].icon,
                                                            forecast.daily().data[2].moonPhase)))
        self.lblHour3Time.setText(datetime.fromtimestamp(forecast.hourly().data[2].d["time"]).strftime('%I:%M:%S %p'))

        self.lblHour4Temp.setText(str(int(forecast.hourly().data[3].temperature)))
        self.lblHour4Icon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[3].icon,
                                                            forecast.daily().data[3].moonPhase)))
        self.lblHour4Time.setText(datetime.fromtimestamp(forecast.hourly().data[3].d["time"]).strftime('%I:%M:%S %p'))

        self.lblHour5Temp.setText(str(int(forecast.hourly().data[4].temperature)))
        self.lblHour5Icon.setPixmap(QPixmap(convert_to_icon(forecast.hourly().data[4].icon,
                                                            forecast.daily().data[4].moonPhase)))
        self.lblHour5Time.setText(datetime.fromtimestamp(forecast.hourly().data[4].d["time"]).strftime('%I:%M:%S %p'))

        self.lblDaily1Temp.setText(f"Hi: {str(int(forecast.daily().data[0].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[0].temperatureLow))}")
        self.lblDaily1Icon.setPixmap(QPixmap(convert_to_icon(forecast.daily().data[0].icon)))
        self.lblDaily1Time.setText(datetime.fromtimestamp(forecast.daily().data[0].d["time"]).strftime('%A'))

        self.lblDaily2Temp.setText(f"Hi: {str(int(forecast.daily().data[1].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[1].temperatureLow))}")
        self.lblDaily2Icon.setPixmap(QPixmap(convert_to_icon(forecast.daily().data[1].icon)))
        self.lblDaily2Time.setText(datetime.fromtimestamp(forecast.daily().data[1].d["time"]).strftime('%A'))

        self.lblDaily3Temp.setText(f"Hi: {str(int(forecast.daily().data[2].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[2].temperatureLow))}")
        self.lblDaily3Icon.setPixmap(QPixmap(convert_to_icon(forecast.daily().data[2].icon)))
        self.lblDaily3Time.setText(datetime.fromtimestamp(forecast.daily().data[2].d["time"]).strftime('%A'))

        self.lblDaily4Temp.setText(f"Hi: {str(int(forecast.daily().data[3].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[3].temperatureLow))}")
        self.lblDaily4Icon.setPixmap(QPixmap(convert_to_icon(forecast.daily().data[3].icon)))
        self.lblDaily4Time.setText(datetime.fromtimestamp(forecast.daily().data[3].d["time"]).strftime('%A'))

        self.lblDaily5Temp.setText(f"Hi: {str(int(forecast.daily().data[4].temperatureHigh))} | Low: "
                              f"{str(int(forecast.daily().data[4].temperatureLow))}")
        self.lblDaily5Icon.setPixmap(QPixmap(convert_to_icon(forecast.daily().data[4].icon)))
        self.lblDaily5Time.setText(datetime.fromtimestamp(forecast.daily().data[4].d["time"]).strftime('%A'))

    @pyqtSlot()
    def show_alarms(self):
        self.lvAlarmList.setVisible(not self.lvAlarmList.isVisible())

    @pyqtSlot(str)
    def on_time_change(self, value):
        self.lblTime.setText(value)

    @pyqtSlot(str)
    def on_temp_range_change(self, value):
        self.label.setText(value)

    @pyqtSlot(str)
    def on_date_change(self, value):
        self.lblDate.setText(value)

    @pyqtSlot(str)
    def on_name_change(self, value):
        self.txtName.setPlainText(value)

    @QtCore.pyqtSlot()
    def add_alarm(self):
        name = self.txtName.toPlainText()
        self.alarms[name] = (AlarmModel(name=name, set_hour=self.tAlarmTime.time().hour(),
                                        set_minute=self.tAlarmTime.time().minute()))

        self.lvAlarmList.addItem(name)

        JsonStorage.save(self, self.alarms)

    @QtCore.pyqtSlot()
    def delete_alarm(self):
        name = self.txtName.toPlainText()
        self.alarms.pop(name, None)
        items = self.lvAlarmList.selectedItems()
        for item in items:
            self.lvAlarmList.takeItem(self.lvAlarmList.row(item))
        self.txtName.setPlainText('')
        self.tAlarmTime.setTime(QTime(0, 0))

        JsonStorage.save(self, self.alarms)

    def read_alarms(self):
        self.alarms = JsonStorage.read(self)
        if self.alarms is not None:
            for k, v in self.alarms.items():
                self.lvAlarmList.addItem(k)

    def clock(self):
        self.lblTime.setText(datetime.now().strftime('%H:%M:%S'))
        self.lblDate.setText(datetime.now().strftime('%m-%d-%Y'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AlarmClock()
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())
