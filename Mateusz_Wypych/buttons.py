import sys
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QVBoxLayout, QHBoxLayout, QPushButton


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.makeButtons()

    def makeButtons(self):
        verticalBox = QVBoxLayout()
        for i in range(5):
            horizontalBox = QHBoxLayout()
            verticalBox.addLayout(horizontalBox)
            for j in range(5):
                buttonConcat = QPushButton(str(i) + str(j), self)
                horizontalBox.addWidget(buttonConcat)

        btnId = QPushButton("Zaloguj")
        exitId = QPushButton("Wyjdz")

        horizontalBox = QHBoxLayout()
        verticalBox.addLayout(horizontalBox)
        horizontalBox.addWidget(btnId)
        horizontalBox.addWidget(exitId)

        self.setLayout(verticalBox)
        self.show()

        btnId.clicked.connect(self.loginF)
        exitId.clicked.connect(self.exitF)

    def loginF(self):
        print("kliknales mnie")

    def exitF(self):
        choice = QMessageBox.question(self, 'Exit', 'Czy na pewno chcesz wyjść?',
                                      QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:
            sys.exit(app.exec_())
        elif choice == QMessageBox.No:
            QMessageBox.RejectRole


app = QApplication(sys.argv)
mainWindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(420)
widget.setFixedHeight(600)
widget.show()
app.exec_()
