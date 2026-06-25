# Studying the DEBUG Parameter
#
# 1. Create a new Django project named `debug_settings_project`.
#
# 2. Modify the `settings.py` file of your project.
#
# 3. Set the value of the `DEBUG` parameter to `True`.
#
# 4. Create a simple view function that raises a "division by zero" exception.
#
# 5. Create a URL route that will be connected to this view.
#
# Requirements:
#
# 1. Create a new Django project named `debug_settings_project`.
# 2. In the project's `settings.py` file, the `DEBUG` parameter must be set to `True`.
# 3. A view function that raises a "division by zero" exception must be created.
# 4. A URL route connected to the specified view function must be created.
# 5. When the "division by zero" exception occurs, the standard Django error message in DEBUG mode must be displayed.
#
# 🇺🇦 Ukrainian version:
#
# Вивчення параметра DEBUG
#
# 1. Створи новий проєкт Django з іменем `debug_settings_project`.
#
# 2. Зміни файл `settings.py` твого проєкту.
#
# 3. Встанови значення параметра `DEBUG` у `True`.
#
# 4. Створи просту функцію-представлення (view), яка викликає виняток "ділення на нуль".
#
# 5. Створи маршрут URL, який буде пов'язаний із цим представленням.
#
# Вимоги:
#
# 1. Створи новий проєкт Django з іменем `debug_settings_project`.
# 2. У файлі `settings.py` проєкту параметр `DEBUG` має бути встановлений у значення `True`.
# 3. Потрібно створити функцію-представлення (view), яка викликає виняток "ділення на нуль".
# 4. Має бути створений маршрут URL, який буде пов'язаний із зазначеною функцією-представленням.
# 5. При виникненні винятку "ділення на нуль" має відображатися стандартне повідомлення про помилку Django у режимі DEBUG.

"""
Main file for managing the Django project.
It is run with commands such as "python manage.py runserver".
"""

import os
import sys


def main():
    try:
        # Set the environment variable to use the Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debug_settings_project.settings")

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
