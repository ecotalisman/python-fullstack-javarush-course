# Creating a Django Project and Working with Basic Settings
#
# 1. Create a new Django project named "MyProject".
#
# 2. Make changes to the settings.py file.
#
# 3. Add the value "127.0.0.1" to `ALLOWED_HOSTS`.
#
# 4. Set the value of `DEBUG` to False.
#
# 5. Start the dev server.
#
# Requirements:
#
# 1. Create a project named "MyProject" using the `django-admin startproject MyProject` command.
# 2. The user must make changes to the settings.py file located in the project folder.
# 3. In the project settings, the string "127.0.0.1" must be added to the `ALLOWED_HOSTS` field.
# 4. The value of the `DEBUG` parameter must be set to `False`.
# 5. The user must start the built-in Django dev server using the `python manage.py runserver` command.
#
# 🇺🇦 Ukrainian version:
#
# Створення проєкту Django та робота з базовими налаштуваннями
#
# 1. Створи новий проєкт Django з назвою "MyProject".
#
# 2. Внеси зміни у файл settings.py.
#
# 3. Додай у `ALLOWED_HOSTS` значення "127.0.0.1".
#
# 4. Встанови значення `DEBUG` рівним False.
#
# 5. Запусти dev-сервер.
#
# Вимоги:
#
# 1. Створи проєкт з ім'ям "MyProject" за допомогою команди `django-admin startproject MyProject`.
# 2. Користувач має внести зміни у файл налаштувань settings.py, що знаходиться в папці проєкту.
# 3. В налаштуваннях проєкту у полі `ALLOWED_HOSTS` потрібно додати рядок "127.0.0.1".
# 4. Значення параметра `DEBUG` має бути встановлено у `False`.
# 5. Користувач має запустити вбудований dev-сервер Django за допомогою команди `python manage.py runserver`.

"""
Main file for managing the Django project.
It is run with commands such as "python manage.py runserver".
"""

import os
import sys


def main():
    try:
        # Set the environment variable to use the Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyProject.settings")

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
