# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\welcomescreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.091, x2:0.965909, y2:0.784, stop:0 rgba(79, 91, 200, 255), stop:1 rgba(151, 231, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(500, 120, 201, 61))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 190, 301, 31))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(self.bgwidget)
        self.login.setGeometry(QtCore.QRect(450, 330, 291, 41))
        self.login.setStyleSheet("border-radius:15px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 255, 255), stop:1 rgba(62, 62, 62, 255));")
        self.login.setObjectName("login")
        self.newaccount = QtWidgets.QPushButton(self.bgwidget)
        self.newaccount.setGeometry(QtCore.QRect(450, 410, 291, 41))
        self.newaccount.setStyleSheet("border-radius:15px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 255, 255), stop:1 rgba(62, 62, 62, 255));")
        self.newaccount.setObjectName("newaccount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">Welcome</span></p></body></html>"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Sign In or Create an Account</span></p></body></html>"))
        self.login.setText(_translate("Dialog", "Login"))
        self.newaccount.setText(_translate("Dialog", "Create a New Account"))
