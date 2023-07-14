from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from mainscreen import MainScreen

class LoginScreen(QDialog):
    def __init__(self, widget) -> None:
        self.widget = widget
        super(LoginScreen, self).__init__()
        self.button_style_entered = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);"
        self.button_style_left = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255))"

        #Loading LogIn UI
        loadUi("login.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        #Login Button
        self.login2.clicked.connect(self.loggedin)
        # Connect the button to the hover functions
        self.login2.enterEvent = self.button_entered
        self.login2.leaveEvent = self.button_left

        #Back Button
        self.back.clicked.connect(self.welcomescreen)
        # Connect the button to the hover functions
        self.back.enterEvent = self.button_entered2
        self.back.leaveEvent = self.button_left2

        self.username = self.findChild(QLineEdit, "username")
        # self.username.textChanged.connect(self.on_username)

        self.password = self.findChild(QLineEdit, "password")
        # self.password.textChanged.connect(self.on_password)

        

    def button_entered(self, event):
        self.login2.setStyleSheet(self.button_style_entered)
    def button_entered2(self, event):
        self.back.setStyleSheet(self.button_style_entered)

    def button_left(self, event):
        self.login2.setStyleSheet(self.button_style_left)
    def button_left2(self, event):
        self.back.setStyleSheet(self.button_style_left)

    def loggedin(self):
        username = self.username.text()
        password = self.password.text()
        if(username=='AnnasAsif' and password=='Annas@3221'):
            print('Logging In')
        else:
            print('Enter right credentials')
        mainscreen = MainScreen(self.widget)
        self.widget.addWidget(mainscreen)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def welcomescreen(self):
        print('BACK TO WELCOME SCREEN')
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    # def on_username(self):
    #     print(self.username.text())

    # def on_password(self):
    #     print(self.password.text())