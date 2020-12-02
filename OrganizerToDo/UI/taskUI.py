# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Task(object):
    def setupUi(self, Zadanie):
        Zadanie.setObjectName("Zadanie")
        Zadanie.resize(400, 300)
        self.listView = QtWidgets.QListView(Zadanie)
        self.listView.setGeometry(QtCore.QRect(10, 40, 191, 221))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Zadanie)
        self.label.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Zadanie)
        self.textEdit.setGeometry(QtCore.QRect(210, 40, 181, 221))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Zadanie)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Zadanie)
        self.pushButton.setGeometry(QtCore.QRect(260, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Zadanie)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Zadanie)
        QtCore.QMetaObject.connectSlotsByName(Zadanie)

    def retranslateUi(self, Zadanie):
        _translate = QtCore.QCoreApplication.translate
        Zadanie.setWindowTitle(_translate("Zadanie", "Zadanie"))
        self.label.setText(_translate("Zadanie", "Twoje zadania:"))
        self.label_2.setText(_translate("Zadanie", "Edytuj zadanie:"))
        self.pushButton.setText(_translate("Zadanie", "Dodaj"))
        self.pushButton_2.setText(_translate("Zadanie", "Usuń"))
