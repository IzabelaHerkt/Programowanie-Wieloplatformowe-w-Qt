import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTextCodec
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QFileDialog
from PyQt5.uic.properties import QtGui

from UI.calendarUI import Ui_Form
from models.Task import Task
from task import TaskMenu


class Calendar(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)
        QTextCodec.setCodecForLocale(QTextCodec.codecForName("UTF-8"))
        self.setupUi(self)
        self.taskArray = []
        self.calendarWidget.selectionChanged.connect(self.dateSelected)
        self.quitbtn.clicked.connect(self.quit)
        self.taskbtn.clicked.connect(self.taskFile)
        self.addbtn.clicked.connect(self.addFile)

    def addFile(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        input_file, x = QFileDialog.getOpenFileName(self, 'Open File', 'calendar.py', 'Wszystko (*);;Tekst (*)',
                                                  options=options)
        output_file = "zadania.txt"

        if input_file != "":
            with open(input_file, 'r') as in_file, open(output_file, 'a') as out_file:
                for line in in_file:
                    out_file.write(line)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Komunikat')
            msg.setText("Dodano zadania!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def taskFile(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName = 'zadania.txt'

        if fileName:
            fileRead = open(fileName, 'r', encoding='utf-8')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Zadania do wykonania')
            msg.setText("Wszystkie zadania:\n" + fileRead.read())
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            print(fileRead.read())
            fileRead.close()

    def quit(self):
        msg = QMessageBox.question(self, "Wyjscie", "Czy chcesz zamknąć aplikację?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            sys.exit(1)

    def showApp(self):
        self.show()

    def dateSelected(self):
        month = self.calendarWidget.selectedDate().month()
        year = self.calendarWidget.selectedDate().year()
        day = self.calendarWidget.selectedDate().day()

        #print(month, year, day)

        taskH = str(day) + "|" + str(month) + "|" + str(year)

        newTask = TaskMenu()
        newTask.addHash(taskH)

        listLen = len(self.taskArray)

        if listLen != 0:
            for i in range(listLen):
                if self.taskArray[i].hash == taskH:
                    self.taskArray[i].ShowApp()
                    break

                else:
                    self.taskArray.append(newTask)
                    self.taskArray[len(self.taskArray)-1].ShowApp()
        else:
            self.taskArray.append(newTask)
            self.taskArray[len(self.taskArray) - 1].ShowApp()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Calendar()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(400)
    widget.setFixedHeight(350)
    widget.show()
    sys.exit(app.exec())