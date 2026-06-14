# Creating Another Application
#
# 1. Create a new application in the Django project named "news". Register it in the `INSTALLED_APPS` file.
#
# 2. In the `views.py` file of the created "news" application, create a function-based view that returns the text "Good news, everyone!".
#
# 3. Create a `urls.py` file in the "news" folder and configure routing so that the root URL ('') points to this view.
#
# 4. Connect the "news" application URLs to the main project `urls.py` file. Use the `news/` prefix for all application routes.
#
# Requirements:
#
# 1. A new application named "news" must be created using the `python manage.py startapp news` command.
# 2. The created "news" application must be registered in the `INSTALLED_APPS` list in the `settings.py` file.
# 3. In the `views.py` file of the "news" application, a function-based view must be created that returns the simple text message "Good news, everyone!".
# 4. A `urls.py` file must be created in the "news" application, where a route for the root URL ('') will be configured. This route must point to the created function-based view.
# 5. The routes of the "news" application must be connected to the main project `urls.py` file using the `news/` prefix. This ensures that all application routes are available at URLs beginning with `news/`.
#
# 🇺🇦 Ukrainian version:
#
# Створення ще одного додатку
#
# 1. Створи новий додаток у Django-проекті з ім'ям "news". Зареєструй його у файлі `INSTALLED_APPS`.
#
# 2. У файлі `views.py` створеного додатку "news" створи функцію-представлення, яка повертає текст "Good news, everyone!".
#
# 3. Створи файл `urls.py` у папці "news" і налаштуй маршрутизацію так, щоб кореневий URL ('') спрямовував на це представлення.
#
# 4. Підключи URL-додатку "news" до основного файлу `urls.py` проекту. Використовуй префікс `news/` для всіх маршрутів додатку.
#
# Вимоги:
#
# 1. Потрібно створити новий додаток з ім'ям "news" за допомогою команди `python manage.py startapp news`.
# 2. Створений додаток "news" має бути зареєстрований у списку `INSTALLED_APPS` у файлі `settings.py`.
# 3. У файлі `views.py` додатку "news" повинна бути створена функція-представлення, яка повертає просте текстове повідомлення "Good news, everyone!".
# 4. У додатку "news" має бути створений файл `urls.py`, у якому буде налаштовано маршрут для кореневого URL (''). Цей маршрут має вказувати на створену функцію-представлення.
# 5. Маршрути додатку "news" повинні бути підключені до основного файлу `urls.py` проекту з використанням префікса `news/`. Це гарантує, що всі маршрути додатку будуть доступні за URL, що починається з `news/`.

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
