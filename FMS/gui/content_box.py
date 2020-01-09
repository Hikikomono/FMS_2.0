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
        self.tags = bookmark.tags   #list

        frame_layout = QVBoxLayout()
        self.setLayout(frame_layout)
        self.setFrameShape(QFrame.Box)

        title = QLabel(self.title)
        url = QLabel(self.url)
        tags = QLabel(self.tags)  # listen-impl muss noch überdacht werden

        frame_layout.addWidget(title)
        frame_layout.addWidget(url)
        frame_layout.addWidget(tags)

