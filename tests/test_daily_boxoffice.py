#!/usr/bin/env python3
import unittest
from api import DailyBoxoffice


class TestDailyBoxoffice(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_file(self):
        api = DailyBoxoffice("20170824")
        api.save_data()

    @unittest.skip("Test skipped")
    def test_api_call(self):
        d = DailyBoxoffice("20170824")
        d.api_call()
        self.assertEqual(d.response.text[:50], '{"boxOfficeResult":{"boxofficeType":"일별 박스오피스","sh')

    def test_daily_boxoffice(self):
        d = DailyBoxoffice("20170826")
        self.assertEqual(d.url, "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json")
        self.assertEqual(str(d.params), "{'key': '8ed1be3a773c6b4e6bccb8fe28296f98', 'targetDt': '20170826'}")
