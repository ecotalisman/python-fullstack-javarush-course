# Creating the First Migration
#
# 1. Create a new application named "library".
#
# 2. In the `models.py` file of this application, create a model named `Book` that will contain the following fields:
#
# - `title` of type `CharField` with a maximum length of 200 characters.
#
# - `author` of type `CharField` with a maximum length of 100 characters.
#
# - `published_date` of type `DateField`.
#
# 3. Use the `makemigrations` command to create a migration for this model.
#
# Requirements:
#
# 1. Create a new Django application named "library".
# 2. In the `models.py` file of the "library" application, the `Book` model must be created.
# 3. The `Book` model must contain a `title` field of type `CharField` with a maximum length of 200 characters.
# 4. The `Book` model must contain an `author` field of type `CharField` with a maximum length of 100 characters.
# 5. The `Book` model must contain a `published_date` field of type `DateField`.
# 6. The `python manage.py makemigrations` command must be used to create a migration based on changes in the `models.py` file.
# 7. The "library" application must be registered in the project settings so that migrations and the model are processed correctly.
#
# 🇺🇦 Ukrainian version:
#
# Створення першої міграції
#
# 1. Створи новий додаток із назвою "library".
#
# 2. У файлі `models.py` цього додатка створи модель з іменем `Book`, яка буде містити такі поля:
#
# - `title` типу `CharField` з максимальною довжиною 200 символів.
#
# - `author` типу `CharField` з максимальною довжиною 100 символів.
#
# - `published_date` типу `DateField`.
#
# 3. За допомогою команди `makemigrations` створи міграцію для цієї моделі.
#
# Вимоги:
#
# 1. Створи новий Django-додаток із назвою "library".
# 2. У файлі `models.py` додатка "library" потрібно створити модель `Book`.
# 3. Модель `Book` повинна містити поле `title` типу `CharField` з максимальною довжиною 200 символів.
# 4. Модель `Book` повинна містити поле `author` типу `CharField` з максимальною довжиною 100 символів.
# 5. Модель `Book` повинна містити поле `published_date` типу `DateField`.
# 6. Потрібно використати команду `python manage.py makemigrations` для створення міграції на основі змін у файлі `models.py`.
# 7. Додаток "library" має бути зареєстрований у налаштуваннях проєкту, щоб міграції та модель були коректно опрацьовані.

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
