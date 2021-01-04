
from UI.backUI import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication


import sys

class Back(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Back, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()

    def showApp(self):
        self.show()
        self.timer.timeout.connect(self.TimeCount)
        self.timer.start(100)

    def TimeCount(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 10
            self.progressBar.setValue(value)
        else:
            import login
            self.timer.stop()
            self.log = login.Login()
            self.log.showApp()
            self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Back()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(200)
    widget.show()
    sys.exit(app.exec())
