import sys

from UI.loginUI import loginUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from models.User import User
from calendar import Calendar


class Login(QDialog, loginUI):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.calendar = Calendar()
        self.setupUi(self)

        self.loginbtn.clicked.connect(self.loginF)
        self.exitbtn.clicked.connect(self.exitF)
        Admin = User("admin", "admin")

    def loginF(self):

        login = self.loginId.text()
        haslo = self.loginId.text()

        filepath = 'admin.txt'

        DELIMITER = " "

        with open(filepath) as fr:
            for line in fr:
                loginAdmin = line.split("{}".format(DELIMITER))[0] #czytanie pierwszej kolumny
                hasloAdmin = line.split("{}".format(DELIMITER))[1] #czytanie drugiej kolumny

        if login == loginAdmin and haslo == hasloAdmin:

            print(f'Login : {login}\nHasło : {haslo}')
            print("Zalogowano!")

            self.calendar.showApp()
            self.hide()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Nieprawidłowy login lub hasło, spróbuj ponownie')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def exitF(self):
        print("Zamknięto aplikację")
        sys.exit(1)


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(350)
widget.show()
app.exec_()