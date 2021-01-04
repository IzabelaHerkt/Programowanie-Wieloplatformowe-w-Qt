# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class UI_Task(object):
    def setupUi(self, Zadanie):
        Zadanie.setObjectName("Zadanie")
        self.setFixedSize(QSize(400, 300))
        Zadanie.setStyleSheet("background-color: #808080 ")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.listView = QtWidgets.QListWidget(Zadanie)
        self.listView.setGeometry(QtCore.QRect(10, 40, 182, 221))
        self.listView.setStyleSheet("background-color: #FFFFFF ;border-radius : 6px; color:black")
        self.listView.setObjectName("listView")

        self.label = QtWidgets.QLabel(Zadanie)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 29))
        self.label.setStyleSheet("color:white\n")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Zadanie)
        self.textEdit.setGeometry(QtCore.QRect(210, 40, 182, 221))
        self.textEdit.setStyleSheet("background-color: #FFFFFF;border-radius : 6px; color:black ")
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(Zadanie)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 130, 29))
        self.label_2.setStyleSheet("color:white\n")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(Zadanie)
        self.pushButton.setGeometry(QtCore.QRect(275, 270, 85, 23))
        self.pushButton.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Zadanie)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 270, 85, 23))
        self.pushButton_2.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton3 = QtWidgets.QPushButton(Zadanie)
        self.pushButton3.setGeometry(QtCore.QRect(160, 270, 85, 23))
        self.pushButton3.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton")

        self.retranslateUi(Zadanie)
        QtCore.QMetaObject.connectSlotsByName(Zadanie)

    def retranslateUi(self, Zadanie):
        _translate = QtCore.QCoreApplication.translate
        Zadanie.setWindowTitle(_translate("Zadanie", "Zadanie"))
        self.label.setText(_translate("Zadanie", "Twoje zadania:"))
        self.label_2.setText(_translate("Zadanie", "Edytuj zadanie:"))
        self.pushButton.setText(_translate("Zadanie", "Dodaj"))
        self.pushButton_2.setText(_translate("Zadanie", "Usuń"))
        self.pushButton3.setText(_translate("Zadanie", "Edytuj"))
