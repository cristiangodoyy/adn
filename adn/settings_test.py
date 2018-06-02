from adn.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'NAME': 'adndev',
        'HOST': '/cloudsql/adn-ml:us-central1:adndev',
        'PORT': '5432',
    }
}
