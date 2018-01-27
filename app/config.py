class Config:
    """
    General Configurations parent class
    https://newsapi.org/v2/top-headlines?language=en&country={}&category={}
    https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}
    """
    BASE_NEWS_API_URL = 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    SOURCE_NEWS_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    # pass


class ProdConfig(Config):
    """
    Production Configurations child class

    Args:
        Config parent class with the general app configurations
    """
    pass


class DevConfig(Config):
    """
    Development Configurations child class

    Args:
        Config parent class with the general app configurations
    """
    DEBUG = True
