"""
Settings for the "myproject" Django project.

This file contains the minimum settings required to run the project.
Important: do not use this secret key in production!
"""
import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, replace it with a unique value in a real project
SECRET_KEY = 'django-insecure-zaminit_na_spravzhniy_sekretnyy_kluch'

# Debug mode - True for development, False for production
DEBUG = True

ALLOWED_HOSTS = []

# Define installed applications
INSTALLED_APPS = [
    'django.contrib.admin',           # Django admin panel
    'django.contrib.auth',            # Authentication system
    'django.contrib.contenttypes',    # Content types system
    'django.contrib.sessions',        # Session handling
    'django.contrib.messages',        # Messages framework
    'django.contrib.staticfiles',     # Static files
    'news',

]

# Define middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL module
ROOT_URLCONF = 'myproject.urls'

# Django template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directory for shared project templates
        'APP_DIRS': True,                  # Search for templates in all application folders
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

# Define the WSGI application
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings, using SQLite for simplicity
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

# Local settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Automatic default field selection for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
