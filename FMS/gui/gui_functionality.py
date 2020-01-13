import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.content_box import ContentBox
from gui.gui_raw import MainGui
from gui.gui_raw import AddBookmarkGui
from Caretaker import Caretaker
from Parser import Parser
from Bookmark import Bookmark

import requests
from bs4 import BeautifulSoup




class MainView(MainGui):
    def __init__(self):
        super().__init__()

        self.caretaker = Caretaker()
        self.parser = Parser()
        self.content_box_list = []  # ContentBox

        self.spacer_queue = []
        self.search_bar_content = ""

        self.add_bookmark_key = QShortcut(QKeySequence("Ctrl+N"), self)
        self.enter_key_add = QShortcut(QKeySequence(Qt.Key_Return), self.search_bar)

        self.enter_key_add.activated.connect(self.search_bookmark)

        self.add_bookmark_key.activated.connect(self.add_bookmark_popup)
        self.add_button.clicked.connect(self.add_bookmark_popup)
        self.tag_list.itemClicked.connect(self.tag_clicked)
        self.sync_button.clicked.connect(self.sync_plugin)
        self.search_button.clicked.connect(self.search_bookmark)

        self.search_button.clicked.connect(self.search_bookmark)

    def tag_clicked(self, item):
        """
        when a tag in the "tag_list" (gui) is clicked, this method gets called which inserts the clicked item
        into the "search_bar" (gui)
        """
        if self.search_bar.text().__len__() == 0:
            self.search_bar_content = ""

        self.search_bar_content = self.search_bar_content + " " + QListWidgetItem(item).text()
        self.search_bar.setText(self.search_bar_content)

    def add_bookmark_popup(self):
        self.popup = PopupView(self)
        self.popup.show()
        return None

    def search_bookmark(self):
        """searches content_box_list bookmarks for their tags and titles to match the input of the searchbar"""
        # print(self.search_bar.text())
        # self.search_bar.setText(self.search_bar_content)

        elements = self.search_bar.text().split()
        filtered_content_box_list = []  # hier kommen gefundene Objekte rein
        # print(len(elements))

        # darstellen falls keine suche eingegeben wurde
        if len(elements) == 0:
            print("keine elemente")
            for content in self.content_box_list:
                content.show()

        else:

            for element in elements:
                for content in self.content_box_list:
                    if element in content.tags:
                        filtered_content_box_list.append(content)
                        # print(content.tags)

            # delete layout content
            for content in self.content_box_list:
                content.close()

            for content in filtered_content_box_list:
                content.show()

    def sync_plugin(self):
        old_count = self.caretaker.bookmark_list.__len__()
        self.parser.get_bookmarks()
        self.caretaker.get_list()
        new_count = self.caretaker.bookmark_list.__len__()
        print("old: " + str(old_count) + "| new: " + str(new_count))

        for i in range(old_count, new_count):
            #Contenbox erstellen
            self.content_box_list.append(ContentBox(self.caretaker.bookmark_list[i], self.content_box_list, self.caretaker))
            print(Bookmark(self.content_box_list[-1].bookmark.title))
            #contentbox zu content_box_list adden

            if self.spacer_queue.__len__() > 0:
                self.scroll_layout.removeItem(self.spacer_queue.pop())

            self.scroll_layout.addWidget(self.content_box_list[-1])

            self.spacer_queue.append(QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))
            self.scroll_layout.addSpacerItem(self.spacer_queue[0])

        # delete layout content
        for content in self.content_box_list:
            content.close()

        for content in self.content_box_list:
            content.show()

    def init_gui(self):
        """
        calls "add_tags()" and "add_list_item() when program launches to init everything thats in DB"
        """
        self.caretaker.get_list()
        self.parser.get_bookmarks()
        popup = PopupView(self)
        self.caretaker.get_list()
        popup.init_content(self.caretaker.bookmark_list)

    def add_tags(self, tags: list):
        """
        checks if new tags are in the "tags: list" if so, then they are added to "tag_list"
        if they already exist, they are not added
        """
        if tags.__len__() > 0:
            for i in range(tags.__len__()):
                if self.tag_list.findItems(tags[i], Qt.MatchExactly).__len__() == 0:
                    self.tag_list.addItem(tags[i])

    def add_list_item(self, title: str, url: str, comment: str, tags: list):
        """
        adds a spacer item, so that added Bookmarks / content_box.py are always at the top of the window
        spacer_queue keeps care that only the most recent added Bookmark / Contentbox has a spacer underneath it
        """
        if self.spacer_queue.__len__() > 0:
            self.scroll_layout.removeItem(self.spacer_queue.pop())

        self.caretaker.add_bookmark(None, title, url, comment, None, tags)
        self.content_box_list.append(ContentBox(self.caretaker.bookmark_list[-1], self.content_box_list, self.caretaker))
        self.scroll_layout.addWidget(self.content_box_list[-1])

        self.spacer_queue.append(QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.scroll_layout.addSpacerItem(self.spacer_queue[0])

    def init_list_item(self, bookmark: Bookmark):
        if self.spacer_queue.__len__() > 0:
            self.scroll_layout.removeItem(self.spacer_queue.pop())

        self.content_box_list.append(ContentBox(bookmark, self.content_box_list, self.caretaker))
        self.scroll_layout.addWidget(self.content_box_list[-1])

        self.spacer_queue.append(QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.scroll_layout.addSpacerItem(self.spacer_queue[0])



class PopupView(AddBookmarkGui):
    def __init__(self, parent: MainGui):
        super().__init__()
        self.parent = parent


        #keyboard shortcuts to close popup / add bookmark
        self.enter_key_add = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.esc_key_close = QShortcut(QKeySequence(Qt.Key_Escape), self)
        # event / signals
        self.enter_key_add.activated.connect(self.get_input)
        self.esc_key_close.activated.connect(self.close)

        self.add_button.clicked.connect(self.get_input)
        self.cancel_button.clicked.connect(self.close)
        self.url_input.textChanged.connect(self.add_url_title)

    def get_input(self):
        """
        gets entered variales and passes them to "add_list_item" whichs adds a new content_box.py object / item to
        the main window (gui). If "title"-length < 2 or "url"-length < 5 and the "Add" button on the popup
        is pressed, then no new item is added, the popup just closes

        splits the tags (seperated with " ") into seperate strings -> returns a list which gets passed to
        "add_tags" (gui) method
        """
        if not (self.title_input.text().__len__() < 2 or self.url_input.text().__len__() < 5):
            tags = self.tags_input.text()

            self.parent.add_list_item(self.title_input.text(), self.url_input.text(), self.comment_input.text(),
                                      tags.replace(" ", "").split(","))  # tags.split = tagliste

            print(self.tags_input.text().split())
            self.parent.add_tags(tags.replace(" ", "").split(","))

            print(self.title_input.text() + "\n" +
                  self.url_input.text() + "\n" +
                  self.tags_input.text())

        self.close()

    def init_content(self, bookmarks: list):
        for bookmark in bookmarks:
            self.parent.init_list_item(bookmark)
            self.parent.add_tags(bookmark.tags)

    def add_url_title(self):
        if self.title_input.text().__len__() == 0 and self.url_input.text().__contains__("http"):
            url_tile = self.get_url_title(self.url_input.text())
            self.title_input.setText(url_tile)


    def get_url_title(self, url: str):
        # issue http request to create request object
        try:
            http_request = requests.get(url)
            # extract the text out of the request object
            http_text = http_request.text
            # create BeautifulSoup object with content of the website and define a parser
            soup = BeautifulSoup(http_text, "html.parser")
            # extract the _title_ of the webpage & print it
            article_title = soup.title.string
            return article_title
        except: #eine Übergangslösung weil .. =)
            None

