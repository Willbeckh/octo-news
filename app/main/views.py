from . import main
from flask import render_template
from ..request import get_news_sources

# first default route
@main.route('/')
def index():
    """
    View root page endpoint that returns the landing page and its data
    """
    # return "Yoow Blueprints!"
    # getting top headlines news
    top_news = get_news_sources('top-headlines')
    return render_template('index.html', trending=top_news)