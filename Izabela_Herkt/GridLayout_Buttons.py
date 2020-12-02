import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QMessageBox


def printStatus():

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle('Komunikat')
    msg.setText('Kliknięto')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class Buttons(QWidget):

    def __init__(self):
        super(Buttons, self).__init__()
        self.setWindowTitle('GridLayout_Buttons')
        self.initUI()
        self.GridLayout_Buttons()

    def initUI(self):
        self.setFixedSize(300, 350)

    def GridLayout_Buttons(self):

        verticalBox = QVBoxLayout()
        licznik = 0

        for i in range(3):

            licznik += 1
            horizontalBox = QHBoxLayout()
            verticalBox.addLayout(horizontalBox)

            for j in range(3):
                button = QPushButton(str(licznik), self)
                button.setFont(QFont('Times', 30))
                button.clicked.connect(printStatus)
                button.resize(100, 125)

                horizontalBox.addWidget(button)
                licznik += 1

            licznik -= 1

        horizontalBox = QHBoxLayout()
        verticalBox.addLayout(horizontalBox)
        self.setLayout(verticalBox)
        self.show()


app = QApplication(sys.argv)
ex = Buttons()
sys.exit(app.exec())