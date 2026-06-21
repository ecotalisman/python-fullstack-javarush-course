# Connecting a PostgreSQL Database
#
# 1. Create a new Django project.
#
# 2. Install the `psycopg2` library for PostgreSQL.
#
# 3. Configure the PostgreSQL connection in the `settings.py` file by specifying the following parameters:
#
# - Database name: `testdb`.
#
# - User: `testuser`.
#
# - Password: `testpassword`.
#
# - Host: `localhost`.
#
# - Port: `5432`.
#
# 4. Run the `python manage.py migrate` command to execute migrations on the specified database.
#
# Requirements:
#
# 1. Create a new Django project using the `django-admin startproject` command.
# 2. Install the `psycopg2` library for working with PostgreSQL using the `pip install psycopg2` command.
# 3. In the `settings.py` file, configure the PostgreSQL connection by specifying all required parameters:
#    - `ENGINE` must be set to `'django.db.backends.postgresql'`.
#    - Specify the database name as `testdb`.
#    - Specify the username as `testuser`.
#    - Specify the password as `testpassword`.
#    - Specify the host as `localhost`.
#    - Specify the port as `5432`.
# 4. Run the `python manage.py migrate` command to apply migrations to the specified database.
# 5. The connection must be configured so that no errors occur when starting the project using the `python manage.py runserver` command.
# 6. The task must use PostgreSQL as the database, not any other available Django database engine.
#
# 🇺🇦 Ukrainian version:
#
# Підключення бази даних PostgreSQL
#
# 1. Створи новий проект Django.
#
# 2. Встанови бібліотеку `psycopg2` для PostgreSQL.
#
# 3. Налаштуй у файлі `settings.py` підключення до PostgreSQL, вказавши параметри:
#
# - Назва бази даних: `testdb`.
#
# - Користувач: `testuser`.
#
# - Пароль: `testpassword`.
#
# - Хост: `localhost`.
#
# - Порт: `5432`.
#
# 4. Запусти команду `python manage.py migrate`, щоб виконати міграції на вказаній базі даних.
#
# Вимоги:
#
# 1. Створи новий проект Django за допомогою команди `django-admin startproject`.
# 2. Встанови бібліотеку `psycopg2` для роботи з PostgreSQL через команду `pip install psycopg2`.
# 3. У файлі `settings.py` потрібно налаштувати підключення до PostgreSQL, вказавши всі необхідні параметри:
#    - `ENGINE` має бути встановлений у значення `'django.db.backends.postgresql'`.
#    - Вказати назву бази даних як `testdb`.
#    - Вказати ім’я користувача як `testuser`.
#    - Вказати пароль як `testpassword`.
#    - Вказати хост як `localhost`.
#    - Вказати порт як `5432`.
# 4. Слід запустити команду `python manage.py migrate` для застосування міграцій до вказаної бази даних.
# 5. Підключення має бути налаштоване так, щоб не виникало помилок під час запуску проекту за допомогою команди `python manage.py runserver`.
# 6. У завданні необхідно використовувати саме PostgreSQL як базу даних, а не інші доступні рушії Django.

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
