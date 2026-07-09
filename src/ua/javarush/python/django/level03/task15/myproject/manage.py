# JSON Response
#
# 1. Create a Django view that returns a JSON response with the data `{"status": "success", "message": "Hello, JSON!"}`.
#
# 2. Use the `JsonResponse` class from `django.http`.
#
# Requirements:
#
# 1. The view must use the `JsonResponse` class from the `django.http` module to form the JSON response.
# 2. The view must return a JSON response with the fixed data `{"status": "success", "message": "Hello, JSON!"}`.
# 3. The task requires creating a function-based view.
# 4. The code must explicitly import `JsonResponse` from `django.http`.
#
# 🇺🇦 Ukrainian version:
#
# JSON-відповідь
#
# 1. Створи Django-представлення, яке повертає JSON-відповідь з даними `{"status": "success", "message": "Hello, JSON!"}`.
#
# 2. Використовуй клас `JsonResponse` з `django.http`.
#
# Вимоги:
#
# 1. Представлення має використовувати клас `JsonResponse` з модуля `django.http` для формування JSON-відповіді.
# 2. Представлення повинно повертати JSON-відповідь із фіксованими даними `{"status": "success", "message": "Hello, JSON!"}`.
# 3. Завдання передбачає створення функції-представлення (function-based view).
# 4. Код має явно імпортувати `JsonResponse` з `django.http`.

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
