"""
TODO:
-Should be able to return from various news sources
-See the news articles from the new source
-See the image description and time the news article was
-created Route to the article itself."""


class Source:
    """
    Source class to define news source object
    """

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
