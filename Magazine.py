
class Magazine:

    all_list = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.add_to_all(self)
        self.authors = []
        

    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    @classmethod
    def add_to_all(cls, magazine):
        cls.all_list.append(magazine)
    
    @classmethod
    def all(cls):
        return cls.all_list
    
    def add_author(self, author):
        self.authors.append(author)

    def contributors(self):
        return self.authors
    
    @classmethod
    def find_by_name(cls, name):
        for maga in cls.all_list:
            if type(maga) == Magazine and maga.name == name:
                return maga.name