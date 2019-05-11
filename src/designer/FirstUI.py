# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 120, 89, 16))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 150, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(370, 10, 391, 261))
        self.openGLWidget.setObjectName("openGLWidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 290, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 39, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 80, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(120, 180, 37, 18))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(360, 490, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(370, 290, 391, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.lineEdit.setText(_translate("MainWindow", "user name "))
        self.lineEdit_2.setText(_translate("MainWindow", "password"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "Log out"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))

