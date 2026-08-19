# Handling GET and POST in a CBV
#
# Create a Class-Based View that handles two types of requests:
#
# - For a GET request, it returns the text "This is a GET request".
#
# - For a POST request, it returns the text "This is a POST request".
#
# Register the view in URLConf — it must return the correct response for each request type.
#
# Requirements:
#
# 1. The view must be implemented using Class-Based Views (CBV).
# 2. The view must correctly handle a GET request and return the text "This is a GET request".
# 3. The view must correctly handle a POST request and return the text "This is a POST request".
# 4. To implement the view, one of the base CBV classes must be used, for example, View.
# 5. The HTTP request methods, get() and post(), must be overridden in the class to handle the corresponding requests.
# 6. The view must be registered in the urls.py file so that it becomes available at the defined path.
#
# 🇺🇦 Ukrainian version:
#
# Обробка GET і POST у CBV
#
# Створи Class-Based View, яке обробляє два типи запитів:
#
# - Для GET-запиту повертає текст "This is a GET request".
#
# - Для POST-запиту повертає текст "This is a POST request".
#
# Зареєструй view у URLConf — воно має повертати правильну відповідь для кожного типу запиту.
#
# Вимоги:
#
# 1. View має бути реалізовано з використанням Class-Based Views (CBV).
# 2. View має коректно обробляти GET-запит і повертати текст "This is a GET request".
# 3. View має коректно обробляти POST-запит і повертати текст "This is a POST request".
# 4. Для реалізації view потрібно використати один із базових класів CBV, наприклад, View.
# 5. Методи HTTP-запитів (get() і post()) мають бути перевизначені в класі для обробки відповідних запитів.
# 6. View має бути зареєстроване у файлі urls.py, щоб воно стало доступним за визначеним шляхом.

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
