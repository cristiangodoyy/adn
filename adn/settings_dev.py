from adn.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'adn',
        'PASSWORD': 'adn',
        'NAME': 'adn_dev',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
