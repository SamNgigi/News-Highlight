from flask import render_template
from app import app
from .request import get_sources, get_news

#  Views


@app.route('/')
def index():
    """
    Function that returns the index page and its data

    Example call
    top_headlines = get_sources('de','business')

    We can also have a get_all() function that gets all the news
    Example call from views would be
    everything
    """
    general_list = get_sources('us', 'business')
    # business_list = get_sources('us', 'business')
    # sports_list = get_sources('us', 'sports')
    # entertainment_list = get_sources('us', 'entertainment')
    test_args = 'Working!'
    return render_template('index.html',
                           test_param=test_args,
                           general=general_list)

    # return render_template('index.html',
    #                        test_param=test_args,
    #                        general=general_list,
    #                        business=business_list,
    #                        sports=sports_list,
    #                        entertainment=entertainment_list)


@app.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news_args = get_news(id)
    highlight_args = 'Route Working!!'
    return render_template('news.html',
                           highlight_param=highlight_args,
                           news=news_args)
