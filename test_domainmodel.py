import pytest

from domainmodel.publisher import Publisher
from domainmodel.author import Author
from domainmodel.book import Book


class TestPublisher:

    def test_construction(self):
        publisher1 = Publisher("Avatar Press")
        assert str(publisher1) == "<Publisher Avatar Press>"
        publisher2 = Publisher("  ")
        assert str(publisher2) == "<Publisher N/A>"
        publisher3 = Publisher("  DC Comics ")
        assert str(publisher3) == "<Publisher DC Comics>"
        publisher4 = Publisher(42)
        assert str(publisher4) == "<Publisher N/A>"

        author1 = Author(3675, "Barack Obama")
        assert str(author1) == "<Author Barack Obama, author id = 3675>"

        book1 = Book(84765876, "Harry Potter")
        assert str(book1) == "<Book Harry Potter, book id = 84765876>"
