"""
    File name: Bookmark.py
    Author: Faelb (faelb@gmx.at)
    Date created: 06/01/2020
    Date last modified: 07/01/2020
    Python Version: 3.6

    This class shall get the download file of the chrome extension
    load the csv data and turn it into bookmark objects, windows & linux compatible
"""

import Caretaker
import csv
import os
from sys import platform
import getpass


class Parser:
    system = platform

    def __init__(self):
        self.carer = Caretaker.Caretaker()

    def get_bookmarks(self):
        """this method crawls the csv created from the browser extension and returns a list of Bookmarks,depending on
         the operating OS"""
        user = getpass.getuser()
        linuxpath = '/home/' + user + '/Downloads/download'
        winpath = 'C:\\Users\\' + user + '\\Downloads\\Download'

        if platform == "linux" or platform == "linux2":
            if os.path.exists(linuxpath):
                with open(linuxpath) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    line_count = 0
                    print("folgende Bookmarks wurden aus dem csv in Bookmark Objekte verwandelt:")
                    for row in csv_reader:
                        # print(f'blabla {attribute} blabla') makes a formatted string
                        self.carer.add_bookmark(None, row[1], row[0], row[3], None, row[2].replace(" ", "").split(","))
                        print(f'\t{row[0]} <-URL {row[1]} <-Title {row[2]} <-tags {row[3]} <-comment')
                        line_count += 1
                    print(f'Processed {line_count} lines.')
                    csv_file.close()
                    os.remove(linuxpath)
            else:
                print("no file from plugin found")
        elif platform == "win32":
            if os.path.exists(winpath):
                with open(winpath) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    line_count = 0
                    print("folgende Bookmarks wurden aus dem csv in Bookmark Objekte verwandelt:")
                    for row in csv_reader:
                        # print(f'blabla {attribute} blabla') makes a formatted string
                        self.carer.add_bookmark(None, row[1], row[0], row[3], None, row[2].replace(" ", "").split(","))
                        print(f'\t{row[0]} <-URL {row[1]} <-Title {row[2]} <-tags {row[3]} <-comment')
                        line_count += 1
                    print(f'Processed {line_count} lines.')
                    csv_file.close()
                    os.remove(winpath)
            else:
                print("no file from plugin found")
