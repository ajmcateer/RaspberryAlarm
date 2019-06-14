from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class ClockModel(QObject):
    time_changed = pyqtSignal(str)
    date_changed = pyqtSignal(str)
    temp_changed = pyqtSignal(str)
    temp_ranged_changed = pyqtSignal(str)
    status_changed = pyqtSignal(str)
    hour_changed = pyqtSignal(int)
    minute_changed = pyqtSignal(int)
    list_changed = pyqtSignal(QStandardItemModel)

    @property
    def forecast_object(self):
        return self._forecast_object

    @forecast_object.setter
    def forecast_object(self, value):
        self._forecast_object = value
        self.forecast_object_changed.emit(value)

    @property
    def current_temp(self):
        return self._current_temp

    @current_temp.setter
    def current_temp(self, value):
        self._current_temp = value
        self.temp_changed.emit(value)

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value
        self.hour_changed.emit(value)

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        self._minute = value
        self.minute_changed.emit(value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        self.status_changed.emit(value)

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value
        self.temp_changed.emit(value)

    @property
    def temp_range(self):
        return self._temp_range

    @temp_range.setter
    def temp_range(self, value):
        self._temp_range = value
        self.temp_ranged_changed.emit(value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
        self.time_changed.emit(value)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
        self.date_changed.emit(value)

    @property
    def alarms(self):
        return self._alarms

    @alarms.setter
    def alarms(self, value):
        self._alarms[value.name] = value
        #if value.name not in self._alarm_list:
        exists = False
        for index in range(self._alarm_list.rowCount()):
            item = self._alarm_list.item(index)
            text = item.text()
            if text == value.name:
                exists = True

        if not exists:
            self._alarm_list.appendRow(QStandardItem(value.name))

    @property
    def alarm_list(self):
        return self._alarm_list

    @alarm_list.setter
    def alarm_list(self, value):
        self._alarm_list.appendRow(QStandardItem(value))

    def __init__(self):
        super().__init__()

        self._time = ''
        self._date = ''
        self._name = ''
        self._hour = 0
        self._minute = 0
        self._alarms = {}
        self._alarm_list = QStandardItemModel()
        self._temp = ""
        self._temp_range = ""
        self._status = ""
        self._current_temp = ""
        self._forecast_object = None
