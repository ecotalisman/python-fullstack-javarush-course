import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for cryptographic signing (replace it with your own in a real project)
SECRET_KEY = 'django-insecure-zdes-dolzhen_byt_sekretnyy_klyuch'

# Debug mode (True for development, False for production)
DEBUG = True

ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',           # Django admin panel
    'django.contrib.auth',            # Django authentication system
    'django.contrib.contenttypes',    # Django content types
    'django.contrib.sessions',        # Sessions
    'django.contrib.messages',        # Messages framework
    'django.contrib.staticfiles',     # Serving static files
    'app',                            # Our application for working with users
]

# List of middleware
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
        'DIRS': [],  # You can specify paths to additional template directories here
        'APP_DIRS': True,  # Search for templates in each application directory
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

# Database configuration (SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password complexity validation settings
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

# Settings for working with static files
STATIC_URL = 'static/'

# Default field setting for the model
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'