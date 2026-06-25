"""
Settings for the Django project "myproject".
Versions: Django 5.1, Python 3.12
"""

from pathlib import Path

# Project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, do not use this key in production!
SECRET_KEY = 'django-insecure-zamenite-na-nastoyahtshiy-klyuch'

DEBUG = True

ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',          # Admin panel
    'django.contrib.auth',           # Authentication system
    'django.contrib.contenttypes',   # Content types
    'django.contrib.sessions',       # Sessions
    'django.contrib.messages',       # Messages framework
    'django.contrib.staticfiles',    # Static files
    'library',                       # Our "library" application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # Common settings, for example, adding headers
    'django.middleware.csrf.CsrfViewMiddleware',  # Protection against request forgery
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication check
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

# Django templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Here you can add paths to template directories
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Use SQLite as the default database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators for authentication
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
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for accessing static files
STATIC_URL = 'static/'

# Default field setting for auto-incrementing primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
