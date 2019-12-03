# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window_menu(QWidget):
    def setupUi_menu(self, Form):
        Form.setObjectName("Menu")
        Form.resize(469, 212)
        Form.setMaximumSize(QtCore.QSize(469, 212))
        Form.setStyleSheet(
            "QPushButton{\n"
            "    color: #fff;\n"
            "    background-color: rgb(71, 69, 69);\n"
            "    width: 40px;\n"
            "    height: 30px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "QPushButton::hover{\n"
            "    background-color: rgb(85, 87, 83);\n"
            "}\n"
            "\n"
            "*{\n"
            "    background-color: rgb(196, 183, 183);\n"
            "}\n"
            ""
        )
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 421, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 170, 441, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 441, 21))
        self.line_2.setStyleSheet(
            "QPushButton {\n" "    background-color: rgb(136, 138, 133);\n" "}"
        )
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Menu"))
        self.pushButton.setText(_translate("Form", "Администратор"))
        self.pushButton_2.setText(_translate("Form", "Официант"))
        self.pushButton_3.setText(_translate("Form", "Гость"))

