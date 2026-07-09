# Main settings of the Django project

from pathlib import Path

# Get the base path of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Project secret key (in real projects, store it securely)
SECRET_KEY = 'django-insecure-very-secret-key'

# Debug mode: True for development, False for production
DEBUG = True

# List of allowed hosts
ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin',             # Django admin panel
    'django.contrib.auth',              # Authentication system
    'django.contrib.contenttypes',      # Content types system
    'django.contrib.sessions',          # Working with user sessions
    'django.contrib.messages',          # Messages system
    'django.contrib.staticfiles',       # Serving static files
    'app',                              # Our custom application
]

# Middleware — list of intermediate layers for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URLConf of the project
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Folder for templates, add it if needed
        'APP_DIRS': True,   # Automatically search for templates in application folders
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

# WSGI application for deploying the project on a web server
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database configuration, SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Language settings
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'

# Default field for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'