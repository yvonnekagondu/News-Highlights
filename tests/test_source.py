import unittest
from app.models import Source


class NewsSource(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source class
    """
    def setUp(self):
        """
        Set up method that runs before every TestCase
        """
        self.new_source = Source("ktn-news",
                                "ktn-news",
                                "north east west and south",
                                "https://ntv.nation.co.ke",
                                "general",
                                "Kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
