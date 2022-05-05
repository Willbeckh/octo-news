import os


class Source:
    '''
    Class for defining the news source object.
    '''

    def __init__(self, id, name, description, url, category, language, country):
        '''
        Initializes the news sources object.
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Article:
    """
    Class for defining the articles object
    """

    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
        """
        Initializes the article object instance
        """
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
