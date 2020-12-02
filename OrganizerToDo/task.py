import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from models.Task import Task

from UI.taskUI import UI_Task
from models.Task import Task


class TaskMenu(QWidget, UI_Task):
    def __init__(self, parent=None):
        super(TaskMenu, self).__init__(parent)
        self.setupUi(self)
        self.Tasks = []

    def addTask(self, task):
        print(self.task)

    def ShowApp(self):
        self.show()
