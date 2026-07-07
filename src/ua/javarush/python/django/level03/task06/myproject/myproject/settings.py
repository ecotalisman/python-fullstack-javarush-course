"""
Django settings for the myproject project.
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key, replace it with your own key for production
SECRET_KEY = 'django-insecure-replace-with-your-secret-key'

# Debug mode - True for development
DEBUG = True

ALLOWED_HOSTS = []

# Install the applications used in the project
INSTALLED_APPS = [
    'django.contrib.admin',            # Admin interface
    'django.contrib.auth',             # Authentication system
    'django.contrib.contenttypes',     # Working with content types
    'django.contrib.sessions',         # Working with sessions
    'django.contrib.messages',         # Message system
    'django.contrib.staticfiles',      # Working with static files
    'app_name',                        # Our custom application
]

# Middleware - intermediate software for processing requests
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Main URL module of the project
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Additional template folders can be specified here
        'APP_DIRS': True,  # Automatic search for templates in applications
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

# WSGI application for running on the server
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration, using SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validators for password checking
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

# Localization: language and time zone
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Settings for automatic primary key field detection for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'