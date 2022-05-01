import unittest
from app.models import Source
# for testing the sources na d articles classes.


class TestSource(unittest.TestCase):
    """
    Test class to test the news sources class
    """

    # setUP meethod
    def setUp(self):
        '''
        this setter executes prior to each test.
        '''

        self.new_source = Source("abc-news", "ABC News",  "Your trusted source for breaking news, analysis",
                                 "https://abcnews.go.com", "general", "en", "us")

    def test_instance(self):
        """
        test_instance: checks if an object is an instance of the class
        """
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
        test_init to test if movie object initializes correctly
        '''
        self.assertEqual(self.new_source.id, "abc-news")
        self.assertEqual(self.new_source.name, "ABC News")
        self.assertEqual(self.new_source.description,
                         "Your trusted source for breaking news, analysis")
        self.assertEqual(self.new_source.url, "https://abcnews.go.com")
        self.assertEqual(self.new_source.category, "general")
        self.assertEqual(self.new_source.language, "en")
        self.assertEqual(self.new_source.country, "us")


if __name__ == '__main__':
    unittest.main()
