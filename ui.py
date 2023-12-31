# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from random import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(264, 327)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text1 = QtWidgets.QLabel(self.centralwidget)
        self.Text1.setGeometry(QtCore.QRect(50, 20, 158, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Text1.setFont(font)
        self.Text1.setObjectName("Text1")
        self.NewText = QtWidgets.QLabel(self.centralwidget)
        self.NewText.setGeometry(QtCore.QRect(70, 70, 114, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewText.setFont(font)
        self.NewText.setObjectName("NewText")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 100, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 130, 174, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(90, 190, 81, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Generate.setFont(font)
        self.Generate.setStyleSheet("border: 2px;\n"
"border-radius: 10px;\n"
"background-color: #fbb900;\n"
"color: white;")
        self.Generate.setObjectName("Generate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.Generate.clicked.connect(self.generator)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Text1.setText(_translate("MainWindow", "Генератор паролів"))
        self.NewText.setText(_translate("MainWindow", "Тут буде результат"))
        self.checkBox.setText(_translate("MainWindow", "Використовувати числа"))
        self.checkBox_2.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.Generate.setText(_translate("MainWindow", "Згенерувати"))

    def generator(self):
        
        if self.checkBox_2.isChecked():
            password = ""
            n = randint(8, 16)
            abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            for n in range(n):
                n1= randint(0, len(abc)-1)
                n2= randint(1,2)
                if n2 ==1:
                    password += abc[n1].upper()
                else:
                    password += abc[n1]
            self.NewText.setText(password)


        if self.checkBox.isChecked():
            password = ""
            n = randint(8, 16)
            for n in range(n):
                num = randint(0, 9)
                password += str(num)

            self.NewText.setText(password)

        if self.checkBox_2.isChecked and self.checkBox.isChecked():
            if self.checkBox_2.isChecked():
                password = ""
                n = randint(8, 16)
                abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
                for n in range(n):
                    n1= randint(0, len(abc)-1)
                    n2= randint(1,3)
                    if n2 ==1:
                        password += abc[n1].upper()
                    elif n2 == 2:
                        num = randint(0, 9)
                        password += str(num)
                        
                    else:
                        password += abc[n1]
                self.NewText.setText(password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




