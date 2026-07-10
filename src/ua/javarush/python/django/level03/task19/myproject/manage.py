# Creating a Basic Route
#
# 1. Create a new application named `myapp` in an existing Django project.
#
# 2. Register this application in the `settings.py` file in the `INSTALLED_APPS` section.
#
# 3. In the `views.py` file of the `myapp` application, create a `home_view` view that returns the string "Welcome to the main page!".
#
# 4. Configure routes in the `urls.py` file of the application by connecting the root path, empty `''`, with `home_view`.
#
# 5. Include the application routes in the main `urls.py` file of the project.
#
# Requirements:
#
# 1. A new application named `myapp` must be created inside the existing Django project.
# 2. The `myapp` application must be added to the `INSTALLED_APPS` list in the main project's `settings.py` file.
# 3. In the `views.py` file of the `myapp` application, there must be a `home_view` view that returns the string "Welcome to the main page!".
# 4. In the `urls.py` file of the `myapp` application, routes must be configured by connecting the root path, empty path `''`, with the `home_view` view.
# 5. The main project's `urls.py` file must include the routes of the `myapp` application using the `include()` function.
# 6. Navigating to the root route, for example, `http://127.0.0.1:8000/`, must display the string "Welcome to the main page!".
#
# 🇺🇦 Ukrainian version:
#
# Створення базового маршруту
#
# 1. Створи новий додаток у вже існуючому проекті Django з назвою `myapp`.
#
# 2. Зареєструй цей додаток у файлі `settings.py` у розділі `INSTALLED_APPS`.
#
# 3. Створи у файлі `views.py` додатка `myapp` представлення `home_view`, яке повертає рядок "Ласкаво просимо на головну сторінку!".
#
# 4. Налаштуй маршрути у `urls.py` додатка, зв’язавши кореневий шлях (порожній `''`) з `home_view`.
#
# 5. Включи маршрути додатка у головний файл `urls.py` проекту.
#
# Вимоги:
#
# 1. Потрібно створити новий додаток з іменем `myapp` всередині існуючого проекту Django.
# 2. Додаток `myapp` має бути доданий до списку `INSTALLED_APPS` у файлі `settings.py` основного проекту.
# 3. У файлі `views.py` додатка `myapp` має бути представлення `home_view`, яке повертає рядок "Ласкаво просимо на головну сторінку!".
# 4. У файлі `urls.py` додатка `myapp` потрібно налаштувати маршрути, зв’язавши кореневий шлях, порожній шлях `''`, з представленням `home_view`.
# 5. Файл `urls.py` основного проекту має включати маршрути додатка `myapp` з використанням функції `include()`.
# 6. Перехід на кореневий маршрут, наприклад, `http://127.0.0.1:8000/`, має відображати рядок "Ласкаво просимо на головну сторінку!".

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
