import sqlite3

class DbController:
    def __init__(self):
        self.conn = sqlite3.connect('fms.db')  # tries to connect to db - if file not exist -> create file (db)
        self.cur = self.conn.cursor()  # to navigate / manipulate DB

    def init_tables(self):
        # Bookmark Table Creation
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS bookmarks ("
            "bid INTEGER PRIMARY KEY AUTOINCREMENT,"
            "title CHAR,"
            "url CHAR,"
            "comment CHAR,"
            "image BLOB)")

        # TAG Table Creation
        self.cur.execute("CREATE TABLE IF NOT EXISTS tags ("
                         "tid INTEGER PRIMARY KEY AUTOINCREMENT,"
                         "tag_name CHAR,"
                         "UNIQUE (tag_name))")

        # Connection Table between Bookmark Table & Tag Table
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS linkingTable ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "bid INTEGER,"
            "tid INTEGER,"
            "FOREIGN KEY(bid) REFERENCES bookmarks(bid),"
            "FOREIGN KEY(tid) REFERENCES tags(tid))")

        self.cur.close()
        self.conn.close()


test = DbController()
test.init_tables()

