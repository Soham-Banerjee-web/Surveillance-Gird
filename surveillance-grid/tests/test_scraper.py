import unittest
from src.scraper.selenium_runner import SeleniumRunner
from src.scraper.parsers import parse_data

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.runner = SeleniumRunner()
        self.test_url = "http://example.com"

    def test_scrape_data(self):
        data = self.runner.scrape(self.test_url)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)

    def test_parse_data(self):
        raw_data = "<html><body><h1>Test Title</h1></body></html>"
        parsed_data = parse_data(raw_data)
        self.assertIn("title", parsed_data)
        self.assertEqual(parsed_data["title"], "Test Title")

    def tearDown(self):
        self.runner.quit()

if __name__ == '__main__':
    unittest.main()