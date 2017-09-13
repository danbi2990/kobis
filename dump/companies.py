if __name__ == '__main__':
    import sys
    sys.path.insert(0, "/home/jake/Dev/kobis")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.db.utils import IntegrityError
from json_file import JsonFile
from settings import DATA_DIR
from kobis.models import Companies


path = os.path.join(DATA_DIR, 'companies', 'companies_1_10.json')
file = JsonFile(path)
data = file.load()

data = data['companyListResult']['companyList']
for item in data:
    b = Companies(**item)
    try:
        b.save()
    except IntegrityError:
        pass


first = Companies.objects.all()[0]
print(first)
