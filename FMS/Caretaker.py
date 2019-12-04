"""
    File name: Caretaker.py
    Author: Faelb (faelb@gmx.at)
    Date created: 12/03/2019
    Date last modified: 12/03/2019
    Python Version: 3.8

   This class keeps hold of the Bookmark List
   which is used by the GUI to handle all
   Bookmark interactions like create, delete and also
   the initial ListLoad from the DAO

   It is in a distinct relationship with the DAO
   to update every change of the List to the
   Database
"""
from FMS.Bookmark import Bookmark
from FMS.BookmarkDao import BookmarkDao


class Caretaker:

    def __init__(self):
        self.bookmark_list = []
        self.dao = BookmarkDao()
        # make a singleton here

    def add_bookmark(self, id: int = None, title: str = None, url: str = None, comment: str = None, image=None,
                     tags: list = None):
        """this method is called to create a new bookmark locally, and send it directly to the db via DAO"""
        self.bookmark_list.append(Bookmark(id, title, url, comment, image, tags))
        self.dao.add_bookmark(self.bookmark_list[-1])  # -1 spricht immer das letzte Element einer Liste an

    def delete_bookmark(self, bookmark):
        """this method is called to remove a bookmark locally, and also at the db via DAO"""
        if bookmark in self.bookmark_list:
            self.bookmark_list.remove(bookmark)
            self.dao.delete_bookmark(bookmark)

    def get_list(self):
        """this method is called at the startup of the program to create a List of Bookmarks from the DB via DAO"""
        self.bookmark_list = self.dao.get_list()
