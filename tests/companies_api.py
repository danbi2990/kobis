#!/usr/bin/env python3
import unittest
from api import Companies


class TestCompanies(unittest.TestCase):

    def setUp(self):
        # self.api = Companies("1", "10")
        pass

    def tearDown(self):
        pass

    # @unittest.skip("Test skipped")
    def test_save_file(self):
        api = Companies("1", "10")
        print(api.url)
        api.save_data()

    @unittest.skip("Test skipped")
    def test_api_call(self):
        api = Companies("1", "10")
        api.api_call()
        print(api.response.text[:50])
        # self.assertEqual(api.response.text[:50], '{"movieListResult":{"totCnt":61305,"source":"영화진흥위')
