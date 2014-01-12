# -*- coding: utf-8 -*-

# settings/local.py
from .base import *

# SECURITY
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']

# EMAIL SERVER
#EMAIL_HOST = "localhost"
#EMAIL_PORT = 1025

# DATABASE LOCAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
