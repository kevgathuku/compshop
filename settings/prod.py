import os

from .base import *


DEBUG = False

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']

ADMINS = (
    ("Kevin Ndung'u", 'kevgathuku@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compshop_production',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}
