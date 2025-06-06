# config/settings/production.py

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['django-siscont-1.onrender.com']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('DB_NAME'),
       'USER': config('DB_USER'),
       'PASSWORD': config('DB_PASSWORD'),
       'HOST': config('DB_HOST'),
       'PORT': config('DB_PORT'),
   }
}
