from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

import requests
import json

class LoveFrame(QDialog):
    def __init__(self, widget) -> None:
        self.widget = widget
        super(LoveFrame, self).__init__()
        self.button_style_entered = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);"
        self.button_style_left = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255))"

        #Loading LogIn UI
        loadUi("loveframe.ui", self)

        # Create a list of image paths
        response = requests.get('http://161.97.164.28:8080/api/categories/seemore')
        data = json.loads(response.text)
        image_paths = data['content']

        #Back Button
        self.back.clicked.connect(self.to_mainscreen)
        # Connect the button to the hover functions
        self.back.enterEvent = self.button_entered6
        self.back.leaveEvent = self.button_left6

        layout = QVBoxLayout(self)
        frame = QFrame()
        frame.setFixedSize(200, 200)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(15, 15, 15, 15)

        # Add labels or other widgets to the scroll layout
        for i in image_paths:
            button= QPushButton(i['name'], self)
            button.setStyleSheet("""
                QPushButton {
                    border-radius:15%;
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);
                    background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255));
                    color: white;
                }
                QPushButton:hover {
                    border-radius:15%;
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);
                }
            """)
            button.clicked.connect(self.buttonClicked)
            scroll_layout.addWidget(button)

        frame.setLayout(scroll_layout)

        layout.addWidget(frame)


    def button_entered6(self, event):
        self.back.setStyleSheet(self.button_style_entered)

    def button_left6(self, event):
        self.back.setStyleSheet(self.button_style_left)

    def on_button(self):
        print('BUTTON')

    def to_mainscreen(self):
        print('BACK TO MAIN SCREEN')
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def buttonClicked(self):
        sender = self.sender()  # Get the button that triggered the event
        print(f"Button clicked: {sender.text()}")