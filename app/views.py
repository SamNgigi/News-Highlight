from flask import render_template
from app import app
from .request import get_sources

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
    business_list = get_sources('us', '')
    # business_list = get_sources('us', 'business')
    # sports_list = get_sources('us', 'sports')
    # entertainment_list = get_sources('us', 'entertainment')
    test_args = 'Working!'
    return render_template('index.html',
                           test_param=test_args,
                           business=business_list)

    # return render_template('index.html',
    #                        test_param=test_args,
    #                        general=general_list,
    #                        business=business_list,
    #                        sports=sports_list,
    #                        entertainment=entertainment_list)


@app.route('/articles/<highlight>')
def articles(highlight):
    """
    View articles page that returns the news article from a highlight
    """
    highlight_args = 'Route Working!!'
    return render_template('article.html', highlight_param=highlight_args)
