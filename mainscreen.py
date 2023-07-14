from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

from loveframe import LoveFrame

class MainScreen(QDialog):
    def __init__(self, widget) -> None:
        self.widget = widget
        super(MainScreen, self).__init__()
        self.button_style_entered = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);"
        self.button_style_left = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255))"

        #Loading LogIn UI
        loadUi("main.ui", self)

        #App 1 Button
        self.app1.clicked.connect(self.on_app1)
        # Connect the button to the hover functions
        self.app1.enterEvent = self.button_entered
        self.app1.leaveEvent = self.button_left

        #App 2 Button
        self.app2.clicked.connect(self.on_app2)
        # Connect the button to the hover functions
        self.app2.enterEvent = self.button_entered2
        self.app2.leaveEvent = self.button_left2

        #App 3 Button
        self.app3.clicked.connect(self.on_app3)
        # Connect the button to the hover functions
        self.app3.enterEvent = self.button_entered3
        self.app3.leaveEvent = self.button_left3

        #App 4 Button
        self.app4.clicked.connect(self.on_app4)
        # Connect the button to the hover functions
        self.app4.enterEvent = self.button_entered4
        self.app4.leaveEvent = self.button_left4

        #App 5 Button
        self.app5.clicked.connect(self.on_app5)
        # Connect the button to the hover functions
        self.app5.enterEvent = self.button_entered5
        self.app5.leaveEvent = self.button_left5

        #Back Button
        self.back.clicked.connect(self.loginscreen)
        # Connect the button to the hover functions
        self.back.enterEvent = self.button_entered6
        self.back.leaveEvent = self.button_left6


    def button_entered(self, event):
        self.app1.setStyleSheet(self.button_style_entered)
    def button_entered2(self, event):
        self.app2.setStyleSheet(self.button_style_entered)
    def button_entered3(self, event):
        self.app3.setStyleSheet(self.button_style_entered)
    def button_entered4(self, event):
        self.app4.setStyleSheet(self.button_style_entered)
    def button_entered5(self, event):
        self.app5.setStyleSheet(self.button_style_entered)
    def button_entered6(self, event):
        self.back.setStyleSheet(self.button_style_entered)

    def button_left(self, event):
        self.app1.setStyleSheet(self.button_style_left)
    def button_left2(self, event):
        self.app2.setStyleSheet(self.button_style_left)
    def button_left3(self, event):
        self.app3.setStyleSheet(self.button_style_left)
    def button_left4(self, event):
        self.app4.setStyleSheet(self.button_style_left)
    def button_left5(self, event):
        self.app5.setStyleSheet(self.button_style_left)
    def button_left6(self, event):
        self.back.setStyleSheet(self.button_style_left)

    def on_app1(self):
        print('LOVE PHOTO FRAMES')
        loveframe = LoveFrame(self.widget)
        self.widget.addWidget(loveframe)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def on_app2(self):
        print('App2')
        # self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def on_app3(self):
        print('App3')
        # self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def on_app4(self):
        print('App4')
        # self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def on_app5(self):
        print('App5')
        # self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def loginscreen(self):
        print('BACK TO LOGIN SCREEN')
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)
