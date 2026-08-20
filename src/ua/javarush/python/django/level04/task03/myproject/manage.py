# Creating a Class-Based View (CBV)
#
# Create a Django view as a class using `django.views.View`.
#
# Implement the `get` method, which handles a GET request and returns the string "Hello from CBV!" as an HTTP response.
#
# Configure a route (URL) for this view in your project.
#
# Requirements:
#
# 1. The view must be implemented as a class that inherits from `django.views.View`.
# 2. The class-based view must contain a `get` method that handles GET requests.
# 3. The `get` method must return the string "Hello from CBV!" as an HTTP response.
# 4. To return the string "Hello from CBV!", an `HttpResponse` object must be used.
# 5. A route for this view must be configured in the `urls.py` file.
# 6. The route must use the `as_view()` function to bind the class-based view.
# 7. After configuring the routes, the view that returns "Hello from CBV!" must be available at the specified URL.
#
# 🇺🇦 Ukrainian version:
#
# Створення Class-Based View (CBV)
#
# Створи Django-представлення (view) у вигляді класу, використовуючи `django.views.View`.
#
# Реалізуй метод `get`, який обробляє GET-запит і повертає рядок "Hello from CBV!" як HTTP-відповідь.
#
# Налаштуй маршрут (URL) для цього представлення у своєму проєкті.
#
# Вимоги:
#
# 1. Представлення має бути реалізоване як клас, що наслідується від `django.views.View`.
# 2. Клас-представлення повинен містити метод `get`, який обробляє GET-запити.
# 3. Метод `get` має повертати рядок "Hello from CBV!" як HTTP-відповідь.
# 4. Для повернення рядка "Hello from CBV!" потрібно використовувати об'єкт `HttpResponse`.
# 5. У файлі `urls.py` має бути налаштований маршрут для цього представлення.
# 6. Маршрут повинен використовувати функцію `as_view()` для зв'язування класу-представлення.
# 7. Після налаштування маршрутів, за вказаним URL має бути доступне представлення, що повертає "Hello from CBV!".

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
