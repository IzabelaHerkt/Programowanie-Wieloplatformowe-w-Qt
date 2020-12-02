import sys
from datetime import datetime

from PyQt5.QtCore import QSize
from PyQt5.uic.properties import QtWidgets

from login import Login

from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton


class CalendarMenu(QWidget, Login):

    #global currentYear, currentMonth

    #currentYear = datetime.now().year
    #currentMonth = datetime.now().month

    def __init__(self, parent=None):
        super(CalendarMenu, self).__init__(parent)
 	self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 450, 300)
        self.setupUi(self)

    print("dziala")



def main():
    app = QApplication(sys.argv)
    demo = CalendarMenu()
    demo.show()
    sys.exit(app.exec_())


main()

