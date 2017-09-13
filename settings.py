import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'kobis',
    #     'USER': 'postgres',
    #     'PASSWORD': 'dnwls895',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kobis',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'danbi',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'kobis',
)

SECRET_KEY = 'c2e@+4y8akeaf!=l!g%-7g+f^_v8h0h4m3=h=4n^9%tj$6(5@@'
