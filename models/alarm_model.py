from PyQt5.QtCore import QTime


class AlarmModel:
    name = ""
    set_hour = ""
    set_minute = ""

    def __init__(self, name: str, set_hour, set_minute):
        self.name = name
        self.set_hour = set_hour
        self.set_minute = set_minute

    def time(self):
        return QTime(self.set_hour, self.set_minute)

    def dict(self):
        return {
            "name": self.name,
            "set_hour": self.set_hour,
            "set_minute": self.set_minute
        }
