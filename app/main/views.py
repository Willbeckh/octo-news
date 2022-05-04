from . import main
from flask import render_template, url_for
from ..request import get_news_sources, get_articles

# first default route


@main.route('/')
def index():
    """
    View root page endpoint that returns the landing page and its data
    """
    source_domain = 'techcrunch.com'  # TODO: make the value dynamic
    # TODO: make the value dynamic 'technology' is = user_input/choice
    top_news = get_news_sources('technology')
    articles = get_articles(source_domain)
    return render_template('index.html', trending=top_news, articles=articles)


# TODO: create list that stores all the news sources
# *LOOP through the list and access its value
#  *IF checked sources, RETURN all articles using selected sources.

# TODO: article details page.
# *User Interface, design...
