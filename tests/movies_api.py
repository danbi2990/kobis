#!/usr/bin/env python3
import unittest
from api import Movies


class TestMovies(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @unittest.skip("Test skipped")
    def test_save_file(self):
        api = Movies("1", "10")
        api.save_data()

    @unittest.skip("Test skipped")
    def test_api_call(self):
        api = Movies("1", "10")
        api.api_call()
        self.assertEqual(api.response.text[:50], '{"movieListResult":{"totCnt":61305,"source":"영화진흥위')
