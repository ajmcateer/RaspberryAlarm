from PyQt5 import QtCore, QtWidgets
from Sounds import stop
from base_classes.buttons_dialog_base import Ui_Dialog


class AlarmNotification(QtWidgets.QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(AlarmNotification, self).__init__(parent)
        self.setupUi(self)
        self.btnDismiss.clicked.connect(self.dismiss_alarm)

    @QtCore.pyqtSlot()
    def dismiss_alarm(self):
        stop()
        self.close()
