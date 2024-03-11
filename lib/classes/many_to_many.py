class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
          return list(set(article.magazine for article in self.__articles ))


    def add_article(self, magazine, title):
        existing_article = [article for article in self.__articles if article.magazine == magazine and article.title == title]
        if existing_article :
            return existing_article[0]
        article = Article(self, magazine, title)
        self.__articles.append(article)
        magazine.add_article(self, title)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.__articles)) if self.__articles else None

class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.__title = title
        Article.all.append(self)

        if not(5 <= len(title) <= 50):
            raise

    @property
    def title(self):
        return self.__title
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string of length between 2 and 16")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")
        self.__name = name
        self.category = category
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(set(article.author for article in self.__articles if article.author))

    def article_titles(self):
        return [article.title for article in self.__articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self.__articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    def add_article(self, author, title):
        article = Article(author, self, title)
        self.__articles.append(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.__articles))