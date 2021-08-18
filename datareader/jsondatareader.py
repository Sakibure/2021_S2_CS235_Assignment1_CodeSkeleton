import json
from domainmodel.author import Author
from domainmodel.publisher import Publisher
from domainmodel.book import Book


class BooksJSONReader:
    def __init__(self, books_file_name, authors_file_name):
        self.__books = list()
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name

    @property
    def dataset_of_books(self):
        return self.__books

    def read_json_files(self):
        author_dict = dict()
        # dict_keys(['average_rating', 'author_id', 'text_reviews_count', 'name', 'ratings_count'])
        with open(self.__authors_file_name) as f:
            for line in f.readlines():
                author_data = json.loads(line)
                author_dict[int(author_data['author_id'])] = author_data['name']
        # dict_keys(['isbn', 'text_reviews_count', 'series', 'country_code', 'language_code', 'popular_shelves',
        # 'asin', 'is_ebook', 'average_rating', 'kindle_asin', 'similar_books', 'description', 'format', 'link',
        # 'authors', 'publisher', 'num_pages', 'publication_day', 'isbn13', 'publication_month',
        # 'edition_information', 'publication_year', 'url', 'image_url', 'book_id', 'ratings_count', 'work_id',
        # 'title', 'title_without_series'])
        with open(self.__books_file_name) as f:
            for line in f.readlines():
                data = json.loads(line)
                book = Book(int(data['book_id']), data['title'])
                book.description = data['description']
                book.publisher = Publisher(data['publisher'])
                if data['is_ebook'] == 'true':
                    book.ebook = True
                else:
                    False
                if len(data['publication_year']) != 0:
                    book.release_year = int(data['publication_year'])
                    # book.release_year = int(data['publication_year']) if len(data['publication_year']) != 0 else None
                # book.release_year = data['publication_year']
                for author_info in data['authors']:
                    author_id = int(author_info['author_id'])
                    author = Author(int(author_id), author_dict[author_id])
                    book.add_author(author)
                self.__books.append(book)


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
