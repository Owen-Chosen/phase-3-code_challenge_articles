
class Article:

    all_list = []


    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.add_to_all(title)

    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    
    @property
    def title(self):
        return self._title
    
    @classmethod
    def add_to_all(cls, title):
        cls.all_list.append(title)

    @classmethod
    def all(cls):
        return cls.all_list