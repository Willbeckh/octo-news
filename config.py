import os


class Config:
    NEWS_SOURCE_API_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}'
    NEWS_ARTICLE_API_URL = 'https://newsapi.org/v2/everything?sources={}'
    API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    """
    sets the application development environment
    """
    DEBUG = True


# app config envs
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
