from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.setFixedSize(QSize(400, 420))
        Form.setStyleSheet("background-color:#424242")

        # Napis
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(125, 40, 185, 40))
        self.label.setStyleSheet("background-color: white; color: #717171\n")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # okienko

        self.widget = QtWidgets.QFrame(Form)

        self.widget.setGeometry(QtCore.QRect(50, 40, 300, 340))
        self.widget.setStyleSheet("background-color: white;border: 1px solid white; border-radius : 6px")
        self.widget.setObjectName("widget")

        # przycisk

        self.addbtn = QtWidgets.QPushButton(self.widget)
        self.addbtn.setGeometry(QtCore.QRect(80, 300, 130, 25))
        self.addbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addbtn.setStyleSheet(
            "background-color: #717171;border: 1px solid white ;border-radius : 6px; color:#ffffff\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.addbtn.setFont(font)
        self.addbtn.setObjectName("loginbtn")

        # przycisk cofnij

        self.backbtn = QtWidgets.QPushButton(self.widget)
        self.backbtn.setGeometry(QtCore.QRect(10, 10, 20, 20))
        self.backbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backbtn.setIcon(QIcon('back.png'))
        self.backbtn.setObjectName("backbtn")

        # loginWPIS

        self.loginId = QtWidgets.QLineEdit(self.widget)
        self.loginId.setGeometry(QtCore.QRect(40, 190, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginId.setFont(font)
        self.loginId.setStyleSheet(
            "background-color: #717171;border: 1px solid white ;border-radius : 6px; color:white\n")
        self.loginId.setObjectName("loginId")

        # hasloWPIS

        self.passwordId = QtWidgets.QLineEdit(self.widget)
        self.passwordId.setEchoMode(QLineEdit.Password)
        self.passwordId.setGeometry(QtCore.QRect(40, 250, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordId.setFont(font)
        self.passwordId.setStyleSheet(
            "background-color:#717171;border: 1px solid white ;border-radius : 6px; color:white\n")
        self.passwordId.setObjectName("passwordId")

        # Login
        self.login = QtWidgets.QLabel(self.widget)
        self.login.setGeometry(QtCore.QRect(40, 168, 56, 22))
        self.login.setStyleSheet("background-color: white;color:#717171\n")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.login.setFont(font)
        self.login.setObjectName("login")

        # Haslo
        self.password = QtWidgets.QLabel(self.widget)
        self.password.setGeometry(QtCore.QRect(40, 230, 56, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: white;color:#717171\n")
        self.password.setObjectName("haslo")

        # imie

        self.nameId = QtWidgets.QLineEdit(self.widget)
        self.nameId.setGeometry(QtCore.QRect(40, 60, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameId.setFont(font)
        self.nameId.setStyleSheet(
            "background-color: #717171;border: 1px solid white ;border-radius : 6px; color:white\n")
        self.nameId.setObjectName("nameId")

        # nazwisko

        self.secondId = QtWidgets.QLineEdit(self.widget)
        self.secondId.setGeometry(QtCore.QRect(40, 125, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secondId.setFont(font)
        self.secondId.setStyleSheet(
            "background-color:#717171;border: 1px solid white ;border-radius : 6px; color:white\n")
        self.secondId.setObjectName("secondId")

        # imie
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setGeometry(QtCore.QRect(40, 35, 56, 22))
        self.name.setStyleSheet("background-color: white;color:#717171\n")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setObjectName("name")

        # nazwisko
        self.second = QtWidgets.QLabel(self.widget)
        self.second.setGeometry(QtCore.QRect(40, 100, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.second.setFont(font)
        self.second.setStyleSheet("background-color: white;color:#717171\n")
        self.second.setObjectName("second")

        self.widget.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " REJESTRACJA"))
        self.addbtn.setText(_translate("Form", "Zaloz konto"))
        self.login.setText(_translate("Form", "Login"))
        self.password.setText(_translate("Form", "Hasło"))
        self.name.setText(_translate("Form", "Imie"))
        self.second.setText(_translate("Form", "Nazwisko"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
