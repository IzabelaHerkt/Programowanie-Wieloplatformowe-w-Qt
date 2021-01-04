import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from UI.newUI import Ui_Form
from back import Back


class newUser(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(newUser, self).__init__(parent)
        self.back = Back()
        self.setupUi(self)

        self.backbtn.clicked.connect(self.backF)
        self.addbtn.clicked.connect(self.addF)

    def backF(self):
        self.back.showApp()
        self.hide()

    def addF(self):
        login = self.loginId.text()
        haslo = self.passwordId.text()
        imie = self.nameId.text()
        nazwisko = self.secondId.text()

        if login == "" or haslo == "" or imie == "" or nazwisko == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Brak wszystkich danych!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            plik = open("data.txt", 'a')
            plik.write("\n" + login + " " + haslo)
            plik.close
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Dodano uzytkownika!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.back.showApp()
            self.hide()


    def showApp(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = newUser()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(200)
    widget.show()
    sys.exit(app.exec())