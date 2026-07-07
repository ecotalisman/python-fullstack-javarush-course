# Creating a Route with path()
#
# Create a new route using the `path()` function that handles the `/welcome/` URL. To do this, create a view function named `welcome_view` in the `views.py` file that returns the text "Welcome!". Configure the route so that when `/welcome/` is accessed, this function is called.
#
# Requirements:
#
# 1. A route must be created using the `path()` function from the `django.urls` module.
# 2. In the `views.py` file, a `welcome_view` function must be created that returns the text "Welcome!".
# 3. The route must handle the `/welcome/` URL.
# 4. Routing must be configured so that calling the `/welcome/` URL runs the `welcome_view` function.
# 5. The `welcome_view` function must return a text response "Welcome!" using HttpResponse.
# 6. The created route must be added to the routes file, usually `urls.py`, of the corresponding Django application or project.
#
# 🇺🇦 Ukrainian version:
#
# Створення маршруту з path()
#
# Створи новий маршрут з використанням функції `path()`, який обробляє URL `/welcome/`. Для цього створи функцію-представлення `welcome_view` у файлі `views.py`, яка повертає текст "Ласкаво просимо!". Налаштуй маршрут так, щоб при переході на `/welcome/` викликалась ця функція.
#
# Вимоги:
#
# 1. Потрібно створити маршрут з використанням функції `path()` з модуля `django.urls`.
# 2. У файлі `views.py` повинна бути створена функція `welcome_view`, яка повертає текст "Ласкаво просимо!".
# 3. Маршрут має обробляти URL `/welcome/`.
# 4. Роутінг має бути налаштовано так, щоб виклик URL `/welcome/` запускав функцію `welcome_view`.
# 5. Функція `welcome_view` має повертати відповідь у вигляді тексту "Ласкаво просимо!" з використанням HttpResponse.
# 6. Створений маршрут потрібно додати у файл маршрутів, зазвичай `urls.py`, відповідного застосунку або проекту Django.

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
