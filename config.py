import os

class Config:
    """
    General Configurations parent class
    https://newsapi.org/v2/top-headlines?language=en&country={}&category={}
    https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}
    """
    BASE_NEWS_API_URL = 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
