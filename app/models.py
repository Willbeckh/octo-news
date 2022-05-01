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
    
    def __init__(self) -> None:
        pass