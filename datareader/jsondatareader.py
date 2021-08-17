import json


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = ''
        self.__authors_file_name = ''
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
            authors_file = open('book_authors_excerpt.json')
            book_file = open('comic_books_excerpt.json')
            author_line = authors_file.readlines()
            book_line = book_file.readlines()
            authors_file.close()
            book_file.close()
            for i in author_line:
                author_data = json.loads(i)
                print(author_data["average_rating"])
                print(author_data["author_id"])
                print(author_data["text_reviews_count"])
                print(author_data["name"])
                print(author_data["ratings_count"])

            for i in book_line:
                book_data = json.loads(i)
                print(book_data[""])

        except FileNotFoundError:
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
