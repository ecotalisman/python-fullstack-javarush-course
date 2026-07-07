# Creating a Basic Route
#
# 1. Create a `views.py` file and write a view function that returns the text "Welcome to the home page!".
#
# 2. In the project's `urls.py`, create a route that displays this function at the `/home/` address.
#
# 3. The program must return the text "Welcome to the home page!" if the user accesses the `/home/` address.
#
# Requirements:
#
# 1. A `views.py` file must be created in the project if it does not exist.
# 2. A view function that returns the text "Welcome to the home page!" must be declared in the `views.py` file.
# 3. The view function must be imported into the `urls.py` file for use in routing.
# 4. A route that connects the specified URL `/home/` with the view function must be created in the `urls.py` file.
# 5. When the user accesses the `/home/` address, the server must return the text "Welcome to the home page!".
# 6. The `urls.py` file must be correctly connected to the main `urls.py` of the project for routing to work.
# 7. To create the route in the `urls.py` file, the `path` method from the `django.urls` module must be used.
#
# 🇺🇦 Ukrainian version:
#
# Створення базового маршрута
#
# 1. Створи файл `views.py` і напиши функцію представлення, яка повертає текст "Ласкаво просимо на домашню сторінку!".
#
# 2. У `urls.py` проєкта створи маршрут, який відображає цю функцію за адресою `/home/`.
#
# 3. Програма повинна повертати текст "Ласкаво просимо на домашню сторінку!", якщо користувач звертається за адресою `/home/`.
#
# Вимоги:
#
# 1. У проєкті має бути створений файл `views.py`, якщо він відсутній.
# 2. У файлі `views.py` повинна бути оголошена функція представлення, яка повертає текст "Ласкаво просимо на домашню сторінку!".
# 3. Функцію представлення потрібно імпортувати у файл `urls.py` для використання в маршрутизації.
# 4. У файлі `urls.py` має бути створений маршрут, що зв’язує вказаний URL `/home/` із функцією представлення.
# 5. При зверненні користувача за адресою `/home/` сервер повинен повернути текст "Ласкаво просимо на домашню сторінку!".
# 6. Файл `urls.py` має бути коректно підключений до основного `urls.py` проєкта для роботи маршрутизації.
# 7. Для створення маршрута у файлі `urls.py` потрібно використати метод `path` із модуля `django.urls`.

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
