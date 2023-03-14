import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()

        self.button_style_entered = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: rgb(65, 109, 255);"
        self.button_style_left = "border-radius:15px;font: 12pt 'MS Shell Dlg 2';color: rgb(255, 255, 255);background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(60, 60, 255, 255), stop:1 rgba(62, 62, 62, 255));"

        loadUi("welcomescreen.ui", self)
        #Login Button
        self.login.clicked.connect(self.gotologin)
        # Connect the button to the hover functions
        self.login.enterEvent = self.button_entered
        self.login.leaveEvent = self.button_left

        #New Account Button
        self.newaccount.clicked.connect(self.createnewaccount)
        # Connect the button to the hover functions
        self.newaccount.enterEvent = self.button_entered2
        self.newaccount.leaveEvent = self.button_left2

    def createnewaccount(self):
        print('create new account')

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def button_entered(self, event):
        self.login.setStyleSheet(self.button_style_entered)
    def button_entered2(self, event):
        self.newaccount.setStyleSheet(self.button_style_entered)

    def button_left(self, event):
        self.login.setStyleSheet(self.button_style_left)
    def button_left2(self, event):
        self.newaccount.setStyleSheet(self.button_style_left)
        
class LoginScreen(QDialog):
    def __init__(self) -> None:
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

#main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("EXITING")