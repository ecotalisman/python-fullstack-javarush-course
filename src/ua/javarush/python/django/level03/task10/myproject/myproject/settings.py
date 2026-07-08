"""
Django project settings.

Minimal configuration for running the project.
"""

import os
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key (in real projects, do not store it openly)
SECRET_KEY = 'django-insecure-заміни-на-справжній-секретний-ключ'

# Debug mode is enabled for development
DEBUG = True

# Allowed hosts (left empty for development)
ALLOWED_HOSTS = []

# Set the list of applications connected to the project
INSTALLED_APPS = [
    'django.contrib.admin',         # Admin application
    'django.contrib.auth',          # Authentication application
    'django.contrib.contenttypes',  # Content types system
    'django.contrib.sessions',      # Sessions mechanism
    'django.contrib.messages',      # Messages system
    'django.contrib.staticfiles',   # Static files handling
    'blog',                         # Our custom blog application
]

# List of middleware for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration of the project
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Additional template directories can be specified here
        'APP_DIRS': True,  # Automatically search for templates in each application
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

# Use SQLite as the default database
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

# Localization and time zone
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files: CSS, JavaScript, images
STATIC_URL = 'static/'

# Default setting for the model primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'