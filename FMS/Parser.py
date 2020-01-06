"""
    File name: Bookmark.py
    Author: Faelb (faelb@gmx.at)
    Date created: 06/01/2020
    Date last modified: 06/01/2020
    Python Version: 3.6

    This class shall get the download file of the chrome extension
    load the csv data and turn it into bookmark objects
"""


import Caretaker
import csv


class Parser:
    def __init__(self):
        self.carer = Caretaker.Caretaker()

    def get_bookmarks(self):
        """this method crawls the csv created from the browser extension and returns a list of Bookmarks"""
        # TODO: den Pfad dynamisch machen
        with open('/home/faelb/Downloads/download') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            print("Log information for devs - folgende Bookmarks wurden aus dem csv in Bookmark Objekte verwandelt:")
            for row in csv_reader:
                # print(f'blabla {attribute} blabla') makes a formatted string

                self.carer.add_bookmark(None, row[1], row[0], row[3], None, [row[2]])

                print(f'\t{row[0]} <-URL {row[1]} <-Title {row[2]} <-tags {row[3]} <-comment')
                line_count += 1
            print(f'Processed {line_count} lines.')
