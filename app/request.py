from app import app
import urllib.request
import json
from .models import news_source

Source = news_source.Source


# Getting the api_key
api_key = app.config['NEWS_API_KEY']

# Getting the base_url
base_url = app.config['BASE_NEWS_API_URL']


def get_sources(sources, country, category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(sources, country, category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        # get_news_response is now a dictionary because of the json.loads()

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(source_list):
    """
    We now want to process the dictionary and
    output a list of objects - news_results.

    We process results will transform our dictionary into a list of objects.
    """
    news_results = []
    for source in source_list:
        id = source.get('id')
        print(id)
        name = source.get('name')
        print(name)
        author = source.get('author')
        description = source.get('description')
        urlToImage = source.get('urlToImage')
        url = source.get('url')
        publishedAt = source.get('publishedAt')

        if urlToImage:
            source_object = Source(
                id, name, author, description, url, urlToImage, publishedAt)

            news_results.append(source_object)

    return news_results


# def get_news(id):
#     """
#     Function that directs you to the clicked news source articles.
#     """
#     get_news_url = base_url.format(id, api_key)
#     with urllib.request.urlopen(get_news_url) as url:
#         articles = url.read()
#         get_news_response = json.loads(get_news_data)
#
#         news_object = None
#
