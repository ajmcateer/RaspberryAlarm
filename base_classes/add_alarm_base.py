# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAlarmDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(302, 128)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QPlainTextEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(80, 10, 211, 31))
        self.txtName.setObjectName("txtName")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.teAlarmTime = QtWidgets.QTimeEdit(Dialog)
        self.teAlarmTime.setGeometry(QtCore.QRect(80, 50, 211, 31))
        self.teAlarmTime.setObjectName("teAlarmTime")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 100, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.btnDelete = QtWidgets.QPushButton(Dialog)
        self.btnDelete.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.btnDelete.setObjectName("btnDelete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Time"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))

