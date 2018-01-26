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
    business_list = get_sources('us', 'business')
    technology_list = get_sources('us', 'technology')
    science_list = get_sources('us', 'science')
    health_list = get_sources('us', 'health')
    sports_list = get_sources('us', 'sports')
    entertainment_list = get_sources('us', 'entertainment')
    test_args = 'Working!'
    return render_template('index.html',
                           test_param=test_args,
                           business=business_list,
                           technology=technology_list,
                           science=science_list,
                           health=health_list,
                           sports=sports_list,
                           entertainment=entertainment_list)


@app.route('/articles/<id>')
def articles(id):
    """
    View articles page that returns the news article from a highlight
    """
    highlight_args = 'Route Working!!'
    return render_template('article.html', highlight_param=highlight_args)
