"""
Settings for the Django project myproject.
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for development only, do not use in production
SECRET_KEY = 'django-insecure-secret-key-for-dev'

# Debug mode is enabled for development
DEBUG = True

# List of allowed hosts, currently empty
ALLOWED_HOSTS = []

# Define installed applications
INSTALLED_APPS = [
    'django.contrib.admin',          # Django admin panel
    'django.contrib.auth',           # Django authentication system
    'django.contrib.contenttypes',   # Content types support
    'django.contrib.sessions',       # Sessions support
    'django.contrib.messages',       # Messages framework
    'django.contrib.staticfiles',    # Static files support
    'myapp',
]

# Define middleware that process requests/responses
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

# Django template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Additional template directories, if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',     # Pass debug information to templates
                'django.template.context_processors.request',   # Adds the HTTP request to the context
                'django.contrib.auth.context_processors.auth',  # User authentication information
                'django.contrib.messages.context_processors.messages',  # Messages for templates
            ],
        },
    },
]

# WSGI application for project deployment
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings, using SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validator settings
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

# Default value for automatically created primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
