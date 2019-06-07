from PyQt5 import QtCore, QtWidgets
from models.alarm_model import AlarmModel
from base_classes.add_alarm_base import Ui_Dialog


class AddAlarm(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent=None, **kwargs):
        super(AddAlarm, self).__init__(parent)
        self.setupUi(self)
        self.delete = False
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)
        self.btnDelete.clicked.connect(self.on_click)
        self.accepted.connect(self.save)
        self.alarm = None

        if 'alarm_clock' in kwargs:
            self.txtName.setPlainText(kwargs['alarm_clock'].name)
            self.teAlarmTime.setTime(kwargs['alarm_clock'].time())

    @QtCore.pyqtSlot()
    def cancel(self):
        self.close()

    @QtCore.pyqtSlot()
    def on_click(self):
        self.delete = True
        self.close()

    @QtCore.pyqtSlot()
    def save(self):
        hour = self.teAlarmTime.time().hour()
        minute = self.teAlarmTime.time().minute()
        self.alarm = AlarmModel(name=self.txtName.toPlainText(), set_hour=hour, set_minute=minute)
