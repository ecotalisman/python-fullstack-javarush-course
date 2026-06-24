from pathlib import Path
import os

from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT

# Project base directory, the project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, in production it must be stored securely
SECRET_KEY = 'django-insecure-vashe-sekretnyy-klyuch'

# Disabling DEBUG in production is not recommended
DEBUG = True

ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',             # Django administrative interface
    'django.contrib.auth',              # Authentication system
    'django.contrib.contenttypes',      # Content type handling
    'django.contrib.sessions',          # Session handling
    'django.contrib.messages',          # Messages framework
    'django.contrib.staticfiles',       # Static files handling
    'app',                              # Our custom application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# Project template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # By default, templates are searched in application directories when APP_DIRS=True
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Use SQLite as the database for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password strength validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings, CSS, JS, images
STATIC_URL = 'static/'

# ========================
# Media files settings
# ========================

# MEDIA_URL - URL prefix for accessing media files in the browser
MEDIA_URL = '/media/'

# MEDIA_ROOT - path to the directory on disk for storing uploaded media files
MEDIA_ROOT = BASE_DIR / 'media'

# Default field type for model auto-created fields
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
