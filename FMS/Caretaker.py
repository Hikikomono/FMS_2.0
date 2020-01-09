"""
    File name: Caretaker.py
    Author: Faelb (faelb@gmx.at)
    Date created: 12/03/2019
    Date last modified: 06/01/2020
    Python Version: 3.8

   This class keeps hold of the Bookmark List
   which is used by the gui to handle all
   Bookmark interactions like create, delete and also
   the initial ListLoad from the DAO

   It is in a distinct relationship with the DAO
   to update every change of the List to the
   Database
"""
from Bookmark import Bookmark
from BookmarkDao import BookmarkDao
#from Parser import Parser


class Caretaker:

    def __init__(self):
        self.bookmark_list = []
        self.dao = BookmarkDao()
        #self.parser = Parser()
        # make a singleton here (dao + parser)

    def add_bookmark(self, id: int = None, title: str = None, url: str = None, comment: str = None, image=None,
                     tags: list = None):
        """this method is called to create a new bookmark locally, and send it directly to the db via DAO"""
        self.bookmark_list.append(Bookmark(id, title, url, comment, image, tags))
        self.dao.add_bookmark(self.bookmark_list[-1])  # -1 spricht immer das letzte Element einer Liste an
        self.bookmark_list[-1].id = self.dao.table_select_highest_id()

    def delete_bookmark(self, bookmark):
        """this method is called to remove a bookmark locally, and also at the db via DAO"""
        if bookmark in self.bookmark_list:
            self.bookmark_list.remove(bookmark)
            self.dao.delete_bookmark(bookmark)

    def edit_bookmark(self, bookmark, type, value):
        """This Dictionary works like a switch case statement - in case of type 1 (the key of the dictionary)
        it calls the value, which is the specific editing method for the bookmark - the value will be the parameter
        after calling the edit function the DAO will be invoked to update the db"""
        mapping = {1: bookmark.edit_title, 2: bookmark.edit_comment, 3: bookmark.edit_url, 4: bookmark.edit_image}
        mapping[type](value)
        self.dao.update_from_db(bookmark)

    def add_tag(self, bookmark, tag: str):
        bookmark.add_tag(tag)
        self.dao.update_from_db(bookmark)

    def delete_tag(self, bookmark, tag: str):
        bookmark.delete_tag(tag)
        self.dao.update_from_db(bookmark)

    def get_list(self):
        """this method is called at the startup of the program to create a List of Bookmarks from the DB via DAO", also
        it calls the parser to search for files with bookmarks from the Browserplugin"""
        self.bookmark_list = self.dao.get_list()
        print(self.bookmark_list[0].tags)
        #self.parser.get_bookmarks()
