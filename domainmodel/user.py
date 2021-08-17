from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
from domainmodel.review import Review

import datetime

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def user_name(self, name):
        if len(self.__username) == 0:
            return None
        else:
            self.__username = name.strip().tolower()

    def password(self, pwd):
        if len(pwd) < 7:
            self.__password = None
        else:
            self.__password = pwd

    def read_books(self, book):



    def reviews(self, review):

    def pages_read(self, pages):
        if isinstance(pages, int) and pages >= 0:
            return pages
        else:
            raise ValueError

    def __repr__(self):
        return f'<User {self.__username}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__username == other.__username

    def __lt__(self, other):
        return self.__username < other.__username

    def __hash__(self):
        return hash(self.__username)

    def read_a_book(self, book):

    def add_review(self, review):

