from domainmodel.book import Book
from domainmodel.author import Author
from domainmodel.publisher import Publisher


class BooksInventory:
    def __init__(self, price, num_items):
        self.__book = Book
        self.__price = price
        self.__num_items = num_items

    def add_book(self, book, price, nr_books_in_stock):

    def remove_book(self, book_id):

    def find_book(self, book_id):

    def find_price(self, book_id):

    def find_stock_count(self, book_id):

    def search_book_by_title(self, title):

