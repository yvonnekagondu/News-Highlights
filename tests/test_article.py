import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    """
    Test Class to test the behaviour of the Articles class
    """
    def setUp(self):
        """
        Set up method that runs before every TestCase
        """
        self.new_articles = Articles("ntv-news",
                                "ntv-news",
                                "Nimro Taabu",
                                "Mudavadi: I did not believe in Raila Odinga's 'swearing-in'",
                                "National Super Alliance (NASA) co-principal Musalia Mudavadi has previously said that his skipping of Raila Odinga's 'swearing-in' did not make him a coward.",
                                "https://www.standardmedia.co.ke/ktnnews/video/2000153075/-mudavadi-i-did-not-believe-in-raila-odinga-s-swearing-in",
                                "general",
                                "Sunday 8 Apr 2018 10:40 pm")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
