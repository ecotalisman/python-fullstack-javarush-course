"""
Налаштування проєкту Django.

Зауваження: цей файл містить мінімальні налаштування,
не призначені для використання у продакшені.
"""
from pathlib import Path

# Визначаємо базову директорію проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ (не використовувати у продакшені)
SECRET_KEY = 'django-insecure-zamenit-na-nastojashchii-kliuch'

# Режим налагодження (DEBUG=True для розробки)
DEBUG = True

ALLOWED_HOSTS = []

# Встановлюємо застосунки, які використовуються у проєкті
INSTALLED_APPS = [
    'django.contrib.admin',         # Адмін-панель Django
    'django.contrib.auth',          # Система автентифікації
    'django.contrib.contenttypes',  # Система типів контенту
    'django.contrib.sessions',      # Механізм сесій
    'django.contrib.messages',      # Система повідомлень
    'django.contrib.staticfiles',   # Робота зі статичними файлами
    'app',                          # Наш користувацький застосунок
]

# Middleware для обробки запитів
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Захист CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Коренева конфігурація URL
ROOT_URLCONF = 'myproject.urls'

# Налаштування шаблонів Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Тут можна вказати директорії для шаблонів
        'APP_DIRS': True,  # Пошук шаблонів у застосунках
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Об'єкт запиту у контексті
                'django.contrib.auth.context_processors.auth',  # Інформація про користувача
                'django.contrib.messages.context_processors.messages',  # Передача повідомлень
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Конфігурація бази даних (використовуємо SQLite для простоти)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідатори паролів
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

# Налаштування локалізації
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# URL для статичних файлів
STATIC_URL = 'static/'

# Автоматичне визначення поля для первинних ключів
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'