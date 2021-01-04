from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Kalendarz")
        self.setFixedSize(QSize(500, 420))
        Form.setStyleSheet("background-image: url(g2.jpg)")

        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 400, 420))
        self.calendarWidget.setObjectName("calendarWidget")
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        QtCore.QMetaObject.connectSlotsByName(Form)

        #przycisk wylogowania
        self.quitbtn = QtWidgets.QPushButton(Form)
        self.quitbtn.setGeometry(QtCore.QRect(400, 210, 100, 210))
        self.quitbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quitbtn.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.quitbtn.setFont(font)
        self.quitbtn.setObjectName("quitbtn")

        #przycisk do wszystkich zadań
        self.taskbtn = QtWidgets.QPushButton(Form)
        self.taskbtn.setGeometry(QtCore.QRect(400, 0, 100, 210))
        self.taskbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.taskbtn.setStyleSheet("background-image: url(black.png);border: 1px solid white ;border-radius : 6px; color:white\n""")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.taskbtn.setFont(font)
        self.taskbtn.setObjectName("taskbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Calendar", "Kalendarz"))
        self.quitbtn.setText(_translate("Form", "Zakoncz"))
        self.taskbtn.setText(_translate("Form", "Wszystkie\nzadania"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
