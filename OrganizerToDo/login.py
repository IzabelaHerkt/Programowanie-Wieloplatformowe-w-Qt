import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from models.User import User


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbtn.clicked.connect(self.loginF)
        self.exitbtn.clicked.connect(self.exitF)
        Admin = User("admin", "admin")

    def loginF(self):
        login = self.loginId.text()
        haslo = self.passwordId.text()
        print(login + haslo)
        if login == "admin" and haslo == "admin":
            print("ok")
            from calendarMenu import CalendarMenu
            calendar = CalendarMenu()
            calendar.main()

    def exitF(self):
        print("exit")


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(420)
widget.setFixedHeight(600)
widget.show()
app.exec_()
