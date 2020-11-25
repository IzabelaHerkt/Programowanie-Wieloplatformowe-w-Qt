import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import calendar
from PyQt5.QtCore import QDate


class CalendarMenu(QWidget):
    global currentYear, currentMonth

    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 450, 300)


def main():
    app = QApplication(sys.argv)
    demo = CalendarMenu()
    demo.show()
    sys.exit(app.exec_())


main()
