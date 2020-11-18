import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.btnId.clicked.connect(self.loginF)
        self.exitId.clicked.connect(self.exitF)

    def loginF(self):
        login = self.loginId.text()
        password = self.passwordId.text()
        user = login + ' ' + password
        print(user)

    def exitF(self):
        choice = QMessageBox.question(self, 'Exit', 'Czy na pewno chcesz wyjść?',
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit(app.exec_())
        elif choice == QMessageBox.No:
            QMessageBox.close(self)


app = QApplication(sys.argv)
mainWindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(420)
widget.setFixedHeight(420)
widget.show()
app.exec_()
