"""Just for Testing purposes"""

from DbController import DbController
from gui.gui_functionality import MainView
from PyQt5.QtWidgets import *
import sys


db = DbController()
db.init_tables()

app = QApplication(sys.argv)
window = MainView()
window.init_gui()
window.show()
app.exec_()


