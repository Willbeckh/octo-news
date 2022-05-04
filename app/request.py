import requests
from .models import Article, Source


# get api key && url
api_key = None
api_base_url = None
articles_base_url = None


# define request configuration
def configure_request(app):
    global api_key, api_base_url, articles_base_url
    api_key = app.config['API_KEY']
    api_base_url = app.config['NEWS_SOURCE_API_URL']
    articles_base_url = app.config['NEWS_ARTICLE_API_URL']


def get_news_sources(category):
    """
    queries the news api and returns the json response
    """
    news_sources_url = api_base_url.format(category)
    headers = {'X-Api-Key': api_key}

    with requests.get(news_sources_url, headers=headers) as url:
        news_response = url.json()
        news_results = None

        if news_response['sources']:
            news_response_data = news_response['sources']
            news_results = process_news(news_response_data)

        return news_results


def process_news(news_list):
    """
    Function that processes the news result and transform to a list of objects
    Args:
        news_list - a list of dictionaries that contain the news source details
    Returns:
        news_results - a list of news objects
    """

    news_results = []
    for news in news_list:
        id = news['id']
        name = news['name']
        description = news['description']
        url = news['url']
        category = news['category']
        language = news['language']
        country = news['country']

        if country:
            news_object = Source(id, name,  description,
                                 url, category, language, country)
            news_results.append(news_object)

    return news_results


# articles query
def get_articles(domain):
    """
    Function that queries the api for all articles
    Returns:
        object - a JSON object for available articles.
    """
    articles_url = articles_base_url.format(domain)
    # stores the api key, and pass it with the request
    headers = {'X-Api-Key': api_key}

    with requests.get(articles_url, headers=headers) as url:
        articles_response = url.json()
        article_results = None

        if articles_response['articles']:
            articles_response_data = articles_response['articles']
            article_results = process_articles(articles_response_data)

        return article_results


# for processing the available articles.
def process_articles(articles_list):
    """
    Funtion that process the available news articles and transform to a list of dictionaries.
    Args: 
        articles_list - list of dictionaries
    Returns:
        articles_result - a list of new articles.
    """

    article_results = [] 
    try: 
        for article in articles_list:
            id = article['source']['id']
            name = article['source']['name']
            author = article['author']
            title = article['title']
            description = article['description']
            url = article['url']
            urlToImage = article['urlToImage']
            publishedAt = article['publishedAt']
            content = article['content']

            if author:
                new_article_object = Article(id, name,
                                             author, title, description, url, urlToImage, publishedAt, content)
                article_results.append(new_article_object)
    except:
        print("ERR: Some unknown error occurred!")
    finally:
        return article_results
