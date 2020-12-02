from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class loginUI(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 319)
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet("background-color: rgb(223, 223, 223)")

        self.exitbtn = QtWidgets.QPushButton(Dialog)
        self.exitbtn.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.exitbtn.setStyleSheet("background-color: rgb(223, 223, 223);border: 1px solid black; border-radius : 4px}\n""")
        self.exitbtn.setObjectName("exitbtn")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(95, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #biale okienko
        self.widget = QtWidgets.QFrame(Dialog)

        self.widget.setGeometry(QtCore.QRect(50, 70, 300, 230))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);border: 1px solid black;}")
        self.widget.setObjectName("widget")

        self.loginbtn = QtWidgets.QPushButton(self.widget)
        self.loginbtn.setGeometry(QtCore.QRect(100, 182, 100, 35))
        self.loginbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginbtn.setStyleSheet("background-color: rgb(145, 145, 145);border: 1px solid black; border-radius : 4px}\n""")
        #self.loginbtn.setProperty("Color", QtGui.QColor(20, 20, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.loginbtn.setFont(font)
        self.loginbtn.setObjectName("loginbtn")

        self.loginId = QtWidgets.QLineEdit(self.widget)
        self.loginId.setGeometry(QtCore.QRect(50, 50, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginId.setFont(font)
        self.loginId.setStyleSheet("background-color: rgb(245, 245, 245);border: 1px solid black; border-radius : 2px}\n""")
        self.loginId.setObjectName("loginId")

        self.passwordId = QtWidgets.QLineEdit(self.widget)
        self.passwordId.setGeometry(QtCore.QRect(50, 125, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordId.setFont(font)
        self.passwordId.setStyleSheet("background-color: rgb(245, 245, 245);border: 1px solid black; border-radius : 2px}\n""")
        self.passwordId.setObjectName("passwordId")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 19, 47, 31))
        self.label_3.setStyleSheet("border: 0px}\n;")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 94, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 0px}\n;")
        self.label_4.setObjectName("label_4")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 71, 51))

        self.widget.raise_()
        self.exitbtn.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Organizer"))
        self.exitbtn.setText(_translate("Dialog", "Wyjdź"))
        self.label.setText(_translate("Dialog", "Witaj w organizerze"))
        self.loginbtn.setText(_translate("Dialog", "Zaloguj się"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Hasło"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = loginUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())