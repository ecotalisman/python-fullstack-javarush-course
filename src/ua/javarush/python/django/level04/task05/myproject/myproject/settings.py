"""
Settings of the "myproject" Django project.
Settings for development. In production, the security parameters must be configured.
"""
from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key of the project (a test one can be used for development)
SECRET_KEY = "django-insecure-zaminyty-na-naspravdi-secret-key"

# Debug mode for development
DEBUG = True

ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    "django.contrib.admin",            # Django admin site
    "django.contrib.auth",             # User authentication
    "django.contrib.contenttypes",     # Working with content types
    "django.contrib.sessions",         # Sessions
    "django.contrib.messages",         # Messages
    "django.contrib.staticfiles",      # Static files
    "app",                             # Our custom application
]

# List of middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Root URL config of the project
ROOT_URLCONF = "myproject.urls"

# Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Paths to template directories can be added here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = "myproject.wsgi.application"

# Database settings (SQLite for simplicity)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validator settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Language and locale
LANGUAGE_CODE = "uk-ua"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = "static/"

# Default value for new model fields
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"