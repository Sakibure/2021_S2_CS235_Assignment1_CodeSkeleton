import self as self

from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
from domainmodel.review import Review

import datetime


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__read_books = []
        self.__reviews = []
        self.__pages_read = None

    @property
    def user_name(self):
        return self.__username

    @user_name.setter
    def user_name(self, name):
        if len(name) == 0:
            self.__username = None
        else:
            self.__username = name.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) < 7:
            self.__password = None
        else:
            self.__password = password

    @property
    def pages_read(self):
        return self.__pages_read

    @pages_read.setter
    def pages_read(self, pages):
        if isinstance(pages, int) and pages >= 0:
            self.__pages_read = pages

    @property
    def read_books(self):
        return self.__read_books

    @property
    def read_a_books(self, book):
        self.__read_books.append(book)

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

    @property
    def read_a_book(self):
        return self.__read_books

    @read_a_book.setter
    def read_a_book(self, book):
        if book not in self.__read_books:
            self.__read_books.append(book)

    @property
    def add_review(self):
        return self.__reviews

    @add_review.setter
    def add_review(self, review):
        self.__reviews.append(review)


if __name__ == '__main__':
    books = [Book(874658, "Harry Potter"), Book(89576, "Lord of the Rings")]
    books[0].num_pages = 107
    books[1].num_pages = 121
    user = User("Martin", "pw12345")
    print(user.read_books)
    print(user.pages_read)
    for book in books:
        user.read_a_book(book)
    print(user.read_books)
    print(user.pages_read)
