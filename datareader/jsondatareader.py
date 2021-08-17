import json


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = None
        self.__authors_file_name = None
        self.__dataset_of_books = []
        if isinstance(books_file_name, str) and len(books_file_name.strip()) >= 0:
            self.__books_file_name = books_file_name
        else:
            raise ValueError
        if isinstance(authors_file_name, str) and len(authors_file_name.strip()) >= 0:
            self.__authors_file_name = authors_file_name
        else:
            raise ValueError

    @property
    def dataset_of_books(self):
        return self.__dataset_of_books

    def read_json_files(self):
        try:
            with open(self.__authors_file_name, "r") as authors_file:
                with open(self.__books_file_name, "r") as book_file:
                    author_data = json.load(authors_file)
            book_data = json.load(book_file)
            return author_data, book_data

        except ValueError:
            print()


if __name__ == '__main__':
    authors_filename = 'book_authors_excerpt.json'
    books_filename = 'comic_books_excerpt.json'
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()
    print(reader.dataset_of_books[0])
    print(reader.dataset_of_books[10])
    print(reader.dataset_of_books[19])
    print(reader.dataset_of_books[4].publisher)
    print(reader.dataset_of_books[15].authors[0])
