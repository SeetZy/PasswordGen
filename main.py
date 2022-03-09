from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QCursor
from random import randint
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 652)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setFont(font)
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 80, 391, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.btngen = QtWidgets.QPushButton(self.centralwidget)
        self.btngen.setGeometry(QtCore.QRect(60, 400, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btngen.setFont(font)
        self.btngen.setObjectName("btngen")
        self.btngen.clicked.connect(self.rand_pass)
        self.btngen.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btncopy = QtWidgets.QPushButton(self.centralwidget)
        self.btncopy.setGeometry(QtCore.QRect(250, 400, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btncopy.setFont(font)
        self.btncopy.setObjectName("btncopy")
        self.btncopy.clicked.connect(self.copy_pass)
        self.btncopy.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 120, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 160, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 290, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 250, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.btngen.setText(_translate("MainWindow", "Generate Password"))
        self.btncopy.setText(_translate("MainWindow", "Copy To Clipboard"))
        self.label.setText(_translate("MainWindow", "Enter the length of the password"))
        self.label_2.setText(_translate("MainWindow", "Generated Password"))

    def rand_pass(self):
        self.textEdit_2.setText("")
        self.generated_pass = ''

        pass_len = int(self.textEdit.toPlainText())

        for i in range(pass_len):
            self.generated_pass += chr(randint(33, 126))
            self.textEdit_2.setText(f'{self.generated_pass}')
            self.btncopy.setText("Copy To Clipboard")

    def copy_pass(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.generated_pass, mode=cb.Clipboard)

        self.btncopy.setText("Copied!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    css = "style.css"
    with open(css, "r") as fh:
        app.setStyleSheet(fh.read())
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
