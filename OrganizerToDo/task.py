import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu

from UI.taskUI import UI_Task


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

        if zad == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Nie wpisales zadnego zadania')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            self.Tasks.append(zad)
            self.textEdit.clear()
            icon = QtGui.QIcon('not-done.png')
            item = QtWidgets.QListWidgetItem(icon, str(self.hash) + " : " + zad)
            self.listView.insertItem(self.objCounter, item)
            self.objCounter = self.objCounter + 1

            plik = open("zadania.txt", 'a')
            plik.write("\n" + str(self.hash) + " : " + zad )

            plik.close

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

           # filepath = 'zadania.txt'
            #DELIMITER = "\n"
            #SelectedText = self.listView.currentItem().text()
            #with open(filepath, 'r+') as f:
             #   for linia in f.readlines():
              #      linia = linia.strip()

               #     linia = linia.split("{}".format(DELIMITER))[0]
                #    print(linia)
                 #   if linia == SelectedText:
                  #      f.strip(linia)
                   #     print('znalezione')


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Uwaga!')
            msg.setText('Nie wybrałeś żadnego elementu')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction('Zrobione')

        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if self.listView.currentItem() is not None:
            if action == newAct:
                SelectedText = self.listView.currentItem().text()
                self.listView.currentItem().setHidden(True)
                icon = QtGui.QIcon('done.png')
                item = QtWidgets.QListWidgetItem(icon, SelectedText)
                self.listView.insertItem(self.objCounter, item)

                print('Wcisnelam przycisk Zrobione')

