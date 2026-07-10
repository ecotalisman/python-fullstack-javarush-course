"""
Django settings for the myproject project.
Basic settings have been created for running the project in debug mode.
"""
import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key (must be replaced with a secure value in production)
SECRET_KEY = 'replace-this-secret-key-with-a-very-secret-key'

# Debug mode
DEBUG = True

ALLOWED_HOSTS = []

# Registered Django applications
INSTALLED_APPS = [
    'django.contrib.admin',            # Admin panel
    'django.contrib.auth',             # Authentication system
    'django.contrib.contenttypes',     # Working with content types
    'django.contrib.sessions',         # Sessions
    'django.contrib.messages',         # Messages for users
    'django.contrib.staticfiles',      # Working with static files
    'myapp',                           # add my application

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

# Main routes file
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify additional template directories here
        'APP_DIRS': True,  # Automatically search for templates in applications
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

# WSGI application for the server
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database, SQLite is used for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Localization and time zone settings
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Default field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'