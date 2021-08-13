from domainmodel.publisher import Publisher


class Book:
    def __init__(self, id, title):
        self.__publisher = None
        self.__description = None
        self.__authors = []
        self.__publish_year = None
        self.__ebook = False
        if isinstance(id, int):
            self.__book_id = id
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
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    def __repr__(self):
        return f"<Book {self.__book_title}, book id = {self.__book_id}>"

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass
    def add_author(author):
