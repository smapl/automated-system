# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'officiant.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Window_waiter(object):
    def setupUi_waiter(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1047, 706))
        MainWindow.resize(1047, 706)
        MainWindow.setStyleSheet(
            "#tabwidget{\n" "background-color: rgb(208, 251, 179);\n" "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabwidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.tabwidget.setStyleSheet(
            "*{\n" "background-color: rgb(211, 215, 207);\n" "}"
        )
        self.tabwidget.setObjectName("tabwidget")
        self.Menu = QtWidgets.QWidget()
        self.Menu.setStyleSheet(
            "#pushButton{\n"
            "    color: #fff;\n"
            "    font: 25 11pt Yrsa;\n"
            "    background-color: rgb(85, 87, 83);\n"
            "    height: 40px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "#pushButton::hover{\n"
            "    background-color: rgb(136, 138, 133);\n"
            "}\n"
            "\n"
            "#pushButton::pressed{\n"
            "    border: 2px solid silver;\n"
            "}\n"
            "\n"
            "#pushButton_2{\n"
            "    color: #fff;\n"
            "    font: 25 11pt Yrsa;\n"
            "    background-color: rgb(85, 87, 83);\n"
            "    height: 40px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "\n"
            "#pushButton_2::hover{\n"
            "    background-color: rgb(136, 138, 133);\n"
            "}\n"
            "\n"
            "#pushButton_2::pressed{\n"
            "    border: 2px solid silver;\n"
            "}\n"
            ""
        )
        self.Menu.setObjectName("Menu")
        self.listView = QtWidgets.QListView(self.Menu)
        self.listView.setGeometry(QtCore.QRect(250, 40, 256, 311))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.Menu)
        self.listView_2.setGeometry(QtCore.QRect(520, 40, 256, 311))
        self.listView_2.setObjectName("listView_2")
        self.listWidget = QtWidgets.QListWidget(self.Menu)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 221, 311))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.Menu)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 360, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabwidget.addTab(self.Menu, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZakaz = QtWidgets.QAction(MainWindow)
        self.actionZakaz.setObjectName("actionZakaz")

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guest"))
        self.pushButton.setText(_translate("MainWindow", "Принять заказ"))
        self.pushButton_2.setText(_translate("MainWindow", "Сдать заказ"))
        self.tabwidget.setTabText(
            self.tabwidget.indexOf(self.Menu), _translate("MainWindow", "Заказ")
        )
        self.actionZakaz.setText(_translate("MainWindow", "Zakaz"))

