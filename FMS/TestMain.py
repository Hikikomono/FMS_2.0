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





# test = DbController()
# test.init_tables()
#
# parser = Parser()
# carer = Caretaker()
# carer.get_list()
# parser.get_bookmarks() #TODO: krieg ich diese method irnwie in den Caretaker? ws nicht weil sie eine instanz von caretaker aufruft
# # bookmark1 = Bookmark(1, "lala", "url", "comment","picture", ["list"])
#
#
# carer.add_bookmark(None, "My first entry", "www.sex.at", "my comment111", None, ["lulu", "gaga"])
# carer.add_bookmark(None, "My second entry", "www.sex.lulu", "my comment222", None, ["pipi", "vagai"])
# carer.add_bookmark(None, "My 3rd entry", "www.lel.at", "my comment333", None, ["lulu", "gaga"])
# carer.add_bookmark(None, "My 4th entry", "www.4.at", "my comment444", None, ["istan", "bul", "rool", "woool", "swool"])
#
# test = platform
# print(test)
#
# # test deleting bookmark locally & from DB
# #carer.get_list()
# #print(carer.bookmark_list[-1].title)
# #carer.delete_bookmark(carer.bookmark_list[-1])
#
# # carer.delete_bookmark(carer.bookmark_list[1])
#
# # for elements in carer.bookmark_list:
# #    print(elements.id)
#
# print(carer.bookmark_list[-1].id)


