'''
search_bookmark(String) : Bookmark ---> so far not needed -> search is performed in the fetched bookmark list
'''
import sqlite3
from FMS.Bookmark import Bookmark  # from folder_name.file_name import class_name


class BookmarkDao:
    def __init__(self):
        self.conn = sqlite3.connect('fms.db')  # tries to connect to db - if file not exist -> create file (db)
        self.cur = self.conn.cursor()  # to navigate / manipulate DB
        self.bookmark_list = []  # list which will save Bookmark objects

    def add_bookmark(self, bookmark: Bookmark) -> None:  # bookmark:Bookmark erweitern
        """
        add_bookmark() gets a Bookmark object as a parameter
        the values/parameters of the Bookmark object get added as a new insert entry into the DB table bookmarks
        values: bookmark.title, bookmark.url, bookmark.comment, bookmark.image
        """
        self.cur.execute("INSERT OR IGNORE INTO bookmarks VALUES (?, ?, ?, ?, ?)",
                         (None, bookmark.title, bookmark.url, bookmark.comment, bookmark.image))
        for tag in bookmark.tags:
            self.cur.execute("INSERT OR IGNORE INTO tags VALUES (?, ?)", (None, tag))
        self.conn.commit()

        # fill linkingTable
        bid = self.table_select_highest_id()
        for tag in bookmark.tags:
            self.cur.execute("SELECT tid FROM tags WHERE tag_name = ?", [tag])
            tid = self.cur.fetchone()
            self.cur.execute("INSERT INTO linkingTable VALUES (?,?,?)", (None, bid, tid[0]))
        self.conn.commit()

    def delete_bookmark(self, bookmark: Bookmark) -> None:
        self.cur.execute("DELETE FROM bookmarks WHERE bid = ?", [bookmark.id])  #
        self.cur.execute("DELETE FROM linkingTable WHERE bid = ?", [bookmark.id])
        self.conn.commit()

    def update_from_db(self, bookmark: Bookmark) -> None:
        self.cur.execute("UPDATE bookmarks set title = ?, url = ?, comment = ?, image = ? where bid = ?",
                         (bookmark.title, bookmark.url, bookmark.comment, bookmark.image, bookmark.id))  #
        self.conn.commit()

    def get_list(self) -> [Bookmark]:
        self.cur.execute("SELECT * FROM bookmarks")
        db_list = list(self.cur.fetchall())
        bookmark_list = []

        for row in db_list:
            bookmark_list.append(Bookmark(row[0], row[1], row[2], row[3], row[4]))

        # print(bookmark_list[0])
        return bookmark_list

    def table_select_highest_id(self) -> int:   #rename to get_highest_id()
        self.cur.execute("SELECT MAX(bid) FROM bookmarks")
        max_id = self.cur.fetchone()
        return int(max_id[0])



# Testing DB entries

#bookmarkDao = BookmarkDao()
# tag_list_1 = ["tag_1", "tag_2"]
# tag_list_2 = ["tag_3337", "tag_4337"]

#print(bookmarkDao.table_select_highest_id())
#
# bookmark_1 = Bookmark("title_1337", "comment_2337", "URL_1337", "", tag_list_1)
# bookmark_2 = Bookmark("title_2", "comment_2", "URL_2", "", tag_list_2)
# # bookmarkDao.add_bookmark(bookmark_1)
# # bookmarkDao.add_bookmark(bookmark_2)
# # bookmarkDao.delete_bookmark(bookmark_2)
# #bookmarkDao.update_from_DB(bookmark_1)
#
# bookmark_list = bookmarkDao.get_list()
# test_bookmark_object = bookmark_list[0]
# print(test_bookmark_object.comment)
