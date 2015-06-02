import os

import dj_database_url

from .base import *


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = (
    ("Kevin Ndung'u", 'kevgathuku@gmail.com'),
)

MANAGERS = ADMINS

DATABASES['default'] = dj_database_url.config()

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': False,
        },
    },
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Add django-s3-storage to INSTALLED_APPS
INSTALLED_APPS += ('django_s3_storage',)

# Media Files Storage Backend
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"

# The region to connect to when storing files.
AWS_REGION = "eu-west-1"

# The AWS access key used to access the storage buckets.
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

# The AWS secret access key used to access the storage buckets.
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# The S3 bucket used to store uploaded files.
AWS_S3_BUCKET_NAME = os.environ['S3_BUCKET']
