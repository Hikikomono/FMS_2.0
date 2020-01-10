import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Bookmark import Bookmark

class ContentBox(QFrame):
    def __init__(self, bookmark: Bookmark):
        super().__init__()
        self.title = bookmark.title
        self.url = bookmark.url
        self.comment = bookmark.comment
        self.tags = bookmark.tags   #list

        link_markup = f'<a href="{self.url}"><span style="color:green;">{self.url}</span></a>'

        frame_layout = QVBoxLayout()
        self.setLayout(frame_layout)
        self.setFrameShape(QFrame.Box)

        title = QLabel("Title: " + self.title)
        url = QLabel("URL: " + link_markup)
        url.setOpenExternalLinks(True)
        comment = QLabel("Comment: " + self.comment)
        tags = QLabel("Tags: " +''.join(self.tags))

        frame_layout.addWidget(title)
        frame_layout.addWidget(url)
        if self.comment.__len__() > 1:
            frame_layout.addWidget(comment)
        frame_layout.addWidget(tags)

