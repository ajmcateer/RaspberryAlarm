from PyQt5.QtCore import QObject, pyqtSlot, QTimer, QTime, QModelIndex
from datetime import datetime
from models.alarm_model import AlarmModel
from views.add_alarm_view import AddAlarm
from alarm_checker import AlarmChecker
from json_storage import JsonStorage
from get_weather import GetWeather


class ClockController(QObject):
    def __init__(self, model, forecast):
        super().__init__()

        self._model = model
        self._forecast = forecast
        self.timer = QTimer()
        self.json_storage = JsonStorage("")
        self.load_alarms()
        self.timer.timeout.connect(self.clock)
        self.timer.start(1000)
        self.checker = AlarmChecker(self._model.alarms)
        self.weather = GetWeather(self._model, self._forecast)
        print(self._model.temp)

    @pyqtSlot(int)
    def add_alarm(self):
        new_alarm = AlarmModel(self._model.name, self._model.hour, self._model.minute)
        self._model.alarms = new_alarm
        self.json_storage.save(self._model.alarms)

    @pyqtSlot(int)
    def name_changed(self, value):
        self._model.name = value

    @pyqtSlot(QTime)
    def alarm_time_changed(self, value):
        self._model.hour = value.hour()
        self._model.minute = value.minute()

    @pyqtSlot(str)
    def change_time(self, value):
        self._model.time = value

    @pyqtSlot(str)
    def change_date(self, value):
        self._model.date = value

    @pyqtSlot(QModelIndex)
    def selection_changed(self, value):
        name = self._model.alarms[value.data()].name
        ret = AddAlarm(alarm_clock=self._model.alarms[name])
        res = ret.exec()
        if ret.delete:
            self._model.alarms.pop(name)
            for item in self._model.alarm_list.findItems(name):
                self._model.alarm_list.removeRow(item.row())
            self.json_storage.save(self._model.alarms)
        if res != 0:
            self.set_alarm_model(ret.alarm)

    @pyqtSlot()
    def show_add_alarm_dialog(self):
        ret = AddAlarm()
        if ret.exec():
            self.set_alarm_model(ret.alarm)

    def load_alarms(self):
        alarm_list = self.json_storage.read()
        for alarm in alarm_list:
            self._model.alarms = alarm

    def set_alarm_model(self, alarm):
        self._model.alarms = alarm
        self.json_storage.save(self._model.alarms)

    def clock(self):
        self._model.time = datetime.now().strftime('%I:%M:%S %p')
        self._model.date = datetime.now().strftime('%m-%d-%Y')
