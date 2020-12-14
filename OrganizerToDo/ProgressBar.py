import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication

from UI.progressUI import Ui_Form
from calendar import Calendar


class ProgressBarLogin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ProgressBarLogin, self).__init__(parent)
        self.calendar = Calendar()
        self.setupUi(self)

        self.timer = QTimer()


    def showApp(self):
        self.show()
        self.timer.timeout.connect(self.TimeCount)
        self.timer.start(100)

    def TimeCount(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 8
            self.progressBar.setValue(value)
        else:
            self.timer.stop()
            print('Mamy 100%')
            self.calendar.showApp()
            self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = ProgressBarLogin()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(200)
    widget.show()
    sys.exit(app.exec())