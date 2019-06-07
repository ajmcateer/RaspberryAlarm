# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 82)
        self.btnSnooze = QtWidgets.QPushButton(Dialog)
        self.btnSnooze.setGeometry(QtCore.QRect(0, 0, 201, 81))
        self.btnSnooze.setObjectName("btnSnooze")
        self.btnDismiss = QtWidgets.QPushButton(Dialog)
        self.btnDismiss.setGeometry(QtCore.QRect(200, 0, 201, 81))
        self.btnDismiss.setObjectName("btnDismiss")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ALARM!"))
        self.btnSnooze.setText(_translate("Dialog", "Snooze"))
        self.btnDismiss.setText(_translate("Dialog", "Dismiss"))

