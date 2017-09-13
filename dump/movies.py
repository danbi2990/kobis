if __name__ == '__main__':
    import sys
    sys.path.insert(0, "/home/jake/Dev/kobis")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from os.path import isfile, join
from django.db.utils import IntegrityError
from json_file import JsonFile
from settings import DATA_DIR
from kobis.models import Movies


path = join(DATA_DIR, 'movies')
files = [f for f in os.listdir(path) if isfile(join(path, f))]
# print(files)
# file = JsonFile(path)
# data = file.load()

for filename in files:
    file = join(path, filename)
    jsonfile = JsonFile(file)
    data = jsonfile.load()['movieListResult']
    movieList = data['movieList']
    for item in movieList:
        b = Movies(boxofficeType=boxofficeType, showRange=showRange, **item)
        try:
            b.save()
        except IntegrityError:
            break
