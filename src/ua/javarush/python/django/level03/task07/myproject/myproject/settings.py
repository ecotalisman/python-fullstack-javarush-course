"""
Minimal settings for a Django project.
Django version: 5.1, Python: 3.12
"""

from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key, use a more secure value in production
SECRET_KEY = 'django-insecure-zamenite_na_sviy_sekretnyy_klyuch'

# Debug mode, do not enable in production
DEBUG = True

# List of allowed hosts
ALLOWED_HOSTS = []

# Registered applications
INSTALLED_APPS = [
    'django.contrib.admin',              # Django admin panel
    'django.contrib.auth',               # Authentication system
    'django.contrib.contenttypes',       # Working with content types
    'django.contrib.sessions',           # Working with sessions
    'django.contrib.messages',           # Message system
    'django.contrib.staticfiles',        # Static files
    'myapp',                             # Our application that contains the welcome_view function
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',      # Basic security mechanisms
    'django.contrib.sessions.middleware.SessionMiddleware', # Session support
    'django.middleware.common.CommonMiddleware',            # Common tasks
    'django.middleware.csrf.CsrfViewMiddleware',            # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # User authentication
    'django.contrib.messages.middleware.MessageMiddleware', # Working with messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Protection against clickjacking
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Template directories; you can add your own directories here
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',    # Debug information
                'django.template.context_processors.request',  # Request object in templates
                'django.contrib.auth.context_processors.auth', # Authentication information
                'django.contrib.messages.context_processors.messages', # Messages
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Use SQLite as the database for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # SQLite
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings, can be changed if necessary
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
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = 'static/'

# Default value for automatic model fields
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'