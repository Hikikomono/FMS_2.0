import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Bookmark import Bookmark
from Caretaker import Caretaker

class ContentBox(QFrame):
    def __init__(self, bookmark: Bookmark, content_box_list: list, caretaker: Caretaker):
        super().__init__()

        #todo remove id prints------
        self.bookmark = bookmark
        self.caretaker = caretaker
        self.content_box_list = content_box_list
        print(id(bookmark))
        print(id(self.bookmark))
        print(id(caretaker))
        print(id(self.caretaker))
        ##todo remove id prints------

        self.title = bookmark.title
        self.url = bookmark.url
        self.comment = bookmark.comment
        self.tags = bookmark.tags   #list

        self.remove_button = QPushButton("x")
        self.remove_button.setFixedSize(10,20)
        self.remove_button.setObjectName("remove_button")
        self.remove_button.clicked.connect(self.remove_contentbox)

        link_markup = f'<a href="{self.url}"><span style="color:green;">{self.url}</span></a>'

        frame_layout = QVBoxLayout()
        self.setLayout(frame_layout)
        self.setFrameShape(QFrame.Box)

        title = QLabel("Title: " + self.title)
        url = QLabel("URL: " + link_markup)
        url.setOpenExternalLinks(True)
        comment = QLabel("Comment: " + self.comment)
        tags = QLabel("Tags: " +''.join(self.tags))

        self.remove_widget = QWidget()
        self.remove_layout = QHBoxLayout()
        self.remove_layout.setContentsMargins(0,0,0,0)
        self.remove_widget.setLayout(self.remove_layout)
        self.remove_layout.addWidget(title)
        self.remove_layout.addWidget(self.remove_button)

        frame_layout.addWidget(self.remove_widget)
        frame_layout.addWidget(url)
        if self.comment.__len__() > 1:
            frame_layout.addWidget(comment)
        frame_layout.addWidget(tags)

    def remove_contentbox(self):
        #bookmark aus bookmark_list entfernen & DB entfernen
        self.caretaker.delete_bookmark(self.bookmark)
        #contentbox aus content_box_list entfernen
        self.content_box_list.remove(self)
        self.close()


