import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Window_menu
from admin import Window_admin
from waiter import Window_waiter
from guest import Window_guest


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
        self.guest_form.pushButton.clicked.connect(self.close)
        self.guest_form.pushButton.clicked.connect(self.menu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Window_main()
    sys.exit(app.exec())

