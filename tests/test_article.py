import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    """
    Test Case for news articles
    """

    def setUp(self):
        """
        Sets the values for the test runner to execute prior to each test case
        """
        self.new_article = Article( "Jay Peters", "Block and Blockstream are partnering with Tesla",
                               "Tesla's 3.8-megawatt Solar PV array and its 12 megawatt-hour Megapack will power the", "https://www.engadget.com/wikipedia-editors-vote-to-block-cryptocurrency-donations-113549175.html", "https://s.yimg.com/os/creatr-uploaded-images/2021-07/9f595ce0-de17-11eb-bef2-e1b1456d84ae", "2022-04-14T11:35:49Z", "Wikipedia editors have voted in favor of dropping cryptocurrency")

    def test_init(self):
        """
        test_init: test case for testing if object is initialized correctly
        """
        # self.assertEqual(self.new_article.source.id, "the-verge")
        # self.assertEqual(self.new_article.source.name, "The Verge")
        self.assertEqual(self.new_article.author, "Jay Peters")
        self.assertEqual(self.new_article.title,
                         "Block and Blockstream are partnering with Tesla")
        self.assertEqual(self.new_article.description,
                         "Tesla's 3.8-megawatt Solar PV array and its 12 megawatt-hour Megapack will power the")
        self.assertEqual(
            self.new_article.url, "https://www.engadget.com/wikipedia-editors-vote-to-block-cryptocurrency-donations-113549175.html")
        self.assertEqual(self.new_article.urlToImage,
                         "https://s.yimg.com/os/creatr-uploaded-images/2021-07/9f595ce0-de17-11eb-bef2-e1b1456d84ae")
        self.assertEqual(self.new_article.publishedAt, "2022-04-14T11:35:49Z")
        self.assertEqual(self.new_article.content,
                         "Wikipedia editors have voted in favor of dropping cryptocurrency")


# test runner
if __name__ == '__main__':
    unittest.main()
