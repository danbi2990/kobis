import os
import json
import requests
from json_file import JsonFile

BASEDIR = os.path.join(os.path.dirname(__file__), "data")


class BaseAPI:

    def __init__(self):
        self.urls = {
            "base": "",
            "daily_boxoffice": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json",
            "weekly_boxoffice": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json",
            "code_list": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json",
            "movie_list": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json",
            "movie_info": "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json",
        }
        self.url = self.urls[self.api_name]
        self.params = {"key": "8ed1be3a773c6b4e6bccb8fe28296f98"}
        self.data_dir = os.path.join(BASEDIR, self.api_name)
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
        raise NotImplementedError


class MovieList(BaseAPI):

    def __init__(self):
        self.api_name = "movie_list"
        super().__init__()

    def make_path(self):
        self.path = os.path.join(self.data_dir, self.api_name + "_" +)


class DailyBoxoffice(BaseAPI):

    def __init__(self, targetDt):
        self.api_name = "daily_boxoffice"
        super().__init__()
        self.params["targetDt"] = targetDt

    def make_path(self):
        self.path = os.path.join(self.data_dir, self.api_name + "_" + self.params["targetDt"] + ".json")
