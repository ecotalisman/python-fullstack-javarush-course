# Connecting an SQLite Database
#
# 1. Create a new Django project.
#
# 2. Configure the `SQLite` database using the `settings.py` file.
#
# 3. Start the dev server using the `python manage.py runserver` command.
#
# Requirements:
#
# 1. A new project must be created using the `django-admin startproject` command.
# 2. In the `settings.py` file, the `DATABASES` section must configure the use of the SQLite database, which is used by default.
# 3. The standard SQLite engine provided by Django must be specified for the database configuration using `ENGINE: django.db.backends.sqlite3`.
# 4. The `NAME` field in the `DATABASES` section must contain the path to the SQLite database file, for example `BASE_DIR / "db.sqlite3"`.
# 5. After successfully configuring the project and the database, the development server must be started using the `python manage.py runserver` command.
#
# 🇺🇦 Ukrainian version:
#
# Підключення бази даних SQLite
#
# 1. Створи новий проєкт Django.
#
# 2. Налаштуй базу даних `SQLite`, використовуючи файл `settings.py`.
#
# 3. Запусти dev-сервер за допомогою команди `python manage.py runserver`.
#
# Вимоги:
#
# 1. Потрібно створити новий проєкт за допомогою команди `django-admin startproject`.
# 2. У файлі `settings.py` в секції `DATABASES` потрібно налаштувати використання бази даних SQLite за замовчуванням.
# 3. Для налаштування бази даних повинен бути зазначений стандартний рушій SQLite, який надає Django, з використанням `ENGINE: django.db.backends.sqlite3`.
# 4. Поле `NAME` у розділі `DATABASES` повинно містити шлях до файлу бази даних SQLite, наприклад `BASE_DIR / "db.sqlite3"`.
# 5. Після успішного налаштування проєкту та бази даних потрібно запустити сервер розробки за допомогою команди `python manage.py runserver`.

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
