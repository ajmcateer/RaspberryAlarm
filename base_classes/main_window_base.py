# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarmclockalt4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setWindowTitle("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 801, 431))
        self.toolBox.setObjectName("toolBox")
        self.toolBoxPage1 = QtWidgets.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 801, 377))
        self.toolBoxPage1.setObjectName("toolBoxPage1")
        self.lblTime = QtWidgets.QLabel(self.toolBoxPage1)
        self.lblTime.setGeometry(QtCore.QRect(10, 120, 781, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblTime.setFont(font)
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.lblDate = QtWidgets.QLabel(self.toolBoxPage1)
        self.lblDate.setGeometry(QtCore.QRect(10, 200, 781, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lblDate.setFont(font)
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        self.btnAddAlarm = QtWidgets.QPushButton(self.toolBoxPage1)
        self.btnAddAlarm.setGeometry(QtCore.QRect(740, 330, 41, 41))
        self.btnAddAlarm.setObjectName("btnAddAlarm")
        self.btnShowAlarms = QtWidgets.QPushButton(self.toolBoxPage1)
        self.btnShowAlarms.setEnabled(True)
        self.btnShowAlarms.setGeometry(QtCore.QRect(740, 280, 41, 41))
        self.btnShowAlarms.setObjectName("btnShowAlarms")
        self.lvAlarmList = QtWidgets.QListView(self.toolBoxPage1)
        self.lvAlarmList.setGeometry(QtCore.QRect(10, 0, 121, 371))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lvAlarmList.setFont(font)
        self.lvAlarmList.setAutoFillBackground(False)
        self.lvAlarmList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lvAlarmList.setObjectName("lvAlarmList")
        self.lblWeatherIcon = QtWidgets.QLabel(self.toolBoxPage1)
        self.lblWeatherIcon.setGeometry(QtCore.QRect(350, 0, 91, 71))
        self.lblWeatherIcon.setText("")
        self.lblWeatherIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWeatherIcon.setObjectName("lblWeatherIcon")
        self.lblHiLow = QtWidgets.QLabel(self.toolBoxPage1)
        self.lblHiLow.setGeometry(QtCore.QRect(10, 70, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblHiLow.setFont(font)
        self.lblHiLow.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHiLow.setObjectName("lblHiLow")
        self.lblCurrent = QtWidgets.QLabel(self.toolBoxPage1)
        self.lblCurrent.setGeometry(QtCore.QRect(10, 90, 781, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCurrent.setFont(font)
        self.lblCurrent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrent.setObjectName("lblCurrent")
        self.lblTime.raise_()
        self.lblDate.raise_()
        self.btnAddAlarm.raise_()
        self.btnShowAlarms.raise_()
        self.lblWeatherIcon.raise_()
        self.lblHiLow.raise_()
        self.lblCurrent.raise_()
        self.lvAlarmList.raise_()
        self.toolBox.addItem(self.toolBoxPage1, "")
        self.toolBoxPage2 = QtWidgets.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 801, 377))
        self.toolBoxPage2.setObjectName("toolBoxPage2")
        self.groupBox = QtWidgets.QGroupBox(self.toolBoxPage2)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 781, 191))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.lblHour1Icon = QtWidgets.QLabel(self.groupBox)
        self.lblHour1Icon.setGeometry(QtCore.QRect(20, 50, 121, 101))
        self.lblHour1Icon.setScaledContents(True)
        self.lblHour1Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour1Icon.setObjectName("lblHour1Icon")
        self.lblHour2Icon = QtWidgets.QLabel(self.groupBox)
        self.lblHour2Icon.setGeometry(QtCore.QRect(170, 50, 121, 101))
        self.lblHour2Icon.setScaledContents(True)
        self.lblHour2Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour2Icon.setObjectName("lblHour2Icon")
        self.lblHour3Icon = QtWidgets.QLabel(self.groupBox)
        self.lblHour3Icon.setGeometry(QtCore.QRect(320, 50, 121, 101))
        self.lblHour3Icon.setScaledContents(True)
        self.lblHour3Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour3Icon.setObjectName("lblHour3Icon")
        self.lblHour4Icon = QtWidgets.QLabel(self.groupBox)
        self.lblHour4Icon.setGeometry(QtCore.QRect(470, 50, 121, 101))
        self.lblHour4Icon.setScaledContents(True)
        self.lblHour4Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour4Icon.setObjectName("lblHour4Icon")
        self.lblHour5Icon = QtWidgets.QLabel(self.groupBox)
        self.lblHour5Icon.setGeometry(QtCore.QRect(620, 50, 121, 101))
        self.lblHour5Icon.setScaledContents(True)
        self.lblHour5Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour5Icon.setObjectName("lblHour5Icon")
        self.lblHour1Temp = QtWidgets.QLabel(self.groupBox)
        self.lblHour1Temp.setGeometry(QtCore.QRect(20, 160, 131, 20))
        self.lblHour1Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour1Temp.setObjectName("lblHour1Temp")
        self.lblHour2Temp = QtWidgets.QLabel(self.groupBox)
        self.lblHour2Temp.setGeometry(QtCore.QRect(170, 160, 131, 20))
        self.lblHour2Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour2Temp.setObjectName("lblHour2Temp")
        self.lblHour3Temp = QtWidgets.QLabel(self.groupBox)
        self.lblHour3Temp.setGeometry(QtCore.QRect(320, 160, 131, 20))
        self.lblHour3Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour3Temp.setObjectName("lblHour3Temp")
        self.lblHour4Temp = QtWidgets.QLabel(self.groupBox)
        self.lblHour4Temp.setGeometry(QtCore.QRect(470, 160, 131, 20))
        self.lblHour4Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour4Temp.setObjectName("lblHour4Temp")
        self.lblHour5Temp = QtWidgets.QLabel(self.groupBox)
        self.lblHour5Temp.setGeometry(QtCore.QRect(620, 160, 131, 20))
        self.lblHour5Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour5Temp.setObjectName("lblHour5Temp")
        self.lblHour5Time = QtWidgets.QLabel(self.groupBox)
        self.lblHour5Time.setGeometry(QtCore.QRect(620, 20, 131, 20))
        self.lblHour5Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour5Time.setObjectName("lblHour5Time")
        self.lblHour4Time = QtWidgets.QLabel(self.groupBox)
        self.lblHour4Time.setGeometry(QtCore.QRect(470, 20, 131, 20))
        self.lblHour4Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour4Time.setObjectName("lblHour4Time")
        self.lblHour2Time = QtWidgets.QLabel(self.groupBox)
        self.lblHour2Time.setGeometry(QtCore.QRect(170, 20, 131, 20))
        self.lblHour2Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour2Time.setObjectName("lblHour2Time")
        self.lblHour3Time = QtWidgets.QLabel(self.groupBox)
        self.lblHour3Time.setGeometry(QtCore.QRect(320, 20, 131, 20))
        self.lblHour3Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour3Time.setObjectName("lblHour3Time")
        self.lblHour1Time = QtWidgets.QLabel(self.groupBox)
        self.lblHour1Time.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.lblHour1Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour1Time.setObjectName("lblHour1Time")
        self.groupBox_2 = QtWidgets.QGroupBox(self.toolBoxPage2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 781, 191))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblDaily1Icon = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily1Icon.setGeometry(QtCore.QRect(20, 50, 131, 101))
        self.lblDaily1Icon.setScaledContents(True)
        self.lblDaily1Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily1Icon.setObjectName("lblDaily1Icon")
        self.lblDaily2Icon = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily2Icon.setGeometry(QtCore.QRect(170, 50, 131, 101))
        self.lblDaily2Icon.setScaledContents(True)
        self.lblDaily2Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily2Icon.setObjectName("lblDaily2Icon")
        self.lblDaily3Icon = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily3Icon.setGeometry(QtCore.QRect(320, 50, 131, 101))
        self.lblDaily3Icon.setScaledContents(True)
        self.lblDaily3Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily3Icon.setObjectName("lblDaily3Icon")
        self.lblDaily4Icon = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily4Icon.setGeometry(QtCore.QRect(470, 50, 131, 101))
        self.lblDaily4Icon.setScaledContents(True)
        self.lblDaily4Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily4Icon.setObjectName("lblDaily4Icon")
        self.lblDaily5Icon = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily5Icon.setGeometry(QtCore.QRect(620, 50, 131, 101))
        self.lblDaily5Icon.setScaledContents(True)
        self.lblDaily5Icon.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily5Icon.setObjectName("lblDaily5Icon")
        self.lblDaily1Temp = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily1Temp.setGeometry(QtCore.QRect(20, 160, 131, 20))
        self.lblDaily1Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily1Temp.setObjectName("lblDaily1Temp")
        self.lblDaily2Temp = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily2Temp.setGeometry(QtCore.QRect(170, 160, 131, 20))
        self.lblDaily2Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily2Temp.setObjectName("lblDaily2Temp")
        self.lblDaily3Temp = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily3Temp.setGeometry(QtCore.QRect(320, 160, 131, 20))
        self.lblDaily3Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily3Temp.setObjectName("lblDaily3Temp")
        self.lblDaily4Temp = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily4Temp.setGeometry(QtCore.QRect(470, 160, 131, 20))
        self.lblDaily4Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily4Temp.setObjectName("lblDaily4Temp")
        self.lblDaily5Temp = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily5Temp.setGeometry(QtCore.QRect(620, 160, 131, 20))
        self.lblDaily5Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily5Temp.setObjectName("lblDaily5Temp")
        self.lblDaily1Time = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily1Time.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.lblDaily1Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily1Time.setObjectName("lblDaily1Time")
        self.lblDaily2Time = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily2Time.setGeometry(QtCore.QRect(170, 20, 131, 20))
        self.lblDaily2Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily2Time.setObjectName("lblDaily2Time")
        self.lblDaily3Time = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily3Time.setGeometry(QtCore.QRect(320, 20, 131, 20))
        self.lblDaily3Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily3Time.setObjectName("lblDaily3Time")
        self.lblDaily4Time = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily4Time.setGeometry(QtCore.QRect(470, 20, 131, 20))
        self.lblDaily4Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily4Time.setObjectName("lblDaily4Time")
        self.lblDaily5Time = QtWidgets.QLabel(self.groupBox_2)
        self.lblDaily5Time.setGeometry(QtCore.QRect(620, 20, 131, 20))
        self.lblDaily5Time.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDaily5Time.setObjectName("lblDaily5Time")
        self.toolBox.addItem(self.toolBoxPage2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lblTime.setText(_translate("MainWindow", "TextLabel"))
        self.lblDate.setText(_translate("MainWindow", "TextLabel"))
        self.btnAddAlarm.setText(_translate("MainWindow", "+"))
        self.btnShowAlarms.setText(_translate("MainWindow", "Alarms"))
        self.lblHiLow.setText(_translate("MainWindow", "Hi: 89 | Low: 60"))
        self.lblCurrent.setText(_translate("MainWindow", "Current: 89"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1), _translate("MainWindow", "Clock"))
        self.groupBox.setTitle(_translate("MainWindow", "Hourly Forcast"))
        self.lblHour1Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour2Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour3Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour4Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour5Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour1Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour2Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour3Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour4Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour5Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour5Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour4Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour2Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour3Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblHour1Time.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Daily Forcast"))
        self.lblDaily1Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily2Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily3Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily4Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily5Icon.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily1Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily2Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily3Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily4Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily5Temp.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily1Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily2Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily3Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily4Time.setText(_translate("MainWindow", "TextLabel"))
        self.lblDaily5Time.setText(_translate("MainWindow", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2), _translate("MainWindow", "Weather"))

