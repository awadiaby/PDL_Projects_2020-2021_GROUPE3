import unittest
from os import path

from main import extract, extract_wikitables

class TestExtractor(unittest.TestCase):

    # constants


    def test_check_output(self):
        self.assertTrue(path.exists("output/html"))
        self.assertTrue(path.exists("output/csv"))


    def test_extractor(self):
        extract_done = False
        extract()
        extract_done = True
        self.assertTrue(extract_done, "Extraction failed")


    def test_extract_wikitables_1(self):
        result, nbwikitables = extract_wikitables(wikiurl='Comparison_of_email_clients')
        self.assertTrue(result)
        self.assertEqual(nbwikitables, 11)


if __name__ == '__main__':
    unittest.main()