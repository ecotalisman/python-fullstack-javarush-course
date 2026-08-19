from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for security (must be changed and kept secret in production)
SECRET_KEY = 'replace-this-with-a-secure-key'

# Debug mode, can be set to True during development
DEBUG = True

ALLOWED_HOSTS = []

# Declare the installed apps, including our "app" application
INSTALLED_APPS = [
    'django.contrib.admin',          # Admin interface
    'django.contrib.auth',           # Authentication system
    'django.contrib.contenttypes',   # Working with content types
    'django.contrib.sessions',       # Session manager
    'django.contrib.messages',       # Messages framework
    'django.contrib.staticfiles',    # Static files
    'app',                           # Our custom application for the task
]

# Declare the middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL config of the project
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Here you can specify paths to template directories
        'APP_DIRS': True,
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

# WSGI application
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings (using SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Additional language and time settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL for static files
STATIC_URL = '/static/'