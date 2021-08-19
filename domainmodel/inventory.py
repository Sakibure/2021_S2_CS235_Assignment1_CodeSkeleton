from domainmodel.book import Book


class BooksInventory:
    def __init__(self, price, num_items):
        self.book = Book.collection()
        self.price = price
        self.num_items = num_items

    def add_book(self, book, price, nr_books_in_stock):
        wtf is this

