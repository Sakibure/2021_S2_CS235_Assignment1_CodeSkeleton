import json


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        # TODO
        self.__books_file_name = None
        self.__authors_file_name = None
        self.__dataset_of_books = None

    @property
    def dataset_of_books(self) -> list:
        return self.__dataset_of_books

    def read_json_files(self):
        # TODO
        pass
