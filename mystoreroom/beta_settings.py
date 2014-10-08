from mystoreroom.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'mystoreroom.janosgyerik.com']

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # path to database file if using sqlite3.
        'NAME': 'sqlite3.db',
        # Not used with sqlite3.
        'USER': '',
        # Not used with sqlite3.
        'PASSWORD': '',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b!&l+fuwi6db7hn@_^3dkfl=js=v4#ds5mqzt1)-sjzdp_wtvk'

from whitelist_auth.auth import require_whitelisted_wrapper
require_whitelisted_wrapper()
