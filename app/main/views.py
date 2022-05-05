from . import main
from flask import render_template, request
from ..request import get_news_category, get_articles


# first default route
@main.route('/', methods=['GET', 'POST'])
def index():
    """
    View root page endpoint that returns the landing page and its data
    """
    news_category = get_news_category('general')  # default sources
    articles_source = get_articles('bbc-news, abc-news, the-verge')

    try:
        if request.method == 'POST':
            user_category_pick = request.form.get('categories')
            category = get_news_category(user_category_pick)

            user_source_choice = request.form.getlist('source-tag')
            # convert list to comma separated strings.
            source_list = ' ,'.join([str(word) for word in user_source_choice])
            source_ids = get_articles(source_list)

            return render_template('index.html', trending=category, articles=source_ids)

    except TypeError:  # incase the news source picked doesn't have the selected category
        return render_template('404.html')
    except KeyError:
        return render_template('404.html')
    else:
        return render_template('index.html', trending=news_category, articles=articles_source)
