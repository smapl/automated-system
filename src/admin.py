# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window_admin(QWidget):
    def setupUi_admin(self, MainWindow):
        MainWindow.setObjectName("Admin")
        # MainWindow.resize(1102, 694)
        # MainWindow.move(0, 0)
        MainWindow.resize(1102, 694)
        MainWindow.setMinimumSize(QtCore.QSize(1102, 694))
        MainWindow.setMaximumSize(QtCore.QSize(1500, 800))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet(
            "QMainWindow {\n"
            "background-color: rgb(221, 215, 215);"
            "}\n"
            "\n"
            "QTabWidget {\n"
            "    font-size: 18px;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1081, 671))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(
            "#tab_3 {\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: rgb(151, 151, 151);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "#tab_2 {\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: rgb(151, 151, 151);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "#tab {\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: rgb(151, 151, 151);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: rgb(0, 0, 0);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "QRadioButton {\n"
            "    color: rgb(0, 0, 0);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    color: rgb(0, 0, 0);\n"
            "    font-size: 15px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 1px solid rgb(17, 3, 63);\n"
            "}\n"
            "QPushButton {\n"
            "    color: rgb(0, 0, 0);\n"
            "    background-color: rgb(255, 223, 194);\n"
            "    font-size: 15px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color:rgb(216, 189, 155);\n"
            "}"
        )
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(30, 60, 291, 51))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_14)
        self.lineEdit_14.setStyleSheet("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_10.addWidget(self.lineEdit_14)
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(30, 110, 291, 51))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_18)
        self.label_18.setStyleSheet("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_18)
        self.lineEdit_15.setStyleSheet("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.horizontalLayout_15.addWidget(self.lineEdit_15)
        self.horizontalLayoutWidget_19 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(30, 160, 291, 51))
        self.horizontalLayoutWidget_19.setObjectName("horizontalLayoutWidget_19")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_19)
        self.label_24.setStyleSheet("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_19.addWidget(self.label_24)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_19)
        self.lineEdit_16.setStyleSheet("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_19.addWidget(self.lineEdit_16)
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(30, 10, 311, 41))
        self.label_25.setStyleSheet("font-size: 30px;")
        self.label_25.setObjectName("label_25")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 240, 121, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 310, 121, 41))
        self.pushButton_6.setStyleSheet("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(350, 0, 21, 611))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 60, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 110, 311, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 210, 311, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalLayoutWidget_3)
        self.dateEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(35, 0, 0);\n"
            "font-size: 15px;"
        )
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 191, 41))
        self.label_4.setStyleSheet("font-size: 18px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 300, 171, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(210, 300, 231, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(30, 160, 311, 51))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_11.addWidget(self.lineEdit_3)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 410, 181, 31))
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(230, 450, 211, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_7.addWidget(self.lineEdit_9)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(30, 500, 111, 51))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_8.addWidget(self.lineEdit_8)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(150, 500, 211, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_12.setStyleSheet("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(600, 62, 151, 41))
        self.label_17.setStyleSheet("font-size: 18px;")
        self.label_17.setObjectName("label_17")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(30, 450, 191, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(30, 550, 331, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_11)
        self.lineEdit_10.setStyleSheet("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_12.addWidget(self.lineEdit_10)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(600, 152, 361, 51))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.label_19.setStyleSheet("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_13.addWidget(self.label_19)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_12)
        self.lineEdit_12.setStyleSheet("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_13.addWidget(self.lineEdit_12)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(600, 252, 361, 51))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_20 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        self.label_20.setStyleSheet("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_14.addWidget(self.label_20)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_13)
        self.lineEdit_13.setStyleSheet("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_14.addWidget(self.lineEdit_13)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(600, 102, 221, 51))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_22 = QtWidgets.QLabel(self.horizontalLayoutWidget_15)
        self.label_22.setStyleSheet("")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_16.addWidget(self.label_22)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_16.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_15)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_16.addWidget(self.radioButton)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(600, 202, 401, 51))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_23 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        self.label_23.setStyleSheet("")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_17.addWidget(self.label_23)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_4.setStyleSheet("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_17.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_5.setStyleSheet("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_17.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_16)
        self.radioButton_6.setStyleSheet("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_17.addWidget(self.radioButton_6)
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(30, 350, 411, 51))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_17)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_18.addWidget(self.label_7)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_17)
        self.lineEdit_11.setStyleSheet("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_18.addWidget(self.lineEdit_11)
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(600, 320, 121, 41))
        self.label_21.setStyleSheet("\n" "font-size: 18px;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayoutWidget_22 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_22.setGeometry(QtCore.QRect(600, 360, 361, 51))
        self.horizontalLayoutWidget_22.setObjectName("horizontalLayoutWidget_22")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_22)
        self.label_28.setStyleSheet("")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_23.addWidget(self.label_28)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_22)
        self.lineEdit_19.setStyleSheet("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.horizontalLayout_23.addWidget(self.lineEdit_19)
        self.horizontalLayoutWidget_23 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_23.setGeometry(QtCore.QRect(600, 460, 181, 51))
        self.horizontalLayoutWidget_23.setObjectName("horizontalLayoutWidget_23")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_23)
        self.label_29.setStyleSheet("")
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_24.addWidget(self.label_29)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_23)
        self.lineEdit_20.setStyleSheet("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.horizontalLayout_24.addWidget(self.lineEdit_20)
        self.horizontalLayoutWidget_24 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_24.setGeometry(QtCore.QRect(600, 410, 361, 51))
        self.horizontalLayoutWidget_24.setObjectName("horizontalLayoutWidget_24")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_30 = QtWidgets.QLabel(self.horizontalLayoutWidget_24)
        self.label_30.setStyleSheet("")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_25.addWidget(self.label_30)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_24)
        self.lineEdit_21.setStyleSheet("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_25.addWidget(self.lineEdit_21)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(680, 550, 121, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 550, 121, 41))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 511, 41))
        self.label_10.setStyleSheet("font-size: 30px;")
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Статистика")
        )
        self.label_9.setText(_translate("MainWindow", "Имя:"))
        self.label_18.setText(_translate("MainWindow", "Фамилия:"))
        self.label_24.setText(_translate("MainWindow", "ID сотрудника:"))
        self.label_25.setText(_translate("MainWindow", "Просмотр персонала"))
        self.pushButton_5.setText(_translate("MainWindow", "Найти"))
        self.pushButton_6.setText(_translate("MainWindow", "Выход"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            _translate("MainWindow", "Просмотр персонала"),
        )
        self.label.setText(_translate("MainWindow", "Имя:"))
        self.label_2.setText(_translate("MainWindow", "Фамилия:"))
        self.label_3.setText(_translate("MainWindow", "Дата рождения:"))
        self.label_4.setText(_translate("MainWindow", "Паспортные данные"))
        self.label_5.setText(_translate("MainWindow", "Серия:"))
        self.label_6.setText(_translate("MainWindow", "Номер:"))
        self.label_11.setText(_translate("MainWindow", "Отчество:"))
        self.label_8.setText(_translate("MainWindow", "Адрес проживания"))
        self.label_13.setText(_translate("MainWindow", "Улица:"))
        self.label_15.setText(_translate("MainWindow", "Дом:"))
        self.label_12.setText(_translate("MainWindow", "Корпус / строение:"))
        self.label_17.setText(_translate("MainWindow", "Образование"))
        self.label_14.setText(_translate("MainWindow", "Город:"))
        self.label_16.setText(_translate("MainWindow", "Почтовый индекс:"))
        self.label_19.setText(_translate("MainWindow", "Название ВУЗа:"))
        self.label_20.setText(_translate("MainWindow", "Специальность:"))
        self.label_22.setText(_translate("MainWindow", "Статус:"))
        self.radioButton_2.setText(_translate("MainWindow", "Учусь"))
        self.radioButton.setText(_translate("MainWindow", "Не учусь"))
        self.label_23.setText(_translate("MainWindow", "Форма обучения:"))
        self.radioButton_4.setText(_translate("MainWindow", "Очная"))
        self.radioButton_5.setText(_translate("MainWindow", "Очно-заочная"))
        self.radioButton_6.setText(_translate("MainWindow", "Заочная"))
        self.label_7.setText(_translate("MainWindow", "Место рождения:"))
        self.label_21.setText(_translate("MainWindow", "Опыт работы"))
        self.label_28.setText(_translate("MainWindow", "Место работы:"))
        self.label_29.setText(_translate("MainWindow", "Стаж:"))
        self.label_30.setText(_translate("MainWindow", "Должность:"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))
        self.label_10.setText(_translate("MainWindow", "Добавление нового сотрудника"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            _translate("MainWindow", "Добавление персонала"),
        )

