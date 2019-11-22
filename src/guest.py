# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guest.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Window_guest(object):
    def setupUi_guest(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("*{\n"
"background-color: rgb(196, 183, 183);\n"
"}")
        MainWindow.resize(1109, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1061, 611))
        self.tabWidget.setStyleSheet("#tab{\n"
"background-color: rgb(255, 240, 245);\n"
"}\n"
"\n"
"#tab_3{\n"
"background-color: rgb(230, 230, 250);\n"
"}\n"
"\n"
"#tab_2{\n"
"background-color: rgb(255, 255, 240);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet(".tab{\n"
"bac    kground-color: rgb(233, 185, 110);\n"
"}")
        self.tab.setObjectName("tab")
        self.listView_2 = QtWidgets.QListView(self.tab)
        self.listView_2.setGeometry(QtCore.QRect(400, 40, 421, 461))
        self.listView_2.setObjectName("listView_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listView_3 = QtWidgets.QListView(self.tab_3)
        self.listView_3.setGeometry(QtCore.QRect(400, 40, 421, 471))
        self.listView_3.setObjectName("listView_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 30, 381, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Еда"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Напитки"))
        self.pushButton.setText(_translate("MainWindow", "Оплатить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Оплата"))


