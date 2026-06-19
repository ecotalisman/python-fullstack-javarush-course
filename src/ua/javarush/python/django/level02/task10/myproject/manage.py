# Splitting Settings for Development and Production
#
# 1. Split the settings into two files: `settings_development.py` and `settings_production.py`.
#
# 2. In `settings_development.py`:
#
# - Set `DEBUG = True`.
#
# - Add the values "127.0.0.1" and "localhost" to `ALLOWED_HOSTS`.
#
# 3. In `settings_production.py`:
#
# - Set `DEBUG = False`.
#
# - Add only the host "myproductiondomain.com" to `ALLOWED_HOSTS`.
#
# 4. Update the main `settings.py` so that it connects the required settings file depending on the `DJANGO_ENV` environment variable:
#
# ```python
#
# import os
#
# if os.getenv("DJANGO_ENV") == "production":
#
#     from .settings_production import *
#
# else:
#
#     from .settings_development import *
#
# ```
#
# Requirements:
#
# 1. Two separate settings files must be created in the project: `settings_development.py` and `settings_production.py`.
# 2. The `settings_development.py` file must set `DEBUG = True` and add the values "127.0.0.1" and "localhost" to `ALLOWED_HOSTS`.
# 3. The `settings_production.py` file must set `DEBUG = False` and add only the host "myproductiondomain.com" to `ALLOWED_HOSTS`.
# 4. The main `settings.py` file must contain the import of the required settings file, either `settings_development.py` or `settings_production.py`, depending on the value of the `DJANGO_ENV` environment variable.
# 5. The `DJANGO_ENV` environment variable must be used to determine the current environment, development or production.
# 6. The expression `os.getenv("DJANGO_ENV")` must be used in `settings.py` to get the value of the environment variable.
# 7. The project must work correctly both in development mode and in production without the need to change the main `settings.py`.
#
# 🇺🇦 Ukrainian version:
#
# Розділення налаштувань для розробки й продакшена
#
# 1. Розділи налаштування на два файли: `settings_development.py` і `settings_production.py`.
#
# 2. У `settings_development.py`:
#
# - Встанови `DEBUG = True`.
#
# - Додай до `ALLOWED_HOSTS` значення "127.0.0.1" і "localhost".
#
# 3. У `settings_production.py`:
#
# - Встанови `DEBUG = False`.
#
# - Додай до `ALLOWED_HOSTS` тільки хост "myproductiondomain.com".
#
# 4. Онови основний `settings.py`, щоб він підключав потрібний файл налаштувань залежно від змінної середовища `DJANGO_ENV`:
#
# ```python
#
# import os
#
# if os.getenv("DJANGO_ENV") == "production":
#
# from .settings_production import *
#
# else:
#
# from .settings_development import *
#
# ```
#
# Вимоги:
#
# 1. У проєкті повинно бути створено два окремих файли налаштувань: `settings_development.py` та `settings_production.py`.
# 2. Файл `settings_development.py` має встановлювати `DEBUG = True` і додавати в `ALLOWED_HOSTS` значення "127.0.0.1" та "localhost".
# 3. Файл `settings_production.py` має встановлювати `DEBUG = False` і додавати в `ALLOWED_HOSTS` тільки хост "myproductiondomain.com".
# 4. Основний файл `settings.py` повинен містити імпорт потрібного файлу налаштувань (`settings_development.py` або `settings_production.py`) залежно від значення змінної середовища `DJANGO_ENV`.
# 5. Змінна середовища `DJANGO_ENV` повинна використовуватись для визначення поточного оточення (development або production).
# 6. Для отримання значення змінної середовища в `settings.py` повинно використовуватись вираз `os.getenv("DJANGO_ENV")`.
# 7. Проєкт має коректно працювати як у режимі розробки так і в продакшені без необхідності змінювати основний `settings.py`.

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
