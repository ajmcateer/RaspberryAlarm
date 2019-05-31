from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime


class Clock(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, alarms: list):
        QThread.__init__(self)
        self.alarms = alarms

    # run method gets called when we start the thread
    def run(self):
        if self.alarms is None:
            return
        else:
            for alarm in self.alarms:
                if alarm.set_hour is datetime.now().hour and alarm.set_minute is datetime.now().minute:
                    print("ALARM")
