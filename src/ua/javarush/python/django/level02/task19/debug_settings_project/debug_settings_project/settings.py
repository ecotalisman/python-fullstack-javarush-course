"""
Django settings for the debug_settings_project project.
"""

from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug settings (DEBUG)
DEBUG = True

# Application settings
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# URL route settings
ROOT_URLCONF = 'debug_settings_project.urls'

# Database settings, use SQLite by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Language and time zone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files settings
STATIC_URL = '/static/'
