from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLineEdit


class loginUI(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Organizer")
        Dialog.resize(400, 420)
        Dialog.setMouseTracking(False)

        Dialog.setStyleSheet("background-image: url(login.png)")

        #Napis
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 90, 185, 40))
        self.label.setStyleSheet("background-image: url(black.png);color:white\n")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #okienko

        self.widget = QtWidgets.QFrame(Dialog)

        self.widget.setGeometry(QtCore.QRect(70, 70, 260, 280))
        self.widget.setStyleSheet("background-image: url(black.png);border-radius : 6px")
        self.widget.setObjectName("widget")

        #przycisk

        self.loginbtn = QtWidgets.QPushButton(self.widget)
        self.loginbtn.setGeometry(QtCore.QRect(60, 210, 130, 25))
        self.loginbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginbtn.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.loginbtn.setFont(font)
        self.loginbtn.setObjectName("loginbtn")

        #przycisk rejestracji

        self.newbtn = QtWidgets.QPushButton(self.widget)
        self.newbtn.setGeometry(QtCore.QRect(30, 255, 200, 25))
        self.newbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newbtn.setStyleSheet("color:white\n")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.newbtn.setFont(font)
        self.newbtn.setObjectName("newbtn")

        #loginWPIS

        self.loginId = QtWidgets.QLineEdit(self.widget)
        self.loginId.setGeometry(QtCore.QRect(40, 95, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginId.setFont(font)
        self.loginId.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n")
        self.loginId.setObjectName("loginId")

        #hasloWPIS

        self.passwordId = QtWidgets.QLineEdit(self.widget)
        self.passwordId.setEchoMode(QLineEdit.Password)
        self.passwordId.setGeometry(QtCore.QRect(40, 155, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordId.setFont(font)
        self.passwordId.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n")
        self.passwordId.setObjectName("passwordId")

        #Login
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(45, 80, 56, 25))
        self.label_3.setStyleSheet("background-image: url(black.png);color:white\n")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        #Haslo
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(45, 140, 56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-image: url(black.png);color:white\n")
        self.label_4.setObjectName("label_4")

        self.widget.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Organizer"))
        self.label.setText(_translate("Dialog", "  ORGANIZER"))
        self.loginbtn.setText(_translate("Dialog", "Zaloguj"))
        self.newbtn.setText(_translate("Dialog", "Nie masz konta? Zarejestruj sie!"))
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
