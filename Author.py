from Articles import Article
from Magazine import Magazine

class Author:
    
    def __init__(self, name):
        self._name = name
        self.article = []
        self.magazine = []
        self.topics = []
        
    
    @property
    def name (self):
        return self._name
    
    def articles(self):
        return self.article
    
    def add_magazines(self, mag, mag_category):
        self.magazine.append(mag)
        self.topics.append(mag_category)
    
    def magazines(self):
        return self.magazine
    
    def add_article(self, magazine, title):
        self.article.append(Article(self.name, magazine, title))

    def topic_areas(self):
        return self.topics