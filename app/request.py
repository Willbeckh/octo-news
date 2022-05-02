import requests
from requests.exceptions import HTTPError
from .models import Source


# get api key && url
api_key = None
api_base_url = None


# define request configuration
def configure_request(app):
    global api_key, api_base_url
    api_key = app.config['API_KEY']
    api_base_url = app.config['NEWS_API_URL']


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
        # if response is successful, no Exception is raised

    return news_results


def process_news(news_list):
    """
    Function that processes the movie result and transform to a list of objects
    Args:
        news_data - a list of dictionaries that contain the news source details
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
