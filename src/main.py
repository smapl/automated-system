import sys
from pymongo import MongoClient



from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

from menu import Window_menu
from admin import Window_admin
from waiter import Window_waiter
from guest import Window_guest

mongo_url = "mongodb://127.0.0.1:27017"
client = MongoClient(mongo_url)
db = client.coffee

# # collections for waiter
# collection_open_order = db.open_order
# collection_acting_order = db.acting_order
# collection_close_order = db.close_order

# # collections for guest
# collection_order = db.order

# intermediate_snack_list = []
# intermediate_drink_list = []

# snack_list = []
# drink_list = []


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

        self.guest_form.pushButton.clicked.connect(lambda: self.guest_form.view_eat("Пончик", "donut"))
        self.guest_form.pushButton_2.clicked.connect(lambda: self.guest_form.view_eat("Тирамиссу", "tiramisu"))
        self.guest_form.pushButton_3.clicked.connect(lambda: self.guest_form.view_eat("Кекс", "muffin"))
        self.guest_form.pushButton_4.clicked.connect(lambda: self.guest_form.view_eat("Чизкейк", "cheesecake"))
        self.guest_form.pushButton_5.clicked.connect(lambda: self.guest_form.view_eat("Круассан", "croissant"))
        self.guest_form.pushButton_14.clicked.connect(
            lambda: self.guest_form.formation_basket_eat()
        )

        self.guest_form.pushButton_6.clicked.connect(lambda: self.guest_form.view_drinks("Чай", "tea"))
        self.guest_form.pushButton_7.clicked.connect(lambda: self.guest_form.view_drinks("Раф", "ruf"))
        self.guest_form.pushButton_8.clicked.connect(lambda: self.guest_form.view_drinks("Латте", "latte"))
        self.guest_form.pushButton_9.clicked.connect(lambda: self.guest_form.view_drinks("Капучино", "cappucino"))
        self.guest_form.pushButton_10.clicked.connect(lambda: self.guest_form.view_drinks("Эспрессо", "espresso"))
        self.guest_form.pushButton_13.clicked.connect(
            lambda: self.guest_form.formation_basket_drink()
        )

        self.guest_form.pushButton_12.clicked.connect(lambda: self.guest_form.formation_order())
        self.guest_form.pushButton_11.clicked.connect(lambda: self.guest_form.view_order())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Window_main()
    sys.exit(app.exec())

