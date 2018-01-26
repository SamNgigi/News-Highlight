import unittest
from .models import news_source
Source = news_source.Source


class NewsSource(unittest.TestCase):
    """
    Test Class to test the behaviours we expect in our applications
    """

    def setUp(self):
        """
        This will function runs before every Test. Its a
        built in unittest function that allows us to test our object.
        """
