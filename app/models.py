class Source:
    """
    Source class to define news source object
    """

    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    """
    Defines what we want our articles object to look like
    """

    def __init__(self,
                 id,
                 name,
                 author,
                 title,
                 description,
                 url,
                 urlToImage,
                 publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
