import os
import json
import requests
from json_file import JsonFile
from settings import DATA_DIR


class BaseAPI:

    def __init__(self):
        self.urls = {
            "base": "",
            "daily_boxoffice": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json",
            "weekly_boxoffice": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json",
            "codes": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json",
            "movies": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json",
            "movie_details": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json",
            "companies": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json",
            "people": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json",
        }
        self.url = self.urls[self.api_name]
        self.params = {"key": "8ed1be3a773c6b4e6bccb8fe28296f98"}
        self.data_dir = os.path.join(DATA_DIR, self.api_name)
        self.response = ""

    def api_call(self):
        self.response = requests.get(self.url, self.params)

    def save_data(self):
        self.api_call()
        self.make_path()
        file = JsonFile(self.path)
        data = json.loads(self.response.text)
        file.save(data)

    def make_path(self):
        # self.path = os.path.join(self.data_dir, self.api_name + "_")
        raise NotImplementedError


class Movies(BaseAPI):

    def __init__(self, curPage, itemPerPage):
        self.api_name = "movies"
        super().__init__()
        self.params["curPage"] = curPage
        self.params["itemPerPage"] = itemPerPage

    def make_path(self):
        self.path = os.path.join(self.data_dir,
                                 self.api_name + "_" +
                                 self.params["curPage"] + "_" +
                                 self.params["itemPerPage"] + ".json")


class DailyBoxoffice(BaseAPI):

    def __init__(self, targetDt):
        self.api_name = "daily_boxoffice"
        super().__init__()
        self.params["targetDt"] = targetDt

    def make_path(self):
        self.path = os.path.join(self.data_dir,
                                 self.api_name + "_" +
                                 self.params["targetDt"] + ".json")


class Companies(BaseAPI):

    def __init__(self, curPage, itemPerPage):
        self.api_name = "companies"
        super().__init__()
        self.params["curPage"] = curPage
        self.params["itemPerPage"] = itemPerPage

    def make_path(self):
        self.path = os.path.join(self.data_dir,
                                 self.api_name + "_" +
                                 self.params["curPage"] + "_" +
                                 self.params["itemPerPage"] + ".json")


class People(BaseAPI):

    def __init__(self, curPage, itemPerPage):
        self.api_name = "people"
        super().__init__()
        self.params["curPage"] = curPage
        self.params["itemPerPage"] = itemPerPage

    def make_path(self):
        self.path = os.path.join(self.data_dir,
                                 self.api_name + "_" +
                                 self.params["curPage"] + "_" +
                                 self.params["itemPerPage"] + ".json")
