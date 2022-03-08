from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from random import randint
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 506)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setFont(font)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btngen = QtWidgets.QPushButton(self.centralwidget)
        self.btngen.setGeometry(QtCore.QRect(60, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btngen.setFont(font)
        self.btngen.setObjectName("btngen")
        self.btngen.clicked.connect(self.rand_pass)

        self.btncopy = QtWidgets.QPushButton(self.centralwidget)
        self.btncopy.setGeometry(QtCore.QRect(250, 350, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btncopy.setFont(font)
        self.btncopy.setObjectName("btncopy")
        self.btncopy.clicked.connect(self.copy_pass)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 110, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 220, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
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

    def rand_pass(self):
        self.textEdit_2.setText("")
        generated_pass = ''

        pass_len = int(self.textEdit.toPlainText())

        for i in range(pass_len):
            generated_pass += chr(randint(33, 126))

        self.textEdit_2.setText(f'{generated_pass}')

    def copy_pass(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget#MainWindow {
            background-image: url('bg.svg');
            background-repeat: no-repeat;
            background-size: 100%;
        }
        
        QWidget {
            color: #fff;
        }
        
        QTextEdit {
            border: 2px solid #fff;
            border-radius: 8px;
            color: black;
        }
        
        QPushButton {
            border-radius: 8px;
            background-color: #fff;
            color: black;
            border: 2px solid black;
            transition: .2s;
        }
        
        QPushButton:hover {
            cursor: pointer;
        }
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
