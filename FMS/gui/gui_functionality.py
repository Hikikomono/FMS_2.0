import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.content_box import ContentBox
from gui.gui_raw import MainGui
from gui.gui_raw import AddBookmarkGui
from Caretaker import Caretaker
from Parser import Parser




class MainView(MainGui):
    def __init__(self):
        super().__init__()

        self.caretaker = Caretaker()
        self.parser = Parser()

        self.spacer_queue = []
        self.search_bar_content = ""

        self.add_bookmark_key = QShortcut(QKeySequence("Ctrl+N"), self)

        self.add_bookmark_key.activated.connect(self.add_bookmark_popup)
        self.add_button.clicked.connect(self.add_bookmark_popup)
        self.tag_list.itemClicked.connect(self.tag_clicked)

    def tag_clicked(self, item):
        """
        when a tag in the "tag_list" (gui) is clicked, this method gets called which inserts the clicked item
        into the "search_bar" (gui)
        """
        if self.search_bar.text().__len__() == 0:
            self.search_bar_content = ""

        self.search_bar_content = self.search_bar_content + " " + QListWidgetItem(item).text()
        self.search_bar.setText(self.search_bar_content)
        print(QListWidgetItem(item).text())  # prints the content of the list item TODO remove

    def add_bookmark_popup(self):
        self.popup = PopupView(self)
        self.popup.show()
        return None


    def init_gui(self): # TODO init_gui function
        """
        calls "add_tags()" and "add_list_item() when program launches to init everything thats in DB"
        """
        return None

    def add_tags(self, tags: list): # TODO add_tags fucntion
        """
        checks if new tags are in the "tags: list" if so, then they are added to "tag_list"
        if they already exist, they are not added
        """
        if tags.__len__() > 0:
            for i in range(tags.__len__()):
                if self.tag_list.findItems(tags[i], Qt.MatchExactly).__len__() == 0:
                    self.tag_list.addItem(tags[i])
                    print("Item is New")
                else:
                    print("Item already in list")

    def add_list_item(self, title: str, url: str, tags: list):
        """
        adds a spacer item, so that added Bookmarks / content_box.py are always at the top of the window
        spacer_queue keeps care that only the most recent added Bookmark / Contentbox has a spacer underneath it
        """
        print(self.spacer_queue.__len__())
        if self.spacer_queue.__len__() > 0:
            self.scroll_layout.removeItem(self.spacer_queue.pop())

        self.scroll_layout.addWidget(ContentBox(title, url, tags))

        self.spacer_queue.append(QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.scroll_layout.addSpacerItem(self.spacer_queue[0])

    # def add_list_item_2(self, list_item: content_box.py):
    #     self.scroll_layout.addWidget(list_item)

    def remove_list_item(self, list_item: ContentBox):  #TODO implement functionality
        self.scroll_layout.removeWidget(list_item)


class PopupView(AddBookmarkGui):
    def __init__(self, parent: MainGui):
        super().__init__()
        self.parent = parent

        #event / signals
        self.enter_key_add.activated.connect(self.get_input)
        self.esc_key_close.activated.connect(self.close)

        self.add_button.clicked.connect(self.get_input)
        self.cancel_button.clicked.connect(self.close)

    def get_input(self):
        """
        gets entered variales and passes them to "add_list_item" whichs adds a new content_box.py object / item to
        the main window (gui). If "title"-length < 2 or "url"-length < 5 and the "Add" button on the popup
        is pressed, then no new item is added, the popup just closes

        splits the tags (seperated with " ") into seperate strings -> returns a list which gets passed to
        "add_tags" (gui) method
        """
        if not(self.title_input.text().__len__() < 2 or self.url_input.text().__len__() < 5):
            self.parent.add_list_item(self.title_input.text(), self.url_input.text(), self.tags_input.text())

            print(self.tags_input.text().split())
            self.parent.add_tags(self.tags_input.text().split(" "))

            print(self.title_input.text() + "\n" +
                  self.url_input.text() + "\n" +
                  self.tags_input.text())

        self.close()



app = QApplication(sys.argv)
# app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = MainView()
window.show()
app.exec_()


