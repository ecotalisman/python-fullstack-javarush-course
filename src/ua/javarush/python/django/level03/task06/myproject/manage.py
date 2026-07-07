# Connecting Application Routes
#
# 1. Create a new application in the Django project named `app_name`.
#
# 2. In the application's `urls.py` file, add a route that displays the text "This is an application page!" at the `/app/page/` address.
#
# 3. Connect the routes of this application in the main `urls.py` file of the project using the `include` function.
#
# 4. The program must return the text "This is an application page!" when accessing the `/app/page/` address.
#
# Requirements:
#
# 1. Create a new application in the Django project named `app_name` using the `startapp` command.
# 2. The application's `urls.py` file must contain a route that connects the `/app/page/` address with a view that returns the text "This is an application page!".
# 3. The view that returns the text "This is an application page!" must be declared in the application's `views.py` file.
# 4. The application's routes must be connected to the project's main `urls.py` file using the `include` function.
# 5. After all settings are completed, when accessing the `/app/page/` address, the server must return the text "This is an application page!".
# 6. The `include` function must be used in the project's main `urls.py` file to connect the application's routes.
#
# 🇺🇦 Ukrainian version:
#
# Підключення маршрутів додатку
#
# 1. Створи новий додаток у Django-проєкті з іменем `app_name`.
#
# 2. У файлі `urls.py` додатку додай маршрут, який відображає текст "Це сторінка додатку!" за адресою `/app/page/`.
#
# 3. Підключи маршрути цього додатку у головному `urls.py` проєкту, використовуючи функцію `include`.
#
# 4. Програма повинна повертати текст "Це сторінка додатку!" при зверненні за адресою `/app/page/`.
#
# Вимоги:
#
# 1. Створи новий додаток у проєкті Django з іменем `app_name` за допомогою команди `startapp`.
# 2. Файл `urls.py` додатку має містити маршрут, який пов'язує адресу `/app/page/` із view, що повертає текст "Це сторінка додатку!".
# 3. View, яке повертає текст "Це сторінка додатку!", має бути оголошене у файлі `views.py` додатку.
# 4. Маршрути додатку мають бути підключені до головного файлу `urls.py` проєкту з використанням функції `include`.
# 5. Після виконання всіх налаштувань, при зверненні за адресою `/app/page/` сервер має повертати текст "Це сторінка додатку!".
# 6. У головному файлі `urls.py` проєкту повинна бути використана функція `include` для підключення маршрутів додатку.

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
