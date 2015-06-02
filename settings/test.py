import os

import dj_database_url

from .base import *

INSTALLED_APPS += ("django_nose",)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DEBUG = True

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
            'debug': True,
        },
    },
]

SECRET_KEY = 'TESTing SecRet KeY'
