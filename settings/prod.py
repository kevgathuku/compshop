import os

import dj_database_url

from .base import *


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']

# Enable Offline Compression for files
COMPRESS_OFFLINE = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SERVER_EMAIL = "<Comptronics Error> kevgathuku@gmail.com"

ADMINS = (
    ("Kevin Ndung'u", 'kevgathuku@gmail.com'),
)

MANAGERS = ADMINS

DATABASES['default'] = dj_database_url.config()

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Djrill Settings
MANDRILL_API_KEY = os.environ['MANDRILL_API_KEY']

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

DEFAULT_FROM_EMAIL = "<Comptronics> comptronicsltd@gmail.com"
