"""
    File name: Bookmark.py
    Author: Faelb (faelb@gmx.at)
    Date created: 12/03/2019
    Date last modified: 12/03/2019
    Python Version: 3.8

   This class is used for creating new Bookmarks
   with all their properties like title, url, comments
   and so on. Bookmarks are saved in the Bookmarks List
   the Caretaker Class takes care of.
"""


class Bookmark:
    # do we need a placeholder for default image import? empty picture?
    def __init__(self, id: int = None, title: str = None, url: str = None, comment: str = None, image=None,
                 tags: list = None):
        """contstructor for Bookmark with ID for creation from DB"""
        self.title = title
        self.comment = comment
        self.url = url
        self.id = id
        self.image = image
        self.tags = tags

    def edit_bookmark(self, title: str = None, comment: str = None, url: str = None, image=None):
        """edits a bookmarks title, comment, url or image
        by default its none so only elements that are provided
        are changed"""
        if title is not None:
            self.title = title
        if comment is not None:
            self.comment = comment
        if url is not None:
            self.url = url
        if image is not None:
            self.image = image

    def edit_title(self, newtitle: str):
        self.title = newtitle

    def edit_comment(self, newcomment: str):
        self.comment = newcomment

    def edit_url(self, newurl: str):
        self.url = newurl

    def edit_image(self, newimage):
        self.image = newimage

    def add_tag(self, tag: str):
        """adds a tag to a bookmark"""
        self.tags.append(tag)

    def delete_tag(self, tag: str):
        """removes a tag from a bookmark"""
        if tag in self.tags:
            self.tags.remove(tag)


