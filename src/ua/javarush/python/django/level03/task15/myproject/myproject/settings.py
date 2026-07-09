"""
Django project settings for the myproject project.
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, do not use it in production
SECRET_KEY = 'django-insecure-abc123'

# Debug mode. In production, DEBUG must be False.
DEBUG = True

ALLOWED_HOSTS = []

# Install the applications used in the project
INSTALLED_APPS = [
    'django.contrib.admin',          # Django admin application
    'django.contrib.auth',           # User authentication module
    'django.contrib.contenttypes',   # Support for working with content types
    'django.contrib.sessions',       # Working with sessions
    'django.contrib.messages',       # Messages system
    'django.contrib.staticfiles',    # Working with static files
    'app',                           # Our custom application
]

# Define middleware that processes requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL routing file
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify the path to the templates folder here
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

# Database settings. SQLite is used for simplicity.
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

# Localization and time settings
LANGUAGE_CODE = 'uk-ua'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Default field setting for the auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'