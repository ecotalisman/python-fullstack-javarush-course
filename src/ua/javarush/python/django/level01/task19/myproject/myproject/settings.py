import os
from pathlib import Path

# Define the base project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key, in production it should be stored in a secure place
SECRET_KEY = 'your-secret-key-here'

# Debug mode is enabled, do not use it in production
DEBUG = True

# List of domains from which requests are allowed
ALLOWED_HOSTS = []

# List of installed Django applications
INSTALLED_APPS = [
    'django.contrib.admin',           # Admin interface
    'django.contrib.auth',            # Authentication system
    'django.contrib.contenttypes',    # Working with content types
    'django.contrib.sessions',        # Session mechanism
    'django.contrib.messages',        # Messages framework
    'django.contrib.staticfiles',     # Static file management
    'app',                            # Our application that contains the Author model
]

# List of middleware that processes requests
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Main URL routing file
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add paths to your own templates here
        'APP_DIRS': True,  # Automatically search for templates in application folders
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

# Defines the WSGI application for deployment
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings, SQLite is used by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators for users
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

# Static files settings
STATIC_URL = '/static/'

# Automatically set the default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
