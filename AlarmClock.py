from PyQt5.QtCore import pyqtSlot
from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTime, QThread
import threading
from datetime import datetime
from time import sleep
import qtmodern.styles
import qtmodern.windows
from Alarm import Alarm
from PyQt5.QtCore import QTimer, QTime
from AlarmChecker import AlarmChecker
import json


class AlarmClock(QtWidgets.QMainWindow, Ui_MainWindow):
    alarms = {}

    def __init__(self, parent=None):
        super(AlarmClock, self).__init__(parent)
        self.setupUi(self)
        self.btnSet.clicked.connect(self.add_alarm)
        self.lvAlarmList.itemClicked.connect(self.listwidgetclicked)

        self.read_alarms()
        self.timer = QTimer()
        self.timer.timeout.connect(self.clock)
        self.timer.start(1000)
        self.checker = AlarmChecker(self.alarms)
        #timer = threading.Timer(1.0, self.clock)
        #timer.start()

    def listwidgetclicked(self, item):
        item = item.text()
        self.txtName.setPlainText(item)
        time = QTime(self.alarms[item].set_hour, self.alarms[item].set_minute)
        self.tAlarmTime.setTime(time)

    @QtCore.pyqtSlot()
    def add_alarm(self):
        self.alarms[self.txtName.toPlainText()] = (Alarm(name=self.txtName.toPlainText(),
                                                         set_hour=self.tAlarmTime.time().hour(),
                                                         set_minute=self.tAlarmTime.time().minute()))

        try:
            with open("alarms.json", "w+") as f:
                alarm_list = []
                for k, v in self.alarms.items():
                    alarm_list.append(v.dict())
                f.write(json.dumps(alarm_list))
        except Exception as ex:
            print(str(ex))

    def read_alarms(self):
        import ast

        try:
            with open("alarms.json", 'r') as f:
                temp_alarms = ast.literal_eval(f.read())
                for alarm in temp_alarms:
                    self.alarms[alarm["name"]] = (Alarm(name=alarm["name"], set_hour=alarm["set_hour"],
                                                        set_minute=alarm["set_minute"]))
                    self.lvAlarmList.addItem(alarm["name"])
        except FileNotFoundError:
            print("Unable to load alarms.json")

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
