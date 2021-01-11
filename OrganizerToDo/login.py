import sys

from PyQt5.QtCore import QSize
from PyQt5.uic.properties import QtGui

from UI.loginUI import loginUI
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox

from models.User import User
from ProgressBar import ProgressBarLogin
from newuser import newUser


class Login(QDialog, loginUI):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.progressBar = ProgressBarLogin()
        self.NewUser = newUser()

        self.loginbtn.clicked.connect(self.loginF)
        self.newbtn.clicked.connect(self.newF)

        #Admin = User("admin", "admin")

    def showApp(self):
        self.show()

    def newF(self):
        self.NewUser.showApp()
        self.hide()

    def loginF(self):

        import hashlib

        notFound = True
        login = self.loginId.text()
        haslo = self.passwordId.text()
        haslo = hashlib.md5(haslo.encode('utf-8')).hexdigest()

        filepath = 'data.txt'

        DELIMITER = " "

        with open(filepath, 'r') as plik:
            for linia in plik.readlines():
                linia = linia.strip()

                loginAdmin = linia.split("{}".format(DELIMITER))[0] #czytanie pierwszej kolumny
                hasloAdmin = linia.split("{}".format(DELIMITER))[1] #czytanie drugiej kolumny

                if login == loginAdmin and haslo == hasloAdmin:
                    #print(f'Login : {login}\nHasło : {haslo}')
                    print("Zalogowano!")

                    notFound = False

                    if not notFound:
                        self.progressBar.showApp()
                        self.hide()

                    break

            if notFound:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Uwaga!')
                msg.setText('Nieprawidłowy login lub hasło, spróbuj ponownie')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(420)
    widget.show()
    sys.exit(app.exec())




