import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainGui(QWidget):
    def __init__(self):
        super().__init__()
        #todo remove stylesheet position (read)

        sshFile = "style.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

        self.win_layout = QVBoxLayout()
        self.setLayout(self.win_layout)
        self.setWindowIcon(QIcon("search_icon.png"))

        # main windows (app) settings
        self.setGeometry(650, 400, 700, 400)  # ersten 2 coordinaten geben relative position des windows am bildschirm an
        self.setWindowTitle("Find My Stuff")
        self.win_layout.setContentsMargins(0, 0, 0, 0)

        #search bar / add-button / search-button / sync-button
        self.navigation_widget = QWidget()
        self.navigation_layout = QHBoxLayout()
        self.navigation_widget.setLayout(self.navigation_layout)

        self.search_bar = QLineEdit(self)
        self.searchbar_content = ""
        #self.search_bar.placeholderText("pyqt python (separate tags with Spaces)") #TODO how to "placeholder text"?

        self.search_button = QPushButton("Lupe") #TODO lupen icon einfügen
        self.search_button.setFixedWidth(40)
        self.search_button.setFocusPolicy(Qt.NoFocus)

        self.add_button = QPushButton("+")
        self.add_button.setFixedWidth(40)
        self.add_button.setFocusPolicy(Qt.NoFocus)

        self.sync_button = QPushButton("sync")
        self.sync_button.setFixedWidth(40)
        self.sync_button.setFocusPolicy(Qt.NoFocus)

        self.navigation_layout.addWidget(self.search_bar)
        self.navigation_layout.addWidget(self.search_button)
        self.navigation_layout.addWidget(self.add_button)
        self.navigation_layout.addWidget(self.sync_button)
        self.navigation_layout.setContentsMargins(10,10,10,0)

        #main content: tag_list / content_list (where main content is displayed)
        self.content_widget = QWidget(self)
        self.content_layout = QHBoxLayout(self)
        self.content_widget.setLayout(self.content_layout)

        self.content_layout.setContentsMargins(10,0,10,10)

        self.win_layout.addWidget(self.navigation_widget)
        self.win_layout.addWidget(self.content_widget)

        # list (view for tags)
        self.tag_list = QListWidget()

        self.tag_list.setMaximumWidth(80)
        self.content_layout.addWidget(self.tag_list)

        # scroll_area (main view for bookmarks)
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.content_layout.addWidget(self.scroll)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_content.setLayout(self.scroll_layout)

        self.scroll.setWidget(self.scroll_content)

        #todo test section #remove


class AddBookmarkGui(QWidget):
    def __init__(self):
        super().__init__()

        #todo remove
        sshFile = "style.qss"
        with open(sshFile, "r") as fh:
             self.setStyleSheet(fh.read())

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.setWindowIcon(QIcon("search_icon.png"))
        self.setGeometry(850,500, 300,300)
        self.setWindowTitle("Add new Bookmark")
        self.setContentsMargins(0,0,0,0)
        self.setMaximumHeight(150)

        #keyboard shortcuts to close popup / add bookmark
        self.enter_key_add = QShortcut(QKeySequence(Qt.Key_Return), self)
        self.esc_key_close = QShortcut(QKeySequence(Qt.Key_Escape), self)


        #title input
        self.title_widget = QWidget(self)
        self.title_layout = QHBoxLayout(self)
        self.title_input = QLineEdit()
        self.title_widget.setLayout(self.title_layout)
        self.title_layout.addWidget(QLabel("Title: "))
        self.title_layout.addWidget(self.title_input)

        #url input
        self.url_widget = QWidget()
        self.url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_widget.setLayout(self.url_layout)
        self.url_layout.addWidget(QLabel("URL: "))
        self.url_layout.addWidget(self.url_input)

        #comment inüut
        self.comment_widget = QWidget()
        self.comment_layout = QHBoxLayout()
        self.comment_input = QLineEdit()
        self.comment_widget.setLayout(self.comment_layout)
        self.comment_layout.addWidget(QLabel("Comment: "))
        self.comment_layout.addWidget(self.comment_input)

        #tags input
        self.tags_widget = QWidget()
        self.tags_layout = QHBoxLayout()
        self.tags_input = QLineEdit()
        self.tags_widget.setLayout(self.tags_layout)
        self.tags_layout.addWidget(QLabel("Tags: "))
        self.tags_layout.addWidget(self.tags_input)

        #Buttons "input"
        self.button_widget = QWidget(self)
        self.button_layout = QHBoxLayout(self)

        self.add_button = QPushButton("Add")
        self.cancel_button = QPushButton("Cancel")
        self.add_button.setFocusPolicy(Qt.NoFocus)   #Buttons can't be focues with Tab
        self.cancel_button.setFocusPolicy(Qt.NoFocus)    #Buttons can't be focues with Tab

        self.button_widget.setLayout(self.button_layout)
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)

        #add sub-widget to mainwidget (layout)
        self.main_layout.addWidget(self.title_widget)
        self.main_layout.addWidget(self.url_widget)
        self.main_layout.addWidget(self.comment_widget)
        self.main_layout.addWidget(self.tags_widget)
        self.main_layout.addWidget(self.button_widget)
        self.setWindowModality(Qt.ApplicationModal)  #can't access main window when popup is open


# # start app
# app = QApplication(sys.argv)
# #app.setStyleSheet(qdarkgraystyle.load_stylesheet())
# window = gui()
# window.show()
# app.exec_()


