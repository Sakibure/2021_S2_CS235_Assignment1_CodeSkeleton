class Publisher:

    def __init__(self, publisher_name: str):
        self.__name = None
        if isinstance(publisher_name,str) is False or len(publisher_name.strip()) is 0:
            self.__name = "N/A"
        self.__publisher = publisher_name.strip()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        self.__name = publisher_name

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.name

    def __lt__(self, other):
        return self.__name < other.__name

    def __hash__(self):
        return hash(self.__name)
