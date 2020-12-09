import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
from models.Task import Task

from UI.taskUI import UI_Task
from models.Task import Task


class TaskMenu(QWidget, UI_Task):
    def __init__(self, parent=None):
        super(TaskMenu, self).__init__(parent)
        self.setupUi(self)
        self.Tasks = []
        self.pushButton.clicked.connect(self.addBtn)
        self.listView.clicked.connect(self.checkZad)
        self.pushButton3.clicked.connect(self.editZad)
        self.pushButton_2.clicked.connect(self.deleteZad)
        self.objCounter = 0
        self.hash = 0

    def addTask(self, task):
        self.Tasks.append(str(task.day) + str(task.month) + str(task.year))

    def ShowApp(self):
        self.show()

    def addBtn(self):
        zad = self.textEdit.toPlainText()
        self.Tasks.append(zad)
        self.textEdit.clear()
        self.listView.insertItem(self.objCounter, str(self.objCounter) + " : " + zad)
        self.objCounter = self.objCounter+1

    def checkZad(self):
        SelectedText = self.listView.currentItem().text()
        self.textEdit.setText(SelectedText)

    def addHash(self, hsh):
        self.hash = hsh

    def editZad(self):
        zad = self.textEdit.toPlainText()
        if zad != "" and self.listView.currentItem() is not None:
            self.listView.currentItem().setText(zad)
        elif self.listView.currentItem() is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Nie wybrałeś żadnego elementu')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif zad != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Blad!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def deleteZad(self):
        if self.listView.currentItem() is not None:
            self.listView.currentItem().setHidden(True)
            self.textEdit.clear()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Nie wybrałeś żadnego elementu')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
