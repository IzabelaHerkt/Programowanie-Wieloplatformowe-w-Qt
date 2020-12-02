import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication

from UI.calendarUI import Ui_Form
from models.Task import Task
from task import TaskMenu


class Calendar(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)
        self.setupUi(self)
        self.taskMenu = TaskMenu()
        self.calendarWidget.selectionChanged.connect(self.dateSelected)

    def showApp(self):
        self.show()
        print("jest")

    def dateSelected(self):
        month = self.calendarWidget.selectedDate().month()
        year = self.calendarWidget.selectedDate().year()
        day = self.calendarWidget.selectedDate().day()

        taskObj = Task(str(day), str(month), str(year), False)
        self.taskMenu.addTask(taskObj)
        self.taskMenu.ShowApp()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Calendar()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(350)
    widget.show()
    sys.exit(app.exec())