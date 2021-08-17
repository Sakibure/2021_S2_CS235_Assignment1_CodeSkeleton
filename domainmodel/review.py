from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book
import datetime


class Review:
    def __init__(self, book, review_text, rating):
        self.__book = None
        self.__rating = None
        self.__review_text = "N/A"
        self.__timestamp = datetime.datetime.now()

        if isinstance(book, Book):
            self.__book = book

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating = rating
        else:
            raise ValueError

        if isinstance(review_text, str) and len(review_text.strip()) > 0 and review_text is not None:
            self.__review_text = review_text.strip()

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<{self.__book}>"

    def __eq__(self, other):
        if type(other) == type(self):
            if self.__rating == other.__rating and self.__review_text == other.__review_text and self.__timestamp == other.__timestamp and self.__book == other.__book:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    book = Book(2675376, "Harry Potter")
    review_text = "  This book was very enjoyable.   "
    rating = 4
    review = Review(book, review_text, rating)

    print(review.book)
    print("Review: {}".format(review.review_text))
    print("Rating: {}".format(review.rating))

    publisher = Publisher("DC Comics")
    review = Review(publisher, "I liked this book", 4)
    print(review.book)
