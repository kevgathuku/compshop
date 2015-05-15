import os

from .base import *

INSTALLED_APPS += ("django_nose",)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ['SECRET_KEY']
