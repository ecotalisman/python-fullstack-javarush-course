# Simple CBV for Handling a GET Request
#
# Create a Class-Based View (CBV) that returns the text "Welcome to Class-Based Views!" when handling a GET request.
#
# Register this view in the URLConf of your Django project.
#
# Requirements:
#
# 1. A class-based view (CBV) must be created in the project, inheriting from the base View class provided by Django.
# 2. The class-based view must override the `get` method to handle GET requests.
# 3. The `get` method must return an `HttpResponse` object with the text `"Welcome to Class-Based Views!"`.
# 4. The view must be registered in the project's URLConf file.
#
# 🇺🇦 Ukrainian version:
#
# Простий CBV для обробки GET-запиту
#
# Створи Class-Based View (CBV), який повертає текст "Welcome to Class-Based Views!" при обробці GET-запиту.
#
# Зареєструй це представлення в URLConf твого Django-проєкту.
#
# Вимоги:
#
# 1. У проєкті має бути створений клас-представлення (CBV), який наслідує базовий клас View, що надається Django.
# 2. Клас-представлення повинен перевизначити метод `get` для обробки GET-запитів.
# 3. Метод `get` має повертати об'єкт `HttpResponse` з текстом `"Welcome to Class-Based Views!"`.
# 4. Представлення має бути зареєстровано у файлі URLConf проєкту.

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
