import sys

from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMessageBox, QLineEdit, QListWidget, \
    QGridLayout, QWidget, QProgressBar


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Lista obiektow')
        self.setFixedSize(QSize(400, 400)) \

        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.licznik = 0

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Nazwa obiektu:')
        self.nameLabel.setFont(QFont('Times', 16))
        self.nameLabel.move(20, 20)
        self.nameLabel.resize(140, 40)

        layout.addWidget(self.nameLabel)

        # wpisywanie nazwy

        self.line = QLineEdit(self)
        self.line.setFont(QFont('Times', 16))
        self.line.move(160, 25)
        self.line.resize(120, 30)

        layout.addWidget(self.line)

        #przycisk

        self.button = QPushButton(self)
        self.button.setIcon(QIcon('add.png'))

        size = QSize(40, 40)
        self.button.setIconSize(size)

        layout.addWidget(self.button)

        self.button.clicked.connect(self.addObject)

        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)

        self.timer = QTimer()
        self.timer.start(100)

        layout.addWidget(self.progressBar)

        self.listwidget = QListWidget()

        layout.addWidget(self.listwidget)

    def addObject(self):

        lineText = self.line.text()
        value = self.progressBar.value()

        if len(lineText) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Komunikat')
            msg.setText('Nie wpisano nazwy obiektu!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:

            if self.licznik < 10:

                self.listwidget.insertItem(self.licznik, lineText)
                value = value + 10
                self.progressBar.setValue(value)

            if self.licznik == 10:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Komunikat')
                msg.setText('Nie mozna dodac obiektu!')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

                self.timer.stop()

            self.licznik += 1


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())