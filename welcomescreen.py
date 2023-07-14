from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from login import LoginScreen


class WelcomeScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(WelcomeScreen, self).__init__()

        self.button_style_entered = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);"
        self.button_style_left = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255))"
        
        #Loading Welcome Screen UI
        loadUi("welcome.ui", self)
        #Login Button
        self.login.clicked.connect(self.gotologin)
        # Connect the button to the hover functions
        self.login.enterEvent = self.button_entered
        self.login.leaveEvent = self.button_left

    def createnewaccount(self):
        print('create new account')

    def gotologin(self):
        login = LoginScreen(self.widget)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def button_entered(self, event):
        self.login.setStyleSheet(self.button_style_entered)

    def button_left(self, event):
        self.login.setStyleSheet(self.button_style_left)
   