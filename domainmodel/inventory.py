from domainmodel.book import Book
from domainmodel.author import Author
from domainmodel.publisher import Publisher


class BooksInventory:
    def __init__(self):
        self.__book_title_id = {}
        self.__bookid_price_count = {}

    def add_book(self, book: Book, price, nr_books_in_stock):
        if isinstance(book, Book) and book.book_id not in self.__bookid_price_count.keys():
            self.__bookid_price_count[book.book_id] = [price, nr_books_in_stock, book]
            self.__book_title_id[book.title] = book.book_id
        else:
            count = self.__bookid_price_count[book.book_id][1]
            self.__bookid_price_count[book.book_id] = [price, nr_books_in_stock + count, book]
            self.__book_title_id[book.title] = book.book_id

    def remove_book(self, book_id):
        if book_id not in self.__bookid_price_count.keys():
            return None
        else:
            self.__bookid_price_count.pop(book_id)

    def find_book(self, book_id):
        if book_id not in self.__bookid_price_count.keys():
            return None
        else:
            return self.__bookid_price_count[book_id][2]

    def find_price(self, book_id):
        if book_id not in self.__bookid_price_count.keys():
            return None
        else:
            return self.__bookid_price_count[book_id][0]

    def find_stock_count(self, book_id):
        if book_id not in self.__bookid_price_count.keys():
            return None
        else:
            return self.__bookid_price_count[book_id][1]

    def search_book_by_title(self, title):
        if title not in self.__book_title_id.keys():
            return None
        else:
            book_id = self.__book_title_id[title]
            return self.find_book(book_id)


if __name__ == '__main__':
    inventory = BooksInventory()

    publisher1 = Publisher("Avatar Press")

    book1 = Book(17, "Lord of the Rings")
    book1.publisher = publisher1

    book2 = Book(64, "Our Memoires")
    book2.publisher = publisher1

    inventory.add_book(book1, 20, 7)
    inventory.add_book(book2, 30, 2)

    print(inventory.find_price(64))
    print(inventory.find_stock_count(17))
    print(inventory.find_book(99))
