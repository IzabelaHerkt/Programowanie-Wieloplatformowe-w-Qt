import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MessageBox(QWidget):

    def __init__(self):
        super(MessageBox, self).__init__()

        self.setWindowTitle('MessageBox')
        self.setFixedSize(QSize(300, 300))

        button = QPushButton('Zamknij\naplikację', self)
        button.setFont(QFont('Times', 13))
        button.move(100, 100)
        button.resize(100, 100)
        button.clicked.connect(self.printStatus)

    def printStatus(self):

        msg = QMessageBox.question(
            self,
            'Wyjscie',
            'Czy chcesz zamknąć aplikację?',
            QMessageBox.Yes,
            QMessageBox.No
        )

        if msg == QMessageBox.Yes:
            sys.exit(app.exec_())


app = QApplication(sys.argv)
window = MessageBox()
window.show()
app.exec_()
