"""
Django settings for the debug_settings_project project.
"""

from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug settings (DEBUG)
DEBUG = False

# Application settings
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sslserver',
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

# Security setting: enable CSRF protection at the HTTPS level
CSRF_COOKIE_SECURE = True  # CSRF cookies will be transmitted only over HTTPS

# Security setting: protect sessions at the HTTPS level
SESSION_COOKIE_SECURE = True  # Session cookies will be transmitted only over HTTPS
