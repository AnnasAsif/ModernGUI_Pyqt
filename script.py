import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from welcomescreen import WelcomeScreen

def main():
    app = QApplication(sys.argv)
    
    widget = QStackedWidget()
    welcome = WelcomeScreen(widget)
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("EXITING")

if __name__ == "__main__":
    main()