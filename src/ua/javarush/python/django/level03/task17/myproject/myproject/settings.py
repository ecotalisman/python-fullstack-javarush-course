"""
Django settings for the myproject project.

Configured for the task: extracting the id parameter from the URL
and returning the string "Your ID: X".
"""
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key (in a real project, this key must be hidden)
SECRET_KEY = 'django-insecure-zamenitce_cey_kluch_na_spravzhnij'

# Debug mode is enabled for development
DEBUG = True

# Allowed hosts (left empty for development)
ALLOWED_HOSTS = []

# Installed applications, including standard ones and our custom "app" application
INSTALLED_APPS = [
    'django.contrib.admin',            # Django admin interface
    'django.contrib.auth',             # Django authentication
    'django.contrib.contenttypes',     # Working with content types
    'django.contrib.sessions',         # Sessions mechanism
    'django.contrib.messages',         # Messages system
    'django.contrib.staticfiles',      # Static files support
    'app',                             # Our custom application for handling URLs with the id parameter
]

# Define middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Main URL configuration of the project
ROOT_URLCONF = 'myproject.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # You can specify paths to template directories here
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Context processors for templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application for the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings, SQLite is used for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
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

# Language and time zone
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Define the field for automatically generating primary keys in models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'