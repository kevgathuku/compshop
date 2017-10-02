import dj_database_url

from .local import *

INSTALLED_APPS += ("django_nose",)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DEBUG = True

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = 'TESTing SecRet KeY'
