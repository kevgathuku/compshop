from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Make debug_toolbar rely on the version of jQuery that already exists
# Don't load external jquery
DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'JQUERY_URL': '',
}

BOOTSTRAP3 = {
    # Path to local Bootstrap CSS file
    'css_url': '/static/css/bootstrap.css',
    # Path to local jQuery
    'jquery_url': '/static/js/jquery.js',
    # Path to local bootstrap.js
    'javascript_url': '/static/js/bootstrap.js',
}
