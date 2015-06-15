import os

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

INSTALLED_APPS += ('django_seed',)

BOOTSTRAP3 = {
    # Path to local Bootstrap CSS file
    'css_url': '/static/css/bootstrap.css',
    # Path to local jQuery
    'jquery_url': '/static/js/jquery.js',
    # Path to local bootstrap.js
    'javascript_url': '/static/js/bootstrap.js',
}
