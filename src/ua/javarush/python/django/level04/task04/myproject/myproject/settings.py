from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for the project (used only in development mode)
SECRET_KEY = 'django-insecure-replace-with-your-real-secret-key'

# Debug mode - enabled for development
DEBUG = True

# List of allowed hosts on which the project can run
ALLOWED_HOSTS = []

# Set the required Django applications, including our 'app' application
INSTALLED_APPS = [
    'django.contrib.admin',          # Administration panel
    'django.contrib.auth',           # Authentication mechanisms
    'django.contrib.contenttypes',   # Content types framework
    'django.contrib.sessions',       # Working with user sessions
    'django.contrib.messages',       # Messages framework
    'django.contrib.staticfiles',    # Working with static files
    'app',                           # Our custom application
]

# Define the middleware for request processing
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Project protection
    'django.contrib.sessions.middleware.SessionMiddleware',    # Working with sessions
    'django.middleware.common.CommonMiddleware',               # Common operations on requests
    'django.middleware.csrf.CsrfViewMiddleware',               # Protection against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # User authentication
    'django.contrib.messages.middleware.MessageMiddleware',    # Passing messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Protection against clickjacking
]

# Root URL config of the project
ROOT_URLCONF = 'myproject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Here you can specify additional template folders
        'APP_DIRS': True,  # Automatic search for templates in application folders
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',       # Adds debug information
                'django.template.context_processors.request',     # Adds the request object to the template context
                'django.contrib.auth.context_processors.auth',    # Passes authentication data
                'django.contrib.messages.context_processors.messages',  # Passes messages to the templates
            ],
        },
    },
]

# Define the WSGI application of the project
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database settings. We use SQLite for ease of development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Driver for SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Database file
    }
}

# Password validation settings for user authentication
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True    # Enables internationalization
USE_TZ = True      # Uses time zone support

# URL for static files (CSS, JS, images)
STATIC_URL = 'static/'

# Default value for the model's primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'