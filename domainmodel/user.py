from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
from domainmodel.review import Review

import datetime


class User:
    def __init__(self, username, password):
        self.__username = None
        self.__password = None
        self.__read_books = []
        self.__reviews = None
        self.__pages_read = 0

        if isinstance(password, int) and password is not None and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None

        if isinstance(username, str) and len(username.strip()) > 0:
            self.__username = username.strip().lower()
        else:
            self.__username = None

    @property
    def user_name(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def pages_read(self):
        return self.__pages_read

    @pages_read.setter
    def pages_read(self, pages):
        if isinstance(pages, int) and pages >= 0:
            self.__pages_read += pages

    @property
    def read_books(self):
        return self.__read_books

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
        if book not in self.__read_books:
            self.__read_books.append(book)
            self.__pages_read += book.num_pages

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