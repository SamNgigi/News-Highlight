#!/usr/bin/env python3.6
import unittest
from app.models import Source
# Source = news_source.Source


class NewsSource(unittest.TestCase):
    """
    Test Class to test the behaviours we expect in our applications
    """

    def setUp(self):
        """
        This will function runs before every Test. Its a
        built in unittest function that allows us to test our object.
        """

        self.new_source = Source("abc-news",
                                 "ABC News",
                                 "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
                                 "http://abcnews.go.com",
                                 "general",
                                 "country")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


# if __name__ == '__main__':
#     unittest.main()
