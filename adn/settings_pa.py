from adn.settings import *

ALLOWED_HOSTS = ['cristiangodoy.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'adn.sqlite3'),
    }
}
