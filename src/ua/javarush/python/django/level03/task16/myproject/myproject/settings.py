"""
Django project settings.
"""
from pathlib import Path  # Import Path for working with the file system

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key (in production, this key must be hidden)
SECRET_KEY = 'django-insecure-zamenite-na-svij-klyuch'

DEBUG = True  # Debug mode is enabled (for development only)

ALLOWED_HOSTS = []  # List of hosts allowed to connect

# Install the applications required for the project
INSTALLED_APPS = [
    'django.contrib.admin',            # Admin application
    'django.contrib.auth',             # Django authentication system
    'django.contrib.contenttypes',     # Working with content types
    'django.contrib.sessions',         # Working with sessions
    'django.contrib.messages',         # Messages system
    'django.contrib.staticfiles',      # Static files support
    'app',                             # Our custom application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',    # Improved security
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'django.middleware.common.CommonMiddleware',        # Common middleware settings
    'django.middleware.csrf.CsrfViewMiddleware',        # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentication
    'django.contrib.messages.middleware.MessageMiddleware',    # Message handling
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protection against clickjacking
]

ROOT_URLCONF = 'myproject.urls'  # Defines the root URL configuration of the project

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # List of directories where templates are located
        'APP_DIRS': True,  # Automatically search for templates in application directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',      # Debug information
                'django.template.context_processors.request',    # Request object
                'django.contrib.auth.context_processors.auth',   # Authentication data
                'django.contrib.messages.context_processors.messages',  # Messages
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'  # Entry point for the WSGI server

# Database configuration: using SQLite for development simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite engine
        'NAME': BASE_DIR / 'db.sqlite3',         # Database file
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

# Localization and time zone
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'