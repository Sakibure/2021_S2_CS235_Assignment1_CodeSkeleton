from domainmodel.author import Author
from domainmodel.publisher import Publisher


class Book:
    def __init__(self, book_id, title):
        self.__publisher = None
        self.__description = None
        self.__authors = []
        self.__publish_year = None
        self.__ebook = False
        if isinstance(book_id, int):
            self.__book_id = book_id
        else:
            raise ValueError
        if isinstance(title, str) and len(title.strip()) > 0:
            self.__book_title = title
        else:
            raise ValueError

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, name):
        if isinstance(name, Publisher):
            self.__publisher = name

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__book_title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title.strip()) > 0:
            self.__book_title = title
        else:
            raise ValueError

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description.strip()) > 0:
            self.__description = description

    @property
    def release_year(self):
        return self.__publish_year

    @release_year.setter
    def release_year(self, year):
        if isinstance(year, int) and year >= 0:
            self.__publish_year = year
        else:
            raise ValueError

    @property
    def ebook(self):
        return self.__ebook

    @ebook.setter
    def ebook(self, ebook):
        if isinstance(ebook, bool):
            self.__ebook = ebook

    def __repr__(self):
        return f"<Book {self.__book_title}, book id = {self.__book_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__book_id == other.__book_id

    def __lt__(self, other):
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, au):
        if isinstance(au, Author) and au not in self.__authors:
            self.__authors.append(au)

    def remove_author(self, au):
        if isinstance(au, Author) and au in self.__authors:
            self.__authors.remove(au)


if __name__ == '__main__':
    book = Book(84765876, "Harry Potter")
    print(book)

    publisher = Publisher("Bloomsbury")
    book.publisher = publisher
    print(book.publisher)

    author = Author(635, "J.K. Rowling")
    book.add_author(author)
    print(book.authors)
