# Configuring the CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE Settings
#
# 1. In the Django project, open the `settings.py` file.
#
# 2. Set the value of `CSRF_COOKIE_SECURE` to `True`.
#
# 3. Set the value of `SESSION_COOKIE_SECURE` to `True`.
#
# 4. Configure your dev server to support HTTPS.
#
# Hint: If you are working in an IDE, install the `django-sslserver` library and run the server with SSL support.
#
# Requirements:
#
# 1. In the settings.py file, the CSRF_COOKIE_SECURE setting must be set to True.
# 2. In the settings.py file, the SESSION_COOKIE_SECURE setting must be set to True.
# 3. Configure the development server to work over HTTPS.
# 4. Install the django-sslserver library to run the dev server with SSL support.
# 5. The CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE settings must be added to the settings.py file.
#
# 🇺🇦 Ukrainian version:
#
# Налаштування параметрів CSRF_COOKIE_SECURE і SESSION_COOKIE_SECURE
#
# 1. У проекті Django відкрий файл `settings.py`.
#
# 2. Встанови значення `CSRF_COOKIE_SECURE` в `True`.
#
# 3. Встанови значення `SESSION_COOKIE_SECURE` в `True`.
#
# 4. Налаштуй свій dev-сервер для підтримки HTTPS.
#
# Підказка: Якщо ти працюєш в IDE, встанови бібліотеку `django-sslserver` і запусти сервер із підтримкою SSL.
#
# Вимоги:
#
# 1. У файлі settings.py параметр CSRF_COOKIE_SECURE має бути встановлений у True.
# 2. У файлі settings.py параметр SESSION_COOKIE_SECURE має бути встановлений у True.
# 3. Налаштуй сервер розробки для роботи через HTTPS.
# 4. Встанови бібліотеку django-sslserver для запуску dev-серверу з підтримкою SSL.
# 5. Налаштування CSRF_COOKIE_SECURE і SESSION_COOKIE_SECURE мають бути додані у файл settings.py.

"""
Main file for managing the Django project.
It is run with commands such as "python manage.py runserver".
"""

import os
import sys


def main():
    try:
        # Set the environment variable to use the Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

        # Import the utility for executing project management commands
        from django.core.management import execute_from_command_line

        # Execute the command passed in the command-line arguments
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        # Display an error message if Django is not installed
        print("Error: Django is not installed or not found!")
        print("Run 'pip install django' or 'pip install -r requirements.txt'.")

        sys.exit(1)  # Exit with an error code


if __name__ == "__main__":
    main()
