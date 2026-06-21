"""
Django settings for the myproject project.
Generated using the "django-admin startproject" command for Django 5.1.

This configuration is already set up to work with an SQLite database.
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY – use a unique value for production!
SECRET_KEY = 'django-insecure-please-change-me'

# DEBUG=True can be used in development mode
DEBUG = True

# List of allowed hosts. For development, it can be left empty.
ALLOWED_HOSTS = []

# Install the applications included with Django
INSTALLED_APPS = [
    'django.contrib.admin',             # Django administration application
    'django.contrib.auth',              # Authentication system
    'django.contrib.contenttypes',      # Content types system
    'django.contrib.sessions',          # Session handling modules
    'django.contrib.messages',          # Messages framework
    'django.contrib.staticfiles',       # Static files handling
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # Security measures
    'django.contrib.sessions.middleware.SessionMiddleware', # Session handling
    'django.middleware.common.CommonMiddleware',            # Common request settings
    'django.middleware.csrf.CsrfViewMiddleware',            # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentication handling
    'django.contrib.messages.middleware.MessageMiddleware', # Messages handling
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protection against clickjacking attacks
]

# Specify the URL routing module
ROOT_URLCONF = 'myproject.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS – here you can specify the path to custom templates
        'DIRS': [],
        'APP_DIRS': True,  # Automatically search for templates in application directories
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

# WSGI application for deploying the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        # Use Django's built-in SQLite engine
        'ENGINE': 'django.db.backends.sqlite3',

        # Path to the database file located in the project root directory
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validator settings
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

# Project localization
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Important! The project uses the SQLite database specified in DATABASES.
