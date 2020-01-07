import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ContentBox(QFrame):
    def __init__(self, title: str="testTitle", url: str="testURL", tags: list="testTag1, testTag2"):
        super().__init__()
        self.title = title
        self.url = url
        self.tags = tags

        frame_layout = QVBoxLayout()
        self.setLayout(frame_layout)
        self.setFrameShape(QFrame.Box)

        title = QLabel(title)
        url = QLabel(url)
        tags = QLabel(tags)  # listen-impl muss noch überdacht werden

        frame_layout.addWidget(title)
        frame_layout.addWidget(url)
        frame_layout.addWidget(tags)

