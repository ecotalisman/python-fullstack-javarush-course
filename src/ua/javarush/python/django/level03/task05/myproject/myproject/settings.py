"""
Django project settings.

Note: this file contains minimal settings,
not intended for production use.
"""
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, do not use in production
SECRET_KEY = 'django-insecure-zamenit-na-nastoyashchyi-kliuch'

# Debug mode, DEBUG=True for development
DEBUG = True

ALLOWED_HOSTS = []

# Install the applications used in the project
INSTALLED_APPS = [
    'django.contrib.admin',         # Django admin panel
    'django.contrib.auth',          # Authentication system
    'django.contrib.contenttypes',  # Content type system
    'django.contrib.sessions',      # Session mechanism
    'django.contrib.messages',      # Message system
    'django.contrib.staticfiles',   # Working with static files
    'app',                          # Our custom application
]

# Middleware for processing requests
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'myproject.urls'

# Django template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Template directories can be specified here
        'APP_DIRS': True,  # Search for templates in applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Request object in the context
                'django.contrib.auth.context_processors.auth',  # User information
                'django.contrib.messages.context_processors.messages',  # Passing messages
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration, using SQLite for simplicity
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
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization settings
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Automatic field definition for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'