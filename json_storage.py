from base_classes.storage_base import StorageBase
import json
from models.alarm_model import AlarmModel


class JsonStorage(StorageBase):

    alarms = {}

    def __init__(self, path):
        self.path = path

    def save(self, alarms):
        try:
            with open("alarms.json", "w+") as f:
                alarm_list = []
                for k, v in alarms.items():
                    alarm_list.append(v.dict())
                f.write(json.dumps(alarm_list))
        except Exception as ex:
            print(str(ex))

    def read(self):
        import ast
        self.alarms = {}
        try:
            with open("alarms.json", 'r') as f:
                temp_alarms = ast.literal_eval(f.read())
                for alarm in temp_alarms:
                    self.alarms[alarm["name"]] = (AlarmModel(name=alarm["name"], set_hour=alarm["set_hour"],
                                                             set_minute=alarm["set_minute"]))
                return self.alarms
        except FileNotFoundError:
            print("Unable to load alarms.json")
            return self.alarms

    def read(self):
        import ast
        self.alarms = []
        try:
            with open("alarms.json", 'r') as f:
                temp_alarms = ast.literal_eval(f.read())
                for alarm in temp_alarms:
                    self.alarms.append(AlarmModel(name=alarm["name"], set_hour=alarm["set_hour"],
                                                  set_minute=alarm["set_minute"]))
                return self.alarms
        except FileNotFoundError:
            print("Unable to load alarms.json")
            return self.alarms
