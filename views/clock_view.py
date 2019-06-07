from base_classes.main_window_base import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from datetime import datetime
import qtmodern.styles
import qtmodern.windows
from models.alarm_model import AlarmModel
from PyQt5.QtCore import QTime, pyqtSlot
from json_storage import JsonStorage
from PyQt5.QtGui import QIcon, QPixmap


class AlarmClock(QtWidgets.QMainWindow, Ui_MainWindow):
    alarms = {}

    def __init__(self, model, controller):
        super(AlarmClock, self).__init__()

        self._model = model
        self._main_controller = controller

        self.setupUi(self)
        self.lvAlarmList.setVisible(False)
        self.btnAddAlarm.clicked.connect(self._main_controller.show_add_alarm_dialog)
        self.btnShowAlarms.clicked.connect(self.show_alarms)
        self._model.time_changed.connect(self.on_time_change)
        self._model.date_changed.connect(self.on_date_change)
        self._model.status_changed.connect(self.on_status_change)
        self._model.status_changed.connect(self.temp_changed)

        #self._model.temp_changed.connect(self.on_time_change)
        self._model.temp_ranged_changed.connect(self.on_temp_range_change)
        self.lblHiLow.setText(self._model.temp_range)
        self.lblCurrent.setText(self._model.current_temp)

        self.lvAlarmList.setModel(self._model.alarm_list)
        self.lvAlarmList.clicked.connect(self._main_controller.selection_changed)
        self.lblWeatherIcon.setScaledContents(True)
        self.lblWeatherIcon.setPixmap(QPixmap('resources\\weather_images\\na.png'))
        self.on_status_change(self._model.status)

    @pyqtSlot()
    def show_alarms(self):
        self.lvAlarmList.setVisible(not self.lvAlarmList.isVisible())

    @pyqtSlot(str)
    def on_time_change(self, value):
        self.lblTime.setText(value)

    @pyqtSlot(str)
    def temp_changed(self, value):
        self.lblCurrent.setText(value)

    @pyqtSlot(str)
    def on_status_change(self, value):
        qpix = QPixmap('resources\\weather_images\\na.png')
        if value == "Clouds":
            qpix = QPixmap('resources\\weather_images\\cloudy.png')
        elif value == "Haze":
            qpix = QPixmap('resources\\weather_images\\haze.png')
        elif value == "Clear":
            qpix = QPixmap('resources\\weather_images\\clear.png')
        elif value == "Thunderstorm":
            qpix = QPixmap('resources\\weather_images\\thunder_storm.png')
        elif value == "Drizzle":
            qpix = QPixmap('resources\\weather_images\\drizzle.png')
        elif value == "Rain":
            qpix = QPixmap('resources\\weather_images\\heavy_rain.png')
        elif value == "Snow":
            qpix = QPixmap('resources\\weather_images\\heavy_snow.png')
        elif value == "Snow":
            qpix = QPixmap('resources\\weather_images\\heavy_snow.png')

        self.lblWeatherIcon.setPixmap(qpix)

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
