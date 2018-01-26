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

    def __init__(self,
                 id, name, author, title, url, urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
