# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guest.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
from collections import Counter

mongo_url = "mongodb://127.0.0.1:27017"
client = MongoClient(mongo_url)
db = client.coffee

# collections for guest
collection_order = db.order
collection_info = db.information_about

intermediate_snack_list = []
intermediate_drink_list = []

snack_list = []
drink_list = []

class Window_guest(object):

        def setupUi_guest(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.setMinimumSize(QtCore.QSize(1109, 694))
                MainWindow.resize(1109, 694)
                MainWindow.setStyleSheet("background-color: rgb(221, 215, 215);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1071, 631))
                self.tabWidget.setStyleSheet("#tab{\n" "    background-color: #fff;\n" "}\n" "")
                self.tabWidget.setObjectName("tabWidget")
                self.tab = QtWidgets.QWidget()
                self.tab.setStyleSheet(
                        "#tab {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        "}\n"
                        "\n"
                        "#pushButton{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    height: 40px;\n"
                        "    border-radius: 0px;\n"
                        "}\n"
                        "\n"
                        "#pushButton::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "#pushButton_2{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 0px;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_2::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_2::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_3{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_3::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_3::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "#pushButton_4{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_4::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_4::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_5{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_5::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_5::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_14{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "    width: 70px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_14::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_14::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}"
                )
                self.tab.setObjectName("tab")
                self.listView = QtWidgets.QListView(self.tab)
                self.listView.setGeometry(QtCore.QRect(360, 90, 351, 411))
                self.listView.setObjectName("listView")
                
                self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 180, 161, 281))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
                self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton.setObjectName("pushButton")
                self.verticalLayout.addWidget(self.pushButton)
                self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_5.setObjectName("pushButton_5")
                self.verticalLayout.addWidget(self.pushButton_5)
                self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_4.setObjectName("pushButton_4")
                self.verticalLayout.addWidget(self.pushButton_4)
                self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_2.setObjectName("pushButton_2")
                self.verticalLayout.addWidget(self.pushButton_2)
                self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
                self.pushButton_3.setObjectName("pushButton_3")
                self.verticalLayout.addWidget(self.pushButton_3)
                self.pushButton_14 = QtWidgets.QPushButton(self.tab)
                self.pushButton_14.setGeometry(QtCore.QRect(478, 514, 141, 41))
                self.pushButton_14.setObjectName("pushButton_14")
                self.label = QtWidgets.QLabel(self.tab)
                self.label.setGeometry(QtCore.QRect(420, 30, 241, 31))
                self.label.setStyleSheet(
                        "#label {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    font-size: 40px;\n"
                        "}"
                )
                self.label.setObjectName("label")
                self.tabWidget.addTab(self.tab, "")
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setStyleSheet(
                        "#tab_2 {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        "}\n"
                        "\n"
                        "#pushButton_10{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    height: 40px;\n"
                        "    border-radius: 0px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_10::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_10::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "#pushButton_6{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 0px;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_6::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_6::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_7{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_7::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_7::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "#pushButton_8{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_8::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_8::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_9{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_9::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_9::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "\n"
                        "#pushButton_13{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    border-radius: 1px solid black;\n"
                        "    height: 40px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_13::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_13::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}"
                )
                self.tab_2.setObjectName("tab_2")
                self.listView_2 = QtWidgets.QListView(self.tab_2)
                self.listView_2.setGeometry(QtCore.QRect(360, 90, 351, 411))
                self.listView_2.setObjectName("listView_2")
                self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
                self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 180, 161, 251))
                self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
                self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
                self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_10.setObjectName("pushButton_10")
                self.verticalLayout_2.addWidget(self.pushButton_10)
                self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_9.setObjectName("pushButton_9")
                self.verticalLayout_2.addWidget(self.pushButton_9)
                self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_8.setObjectName("pushButton_8")
                self.verticalLayout_2.addWidget(self.pushButton_8)
                self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_7.setObjectName("pushButton_7")
                self.verticalLayout_2.addWidget(self.pushButton_7)
                self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                self.pushButton_6.setObjectName("pushButton_6")
                self.verticalLayout_2.addWidget(self.pushButton_6)
                self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
                self.pushButton_13.setGeometry(QtCore.QRect(478, 514, 141, 41))
                self.pushButton_13.setObjectName("pushButton_13")
                self.label_2 = QtWidgets.QLabel(self.tab_2)
                self.label_2.setGeometry(QtCore.QRect(420, 30, 241, 31))
                self.label_2.setStyleSheet(
                        "#label_2 {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    font-size: 40px;\n"
                        "}"
                )
                self.label_2.setObjectName("label_2")
                self.tabWidget.addTab(self.tab_2, "")
                self.tab_3 = QtWidgets.QWidget()
                self.tab_3.setStyleSheet(
                        "#tab_3 {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        "}\n"
                        "\n"
                        "#pushButton_11{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    height: 40px;\n"
                        "    border-radius: 0px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_11::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_11::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        "\n"
                        "#pushButton_12{\n"
                        "    color: #fff;\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    background-color: rgb(85, 87, 83);\n"
                        "    height: 40px;\n"
                        "    border-radius: 0px;\n"
                        "}\n"
                        "\n"
                        "#pushButton_12::hover{\n"
                        "    background-color: rgb(136, 138, 133);\n"
                        "    /*border: 1px solid silver;*/\n"
                        "}\n"
                        "\n"
                        "#pushButton_12::pressed{\n"
                        "    border: 2px solid silver;\n"
                        "}\n"
                        ""
                )
                self.tab_3.setObjectName("tab_3")
                self.listView_3 = QtWidgets.QListView(self.tab_3)
                self.listView_3.setGeometry(QtCore.QRect(360, 90, 351, 411))
                self.listView_3.setObjectName("listView_3")
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 510, 351, 42))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                self.pushButton_11.setObjectName("pushButton_11")
                self.horizontalLayout.addWidget(self.pushButton_11)
                self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                self.pushButton_12.setObjectName("pushButton_12")
                self.horizontalLayout.addWidget(self.pushButton_12)
                self.label_3 = QtWidgets.QLabel(self.tab_3)
                self.label_3.setGeometry(QtCore.QRect(420, 30, 241, 31))
                self.label_3.setStyleSheet(
                        "#label_3 {\n"
                        "    background-color: rgb(151, 151, 151);\n"
                        '    font: 25 11pt "Yrsa";\n'
                        "    font-size: 40px;\n"
                        "}"
                )
                self.label_3.setObjectName("label_3")
                self.tabWidget.addTab(self.tab_3, "")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1109, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Guest"))
                self.pushButton.setText(_translate("MainWindow", "Пончик"))
                self.pushButton_5.setText(_translate("MainWindow", "Круассан"))
                self.pushButton_4.setText(_translate("MainWindow", "Чизкейк"))
                self.pushButton_2.setText(_translate("MainWindow", "Тирамиссу"))
                self.pushButton_3.setText(_translate("MainWindow", "Кекс"))
                self.pushButton_14.setText(_translate("MainWindow", "Выбрать"))
                self.label.setText(_translate("MainWindow", "Time to coffee"))
                self.tabWidget.setTabText(
                        self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Закуски")
                )
                self.pushButton_10.setText(_translate("MainWindow", "Эспрессо"))
                self.pushButton_9.setText(_translate("MainWindow", "Капучино"))
                self.pushButton_8.setText(_translate("MainWindow", "Латте"))
                self.pushButton_7.setText(_translate("MainWindow", "Раф"))
                self.pushButton_6.setText(_translate("MainWindow", "Чай"))
                self.pushButton_13.setText(_translate("MainWindow", "Выбрать"))
                self.label_2.setText(_translate("MainWindow", "Time to coffee"))
                self.tabWidget.setTabText(
                        self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Напитки")
                )
                self.pushButton_11.setText(_translate("MainWindow", "Просмотр"))
                self.pushButton_12.setText(_translate("MainWindow", "Оплатить"))
                self.label_3.setText(_translate("MainWindow", "Time to coffee"))
                self.tabWidget.setTabText(
                        self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Оплата")
                )

        def view_eat(self, name_snack, key_bd):
                global intermediate_snack_list

                for document in collection_info.find({}):
                        text_from_bd = document[key_bd]
                        item = QtGui.QStandardItem(text_from_bd)
                
                self.model = QtGui.QStandardItemModel()  
                self.model.appendRow(item) 
                self.listView.setModel(self.model)
                intermediate_snack_list.append(name_snack)
                print(intermediate_snack_list)


        def view_drinks(self, name_drink, key_bd):
                global intermediate_drink_list
                
                for document in collection_info.find({}):
                        text_from_bd = document[key_bd]
                        item = QtGui.QStandardItem(text_from_bd)

                self.model = QtGui.QStandardItemModel()  
                self.model.appendRow(item) 
                self.listView_2.setModel(self.model)

                intermediate_drink_list.append(name_drink)
                print(intermediate_drink_list)

        def formation_basket_eat(self):
                global intermediate_snack_list

                snack_list.append(intermediate_snack_list[-1])
                print(snack_list)
                intermediate_snack_list = []


        def formation_basket_drink(self):
                global intermediate_drink_list

                drink_list.append(intermediate_drink_list[-1])
                print(drink_list)
                intermediate_drink_list = []

        def view_order(self):
                global snack_list, drink_list, intermediate_drink_list, intermediate_snack_list

                snack = dict(Counter(snack_list))
                drink = dict(Counter(drink_list))
                order = ""
                print(dict(snack))
                print(dict(drink))
                order_list = []
                
                for _ in drink:
                        order = f"{str(drink[_])} x {_} "
                        order_list.append(order)

                for _ in snack:
                        order = f"{str(snack[_])} x {_} " 
                        order_list.append(order)

                self.model = QtGui.QStandardItemModel()  
                for i in order_list:
                        item = QtGui.QStandardItem(i)
                        self.model.appendRow(item)
                        self.listView_3.setModel(self.model)

        def formation_order(self):
                global snack_list, drink_list, intermediate_drink_list, intermediate_snack_list
                
                snack = Counter(snack_list)
                drink = Counter(drink_list)
                order = {"snacks": snack, "drinks": drink}
                collection_order.insert_one(order)

                intermediate_snack_list = []
                intermediate_drink_list = []

                snack_list = []
                drink_list = []



