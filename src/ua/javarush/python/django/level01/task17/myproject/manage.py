# Creating a Basic Application
#
# 1. Create a new application in the Django project named "myapp". Register it in the `INSTALLED_APPS` file.
#
# 2. In the `views.py` file of the created "myapp" application, create a function-based view that returns the text "Hello, World!".
#
# 3. Create a `urls.py` file in the "myapp" folder and configure routing so that the root URL ('') points to this view.
#
# 4. Connect the "myapp" application URLs to the main project `urls.py` file. Use the `myapp/` prefix for all application routes.
#
# Requirements:
#
# 1. An application named "myapp" must be created using the `python manage.py startapp myapp` command.
# 2. The "myapp" application must be added to the `INSTALLED_APPS` list in the project settings file `settings.py`.
# 3. In the `views.py` file of the "myapp" application, a function-based view must be defined that returns the text "Hello, World!" as an HTTP response.
# 4. A `urls.py` file must be created in the "myapp" application folder, if it does not exist, to configure routes.
# 5. The `urls.py` file of the "myapp" application must contain a route for the root URL ('') connected to the created view.
# 6. The main project `urls.py` file must be changed to connect all routes of the "myapp" application under the `myapp/` prefix.
#
# 🇺🇦 Ukrainian version:
#
# Створення базового застосунку
#
# 1. Створи новий застосунок у Django проєкті з іменем "myapp". Зареєструй його у файлі `INSTALLED_APPS`.
#
# 2. У файлі `views.py` створеного застосунку "myapp" створи функцію-представлення, яка повертає текст "Hello, World!".
#
# 3. Створи файл `urls.py` у папці "myapp" і налаштуй маршрутизацію так, щоб кореневий URL ('') перенаправляв на це представлення.
#
# 4. Підключи URL застосунку "myapp" до основного файлу `urls.py` проєкту. Використовуй префікс `myapp/` для всіх маршрутів застосунку.
#
# Вимоги:
#
# 1. Повинен бути створений застосунок з іменем "myapp" за допомогою команди `python manage.py startapp myapp`.
# 2. Застосунок "myapp" повинен бути доданий до списку `INSTALLED_APPS` у файлі налаштувань проєкту `settings.py`.
# 3. У файлі `views.py` застосунку "myapp" повинна бути визначена функція-представлення, що повертає текст "Hello, World!" як HTTP-відповідь.
# 4. У папці застосунку "myapp" має бути створений файл `urls.py`, якщо його немає, для налаштування маршрутів.
# 5. Файл `urls.py` застосунку "myapp" повинен містити маршрут для кореневого URL ('') з прив'язкою до створеного представлення.
# 6. Файл `urls.py` основного проєкту повинен бути змінений для підключення всіх маршрутів застосунку "myapp" під префіксом `myapp/`.

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
