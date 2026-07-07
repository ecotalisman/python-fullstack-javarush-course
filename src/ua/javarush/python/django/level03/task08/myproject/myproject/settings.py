"""
Django project settings.
"""

import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for cryptographic signing, must be changed in production
SECRET_KEY = 'django-insecure-CHANGE-ME'

# Debug mode, for development
DEBUG = True

ALLOWED_HOSTS = []  # Can be left empty for local development

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',         # Django admin panel
    'django.contrib.auth',          # Authentication system
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',      # Session mechanism
    'django.contrib.messages',      # Message system
    'django.contrib.staticfiles',   # Working with static files
    'myapp',                        # Our custom application
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration for the project
ROOT_URLCONF = 'myproject.urls'

# Django template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Paths to template directories can be added here
        'APP_DIRS': True,  # Automatically search for templates in application directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',   # Adds debug information to templates
                'django.template.context_processors.request', # Adds the request object to the template context
                'django.contrib.auth.context_processors.auth', # Authentication data
                'django.contrib.messages.context_processors.messages', # Messages
            ],
        },
    },
]

# WSGI application for deploying the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings, using SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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

# Localization and time settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True   # Enable the internationalization system
USE_TZ = True     # Enable time zone support

# URL for static files, for example, CSS, JavaScript, images
STATIC_URL = 'static/'

# Default field setting for automatically creating primary keys in models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'