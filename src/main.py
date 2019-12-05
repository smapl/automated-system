import sys
from pymongo import MongoClient
from collections import Counter


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Window_menu
from admin import Window_admin
from waiter import Window_waiter
from guest import Window_guest

mongo_url = "mongodb://127.0.0.1:27017"
client = MongoClient(mongo_url)
db = client.coffee

# collections for waiter
collection_open_order = db.open_order
collection_acting_order = db.acting_order
collection_close_order = db.close_order

# collections for guest
collection_order = db.order

intermediate_snack_list = []
intermediate_drink_list = []

snack_list = []
drink_list = []


def view_eat(name_snack: str):
    global intermediate_snack_list

    intermediate_snack_list.append(name_snack)
    print(intermediate_snack_list)


def view_drinks(name_drink: str):
    global intermediate_drink_list

    intermediate_drink_list.append(name_drink)
    print(intermediate_drink_list)


def formation_basket_eat(snack: list):
    global intermediate_snack_list

    snack_list.append(snack[-1])
    print(snack_list)
    intermediate_snack_list = []


def formation_basket_drink(drink: list):
    global intermediate_drink_list

    drink_list.append(drink[-1])
    print(drink_list)
    intermediate_drink_list = []


def formation_order():
    global snack_list, drink_list

    snack = Counter(snack_list)
    drink = Counter(drink_list)

    print(snack_list)
    print(drink_list)

    order = {"snacks": snack, "drinks": drink}
    collection_order.insert_one(order)

    intermediate_snack_list = []
    intermediate_drink_list = []

    snack_list = []
    drink_list = []


class Window_main(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        self.menu_form = Window_menu()
        self.menu_form.setupUi_menu(self)
        self.show()

        self.menu_form.pushButton.clicked.connect(self.close)
        self.menu_form.pushButton.clicked.connect(self.admin)

        self.menu_form.pushButton_2.clicked.connect(self.close)
        self.menu_form.pushButton_2.clicked.connect(self.waiter)

        self.menu_form.pushButton_3.clicked.connect(self.close)
        self.menu_form.pushButton_3.clicked.connect(self.guest)

    def admin(self):
        self.admin_form = Window_admin()
        self.admin_form.setupUi_admin(self)
        self.show()

        self.admin_form.pushButton_2.clicked.connect(self.close)
        self.admin_form.pushButton_2.clicked.connect(self.menu)

    def waiter(self):
        self.waiter_form = Window_waiter()
        self.waiter_form.setupUi_waiter(self)
        self.show()

        self.waiter_form.pushButton.clicked.connect(self.close)
        self.waiter_form.pushButton.clicked.connect(self.menu)

    def guest(self):
        self.guest_form = Window_guest()
        self.guest_form.setupUi_guest(self)
        self.show()

        self.guest_form.pushButton_11.clicked.connect(self.close)
        self.guest_form.pushButton_11.clicked.connect(self.menu)

        self.guest_form.pushButton.clicked.connect(lambda: view_eat("Пончик"))
        self.guest_form.pushButton_2.clicked.connect(lambda: view_eat("Тирамиссу"))
        self.guest_form.pushButton_3.clicked.connect(lambda: view_eat("Кекс"))
        self.guest_form.pushButton_4.clicked.connect(lambda: view_eat("Чизкейк"))
        self.guest_form.pushButton_5.clicked.connect(lambda: view_eat("Круассан"))
        self.guest_form.pushButton_14.clicked.connect(
            lambda: formation_basket_eat(intermediate_snack_list)
        )

        self.guest_form.pushButton_6.clicked.connect(lambda: view_drinks("Чай"))
        self.guest_form.pushButton_7.clicked.connect(lambda: view_drinks("Раф"))
        self.guest_form.pushButton_8.clicked.connect(lambda: view_drinks("Латте"))
        self.guest_form.pushButton_9.clicked.connect(lambda: view_drinks("Капучино"))
        self.guest_form.pushButton_10.clicked.connect(lambda: view_drinks("Эспрессо"))
        self.guest_form.pushButton_13.clicked.connect(
            lambda: formation_basket_drink(intermediate_drink_list)
        )

        self.guest_form.pushButton_12.clicked.connect(lambda: formation_order())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Window_main()
    sys.exit(app.exec())

