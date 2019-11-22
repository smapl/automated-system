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
        MainWindow.resize(1047, 706)
        MainWindow.setStyleSheet("#tabwidget{\n"
"background-color: rgb(208, 251, 179);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabwidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.tabwidget.setStyleSheet("*{\n"
"background-color: rgb(196, 183, 183);\n"
"}")
        self.tabwidget.setObjectName("tabwidget")
        self.Menu = QtWidgets.QWidget()
        self.Menu.setObjectName("Menu")
        self.pushButton = QtWidgets.QPushButton(self.Menu)
        self.pushButton.setGeometry(QtCore.QRect(650, 440, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit_4 = QtWidgets.QTextEdit(self.Menu)
        self.textEdit_4.setGeometry(QtCore.QRect(600, 10, 171, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Menu)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_2 = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.gridLayout.addWidget(self.listWidget_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.gridLayout.addWidget(self.listWidget_3, 0, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(self.Menu)
        self.listWidget_4.setGeometry(QtCore.QRect(600, 70, 171, 341))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.textEdit = QtWidgets.QTextEdit(self.Menu)
        self.textEdit.setGeometry(QtCore.QRect(10, 330, 189, 41))
        self.textEdit.setStyleSheet("*{\n"
"height: 10px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.Menu)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 330, 189, 41))
        self.textEdit_2.setStyleSheet("*{\n"
"height: 10px;\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.Menu)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 330, 181, 41))
        self.textEdit_3.setStyleSheet("*{\n"
"height: 10px;\n"
"}")
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabwidget.addTab(self.Menu, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1047, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuZakaz = QtWidgets.QMenu(self.menubar)
        self.menuZakaz.setObjectName("menuZakaz")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZakaz = QtWidgets.QAction(MainWindow)
        self.actionZakaz.setObjectName("actionZakaz")
        self.menuMenu.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuZakaz.menuAction())

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">Текущий заказ</span></p></body></html>"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Вафля белгийская"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Маффин"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Чизкейк"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "Медовик"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Треугольник с курицей"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "Кальцоне с колбасками "))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "Грилата по-сицилийски"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("MainWindow", "Панини"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Капучино"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Латте"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Гляссе"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Американо"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Эспрессо"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Напитки</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Снеки</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt;\">Десерты</span></p></body></html>"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.Menu), _translate("MainWindow", "Заказ"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuZakaz.setTitle(_translate("MainWindow", "Zakaz"))
        self.actionZakaz.setText(_translate("MainWindow", "Zakaz"))


