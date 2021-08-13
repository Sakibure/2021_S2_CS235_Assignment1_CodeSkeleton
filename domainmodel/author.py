class Author:
    def __init__(self, author_id, author_name):
        self.__name_ls = []
        if isinstance(author_id, int) and author_id >= 0 and author_id is not None:
            self.__id = author_id
        else:
            raise ValueError
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.__name = author_name
        else:
            raise ValueError

    @property
    def full_name(self):
        return self.__name

    @full_name.setter
    def full_name(self, author_name):
        if isinstance(author_name, str) and len(author_name.strip()) > 0 and author_name is not None:
            self.__name = author_name
        else:
            raise ValueError

    @property
    def unique_id(self):
        return self.__id

    def __repr__(self):
        return f'<Author{self.__name}, author_id = {self.__id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__id == self.__id

    def __lt__(self, other):
        return self.__id < other.__id

    def __hash__(self):
        return hash(self.__id)

    def add_coauthor(self, coauthor):
        if coauthor not in self.__name_ls:
            self.__name_ls.append(coauthor)
            coauthor.__name_ls.append(self)

    def check_if_this_author_coauthored_with(self, name):
        return name in self.__name_ls


if __name__ == '__main__':
    author1 = Author(3675, "Barack Obama")
    print(author1)
    try:
        author2 = Author(123, "  ")
        print(author2)
    except ValueError:
        print("ValueError was raised!")
    try:
        author3 = Author(42, 42)
        print(author3)
    except ValueError:
        print("ValueError was raised!")
    author4 = Author(23, "J.R.R. Tolkien")
    print(author4.unique_id, author4.full_name)
