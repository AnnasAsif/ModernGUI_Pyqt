from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from functools import partial

from io import BytesIO

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

        

        #Back Button
        self.back.clicked.connect(self.to_mainscreen)
        # Connect the button to the hover functions
        self.back.enterEvent = self.button_entered6
        self.back.leaveEvent = self.button_left6

        self.widget = self.findChild(QWidget, "widget")
        self.widget_2 = self.findChild(QWidget, "widget_2")
        
        self.image_widget = self.findChild(QWidget, "image_widget")

        self.createCategoryButtons()
        


    def button_entered6(self, event):
        self.back.setStyleSheet(self.button_style_entered)

    def button_left6(self, event):
        self.back.setStyleSheet(self.button_style_left)

    def on_button(self):
        print('BUTTON')

    def to_mainscreen(self):
        print('BACK TO MAIN SCREEN')
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)


    def createCategoryButtons(self):

        # Create a list of image paths
        response = requests.get('http://161.97.164.28:8080/api/categories/seemore')
        data = json.loads(response.text)
        button_list = data['content']

        
        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(15, 15, 15, 15)

        
        for i in button_list:
            button= QPushButton(i['name'], self)
            button.setStyleSheet("""
                QPushButton {
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);
                    background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255));
                    
                    border-radius: 20px;
                }
                QPushButton:hover {
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);
                    background-color: rgb(65, 109, 255);
                }
            """)
            button.clicked.connect(partial(self.createBundlesButtons, i['_id']))
            scroll_layout.addWidget(button)

        self.widget.setLayout(scroll_layout)

        # self.layout.addWidget(frame)

    def createBundlesButtons(self, value):
        # Create a list of image paths
        url = 'http://161.97.164.28:8080/api/bundles/getbundles?categoryId=' + value
        # print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        button_list = data['content']

        # print(button_list)


        scroll_layout = QVBoxLayout()
        scroll_layout.setContentsMargins(15, 15, 15, 15)
        scroll_layout.setSpacing(10)  # Adjust the spacing between buttons

        
        for i in button_list:
            button= QPushButton(i['name'], self)
            button.setStyleSheet("""
                QPushButton {
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);
                    background-color:  qlineargradient(spread:pad, x1:0.211091, y1:0.199, x2:0.608, y2:0.603, stop:0.767045 rgba(30, 63, 102, 255), stop:0.977273 rgba(34, 70, 117, 255));
                    
                    border-radius: 20px;
                }
                QPushButton:hover {
                    font: 12pt 'MS Shell Dlg 2';
                    color: rgb(255, 255, 255);
                    background-color: rgb(65, 109, 255);
                }
            """)
            button.clicked.connect(partial(self.showImages, i['_id']))
            scroll_layout.addWidget(button)


        self.widget_2.setLayout(scroll_layout)

    def showImages(self, value):
        # Create a list of image paths
        url = 'http://161.97.164.28:8080/api/frames/seemore?bundleId=' + value
        # print(url)
        response = requests.get(url)
        data = json.loads(response.text)
        images_data = data['content']
        # print(images_data)

        frame_width = 134  # Replace with your desired frame width
        frame_height = 200  # Replace with your desired frame height

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        layout = QVBoxLayout()
        scroll_content.setLayout(layout)
        
        # Create a horizontal layout for displaying images in a row
        h_layout = QHBoxLayout()

        for image_url in images_data:
            try:
                response = requests.get(image_url['image'])
                print('---->>', response.status_code)
                if response.status_code == 200:
                    image_data = BytesIO(response.content)
                    # Convert BytesIO to bytes using getvalue()
                    image_bytes = image_data.getvalue()
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_bytes)

                    # Scale the pixmap to the specified frame size
                    pixmap = pixmap.scaled(frame_width, frame_height)

                    if not pixmap.isNull():
                        label = QLabel()
                        label.setPixmap(pixmap)
                        h_layout.addWidget(label)

                        # Check if adding another label would exceed the available width
                        if h_layout.sizeHint().width() > self.image_widget.viewport().width():
                            layout.addLayout(h_layout)
                            h_layout = QHBoxLayout()  # Start a new row
                        
                    # Add the last row to the layout
                    layout.addLayout(h_layout)
                else:
                    print(f"-->Failed to load image from URL: {image_url['image']}, Status Code: {response.status_code}")
            except Exception as e:
                print(f"=>=>Failed to load image from URL: {image_url['image']}, Error: {str(e)}")

                    
        self.image_widget.setLayout(layout)






    def buttonClick(self, value):
        sender = self.sender()  # Get the button that triggered the event
        print('Value: ', value);
        print(f"Button clicked: {sender.text()}")