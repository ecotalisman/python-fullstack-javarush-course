# Creating a Simple Class-Based View (CBV)
#
# Create a view class `HelloWorldView` that returns the string "Hello from CBV!" in response to a GET request.
#
# Connect this view to the `/hello/` route in the `urls.py` file.
#
# Example: When navigating to `http://localhost:8000/hello/`, "Hello from CBV!" must be returned.
#
# Requirements:
#
# 1. The `HelloWorldView` class must inherit from one of Django's built-in view classes, such as `View`.
# 2. The `HelloWorldView` class must override the `get()` method to handle only GET requests.
# 3. The `get()` method must return an HTTP response with the text "Hello from CBV!".
# 4. In the `urls.py` file, the `/hello/` route must be created and connected to the `HelloWorldView` view.
# 5. To connect the `HelloWorldView` class to the route, the `as_view()` method must be used.
# 6. When accessing `http://localhost:8000/hello/`, the text "Hello from CBV!" must be displayed correctly.
#
# 🇺🇦 Ukrainian version:
#
# Створення простого Class-Based View (CBV)
#
# Створи клас представлення `HelloWorldView`, який повертає рядок "Hello from CBV!" у відповідь на GET-запит.
#
# Пов’яжи це представлення з маршрутом `/hello/` у файлі `urls.py`.
#
# Приклад: При переході за адресою `http://localhost:8000/hello/`, має повертатися "Hello from CBV!".
#
# Вимоги:
#
# 1. Клас `HelloWorldView` має бути нащадком одного з вбудованих класів представлень Django, таких як `View`.
# 2. Клас `HelloWorldView` повинен перевизначити метод `get()` для обробки лише GET-запитів.
# 3. Метод `get()` має повертати HTTP-відповідь з текстом "Hello from CBV!".
# 4. У файлі `urls.py` потрібно створити маршрут `/hello/` і пов’язати його з представленням `HelloWorldView`.
# 5. Щоб підключити клас `HelloWorldView` до маршруту, потрібно використовувати метод `as_view()`.
# 6. При доступі до `http://localhost:8000/hello/` має коректно відображатися текст "Hello from CBV!".

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
