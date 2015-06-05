import os

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

INSTALLED_APPS += ('debug_toolbar', 'django_seed',)
