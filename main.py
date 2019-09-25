from PyQt5 import QtWidgets
from menu import Ui_MainWindow

import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	application = mywindow()
	application.show()

	sys.exit(app.exec())
