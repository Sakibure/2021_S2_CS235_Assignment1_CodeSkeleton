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
    def publisher(self, pub):
        self.__publisher = pub

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    def __repr__(self):
        return f"<Book {self.__book_title}, book id = {self.__book_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, au):
        if au not in self.__authors:
            self.__authors.append(au)
            au.__authors.append(self)


if __name__ == '__main__':
    book = Book(84765876, "Harry Potter")
    print(book)

    publisher = Publisher("Bloomsbury")
    book.publisher = publisher
    print(book.publisher)

    author = Author(635, "J.K. Rowling")
    book.add_author(author)
    print(book.authors)
