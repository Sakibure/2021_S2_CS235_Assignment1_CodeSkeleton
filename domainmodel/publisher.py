class Publisher:

    def __init__(self, publisher_name: str):
        self.__name = ''
        if isinstance(publisher_name, str) is False or len(publisher_name.strip()) == 0:
            self.__name = "N/A"
        else:
            self.__name = publisher_name.strip()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        self.__name = publisher_name

    def __repr__(self):
        # we use access via the property here

        return f'<Publisher {self.__name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.__name == self.__name

    def __lt__(self, other):
        return self.__name < other.__name

    def __hash__(self):
        return hash(self.__name)


if __name__ == '__main__':

    publisher1 = Publisher("Avatar Press")
    print(publisher1)
    publisher2 = Publisher("  ")
    print(publisher2)
    publisher3 = Publisher("  DC Comics ")
    print(publisher3)
    publisher4 = Publisher(42)
    print(publisher4)


