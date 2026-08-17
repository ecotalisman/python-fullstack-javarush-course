# Dynamic Routes
#
# 1. Create a new Django project named `dynamic_project` and add an application named `greetings` to it.
#
# 2. Register `greetings` in `INSTALLED_APPS` in the `settings.py` file.
#
# 3. In the `views.py` file of the `greetings` application, create a `hello_view` view that accepts the `name` parameter and returns the string: "Hello, {name}", where `{name}` is the passed parameter with the first letter capitalized.
#
# 4. In the `urls.py` file of the `greetings` application, configure the `/hello/<str:name>/` route, which passes the `name` parameter to `hello_view`.
#
# 5. In the main `urls.py` file of the project, connect the routes of the `greetings` application.
#
# Requirements:
#
# 1. A new Django project named `dynamic_project` must be created.
# 2. An application named `greetings` must be created and added to the project.
# 3. The `greetings` application must be registered in the `INSTALLED_APPS` list in the `settings.py` file.
# 4. In the `views.py` file of the `greetings` application, a `hello_view` view must be created that accepts the `name` parameter.
# 5. The `hello_view` view must return the string "Hello, {name}", where `{name}` is the `name` parameter with the first letter capitalized.
# 6. In the `urls.py` file of the `greetings` application, the `/hello/<str:name>/` route must be created, passing the `name` parameter to the `hello_view` view.
# 7. The routes of the `greetings` application must be connected in the main `urls.py` file of the `dynamic_project` project.
#
# 🇺🇦 Ukrainian version:
#
# Динамічні маршрути
#
# 1. Створи новий Django-проєкт з іменем dynamic_project і додай у нього додаток greetings.
#
# 2. Зареєструй greetings у INSTALLED_APPS у файлі settings.py.
#
# 3. У файлі views.py додатку greetings створи view hello_view, яке приймає параметр name і повертає рядок: "Привіт, {name}", де {name} — переданий параметр з першої великої літери.
#
# 4. У файлі urls.py додатку greetings налаштуй маршрут /hello/<str:name>/, який передає параметр name у hello_view.
#
# 5. В основному urls.py проєкту підключи маршрути додатку greetings.
#
# Вимоги:
#
# 1. Потрібно створити новий Django-проєкт з іменем `dynamic_project`.
# 2. Створити додаток з іменем `greetings` і додати його у проєкт.
# 3. Додаток `greetings` має бути зареєстрований у списку `INSTALLED_APPS` файлу `settings.py`.
# 4. У файлі `views.py` додатку `greetings` має бути створене view `hello_view`, яке приймає параметр `name`.
# 5. View `hello_view` має повертати рядок "Привіт, {name}", де `{name}` — параметр `name` з першої великої літери.
# 6. У файлі `urls.py` додатку `greetings` потрібно створити маршрут `/hello/<str:name>/`, який передає параметр `name` у view `hello_view`.
# 7. Маршрути додатку `greetings` мають бути підключені в основному файлі `urls.py` проєкту `dynamic_project`.

"""
Main file for managing the Django project.
It is run with commands such as "python manage.py runserver".
"""

import os
import sys


def main():
    try:
        # Set the environment variable to use the Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dynamic_project.settings")

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
