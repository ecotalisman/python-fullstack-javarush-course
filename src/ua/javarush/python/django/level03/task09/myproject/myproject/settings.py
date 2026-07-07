"""
Django project settings.
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key — in a real project, it must be kept secret!
SECRET_KEY = 'django-insecure-zaminit_na_nastashij_sekretniy_kluch'

# Debug mode — enable only during development!
DEBUG = True

# List of allowed hosts — during development, it can be left empty
ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',            # Django admin application
    'django.contrib.auth',             # Authentication application
    'django.contrib.contenttypes',     # Application for working with content types
    'django.contrib.sessions',         # Application for working with sessions
    'django.contrib.messages',         # Application for the messages framework
    'django.contrib.staticfiles',      # Application for working with static files
    'app',                             # Our custom application
]

# Define the middleware list
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

# Django template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add paths to template folders here
        'APP_DIRS': True,  # Automatically search for templates in application folders
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Pass the request object to templates
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application for the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration — for simplicity, SQLite is used
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
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

# Localization and language settings
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files: CSS, JavaScript, images
STATIC_URL = 'static/'

# Default value for automatically created primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'