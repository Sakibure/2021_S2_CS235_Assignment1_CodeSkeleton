from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
from domainmodel.review import Review

import datetime


class User:

    def __init__(self, user_name, password):
        self.__user_name = None
        self.__password = None
        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

        if isinstance(user_name, str):
            if len(user_name.strip()) > 0:
                self.__user_name = user_name.strip().lower()
        else:
            self.__user_name = None
        if isinstance(password, str):
            if len(password.strip()) > 0 and len(password) >= 7:
                self.__password = password
        else:
            self.__password = None

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def read_books(self):
        return self.__read_books

    @property
    def reviews(self):
        return self.__reviews

    @property
    def pages_read(self):
        return self.__pages_read

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def read_a_book(self, book):
        if isinstance(book, Book):
            if book not in self.__read_books:
                self.__read_books.append(book)
                self.__pages_read += book.num_pages

    def add_review(self, review):
        if isinstance(review, Review):
            if review not in self.__reviews:
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
