"""
Django settings for the myproject project.

This file contains the minimal configuration required for the project to work,
as well as the registered applications, including our custom 'app' application.
"""
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for the project (in real applications, keep it secret)
SECRET_KEY = 'django-insecure-change-me-please'

# Debug mode enabled for development (do not use DEBUG=True in production)
DEBUG = True

ALLOWED_HOSTS = []

# Installed Django applications
INSTALLED_APPS = [
    'django.contrib.admin',         # Django admin panel
    'django.contrib.auth',          # Authentication system
    'django.contrib.contenttypes',  # Working with content types
    'django.contrib.sessions',      # Session mechanism
    'django.contrib.messages',      # Messages framework
    'django.contrib.staticfiles',   # Static files support
    'app',                          # Our custom application with the Class-Based View
]

# Middleware – the chain of intermediate request handlers
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL config of the project
ROOT_URLCONF = 'myproject.urls'

# Django template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Here you can specify directories containing templates
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

# WSGI application of the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration (using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password settings (validators)
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

# URL for static files
STATIC_URL = 'static/'

# Default value for the auto-increment field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'