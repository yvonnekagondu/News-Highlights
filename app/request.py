import urliib.request
import json
from .models import Source
from .models import Articles

#Getting api_key
api_key = None
#Getting the base_url
base_url = None
#Getting source_url
source_url = None

def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEWS_API_URL']
    source_url = app.config['SOURCE_NEWS_URL']

def get_sources(coutry, category):
    """
    Function that gets the json response to our url request
    """

    get_news_url = base_url.format(coutry,category, api_key)
    with urliib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        source_results = None

    #urliib opens and reads URLs
        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)

    return source_results

def process_results(news_list):
    """
    Function that processes new list dictionary and turns them to a list of objects
    Args:
        news_list: A list of dictionaries that contain news sources_list
    Returns:
        news_results: A list of news objects
    """
    new_results = []
    for source in news_list:
        id = source.get('id')
        print(id)
        name = source.get('name')
        print(name)
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            source_object = Source(id,
                                    name,
                                    description,
                                    url,
                                    category,
                                    country)
            news_results.append(source_object)
    return news_results
#The method get() returns a value for the given key. If key is not available then returns default value None.

def get_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_sources_news_url = source_url.format(
        id,api_key)
