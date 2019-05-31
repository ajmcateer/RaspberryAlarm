from datetime import datetime
from PyQt5.QtCore import QTimer


class AlarmChecker():

    def __init__(self, alarm_dict):
        self.alarm_dict = alarm_dict
        self.alarm()
        self.alarm_timer = QTimer()
        self.alarm_timer.timeout.connect(self.alarm)
        self.alarm_timer.start(60000)

    def alarm(self):
        if not self.alarm_dict:
            return
        else:
            for k, v in self.alarm_dict.items():
                if v.set_hour is datetime.now().hour and v.set_minute is datetime.now().minute:
                    print("ALARM: " + v.name + " fired")
