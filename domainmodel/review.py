from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
import datetime


class Review:
    def __init__(self, book, review_text, rating, timestamp=datetime):
        if isinstance(book, Book) is False:
            self.__book = None
        else:
            self.__book = book

        if isinstance(review_text, str) and len(review_text.strip()) > 0:
            self.__review_text = review_text
        else:
            self.__review_text = "N/A"

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating = rating
        else:
            raise ValueError

        self.__timestamp = timestamp

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text.strip()

    @review_text.setter
    def review_text(self, text):
        if isinstance(text, str):
            self.__review_text = text.strip()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int):
            self.__rating = value

    def __repr__(self):
        return f'<Book {self.__book}, rating: {self.__rating}, timestamp: {self.__timestamp}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True


if __name__ == '__main__':
    book = Book(2675376, "Harry Potter")
    review_text = "  This book was very enjoyable.   "
    rating = 4
    review = Review(book, review_text, rating)

    print(review.book)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))
