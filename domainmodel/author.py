import author as author


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
