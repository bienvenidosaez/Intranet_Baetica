# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
    #PROJECT_DIR.child("static"),
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)

# SECURITY
SECRET_KEY = '(__b8z0w!g@2vgn&ojyk0@*gpq_01!^x=br1mb*&^xqhoy*@w%'

INSTALLED_APPS = (
    # Admin Tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    # End of Admin Tools

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third part app
    'south',
    'mockups',

    # My apps
    'empleados',
    'clientes',
    'proyectos',
    'costes',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'intranet.urls'
WSGI_APPLICATION = 'intranet.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

AUTH_USER_MODEL = 'empleados.Empleado'
