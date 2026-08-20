# Handling GET and POST Requests with CBV
#
# Create a Django view as a class that handles both GET and POST requests.
#
# For GET requests, return the string "This is a GET request" as an HTTP response.
#
# For POST requests, return the string "This is a POST request".
#
# Configure routes (URLs) for this view in your project.
#
# Requirements:
#
# 1. The view must be implemented as a class, not as a function.
# 2. The view class must handle GET requests with the appropriate method, for example, `get`, and return the string "This is a GET request".
# 3. The view class must handle POST requests with the appropriate method, for example, `post`, and return the string "This is a POST request".
# 4. Responses to requests must be returned as HttpResponse instances.
# 5. A route must be configured in the project or application that connects a URL with the created Class-Based View.
#
# 🇺🇦 Ukrainian version:
#
# Обробка GET та POST запитів з CBV
#
# Створи Django представлення (view) у вигляді класу, яке опрацьовує як GET, так і POST-запити.
#
# Для GET-запитів поверни рядок "This is a GET request" у вигляді HTTP-відповіді.
#
# А для POST-запитів поверни рядок "This is a POST request".
#
# Налаштуй маршрути (URLs) для цього представлення у своєму проєкті.
#
# Вимоги:
#
# 1. Представлення повинно бути реалізоване у вигляді класу, а не функції.
# 2. Клас представлення повинен обробляти GET-запити відповідним методом, наприклад, `get`, і повертати рядок "This is a GET request".
# 3. Клас представлення повинен обробляти POST-запити відповідним методом, наприклад, `post`, і повертати рядок "This is a POST request".
# 4. Відповіді на запити мають повертатися у вигляді екземплярів HttpResponse.
# 5. У проєкті або застосунку має бути налаштований маршрут, який зв'язує URL зі створеним Class-Based представленням.

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
