from app import app
import urllib.request
import json
# TODO: from .models import news_source


# Getting the api_key
api_key = app.config['NEWS_API_KEY']

# Getting the base_url
base_url = app.config['BASE_NEWS_API_URL']


def get_sources(country, category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(country, category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        # get_news_response is now a dictionary because of the json.loads()

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(source_list):
    """
    We now want to process the dictionary and
    output a list of objects - news_results.

    We process results will transform our dictionary into a list of objects.
    """
    # news_results = []
    for source in source_list:
        id = source.get('id')
        print(id)
        name = source.get('name')
        print(name)
