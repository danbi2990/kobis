import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import unittest
from api import MovieList
from json_file import JsonFile
from settings import DATA_DIR
from kobis.models import Movies


path = os.path.join(DATA_DIR, 'movies', 'movies_1.json')
file = JsonFile(path)
data = file.load()

# print(data)
data = data['movieListResult']
movieList = data['movieList']
for item in movieList:
    m = Movies(**item)
    m.save()


first = Movies.objects.all()[0]
print(first)


class TestJsonToDbMovies(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_file(self):

