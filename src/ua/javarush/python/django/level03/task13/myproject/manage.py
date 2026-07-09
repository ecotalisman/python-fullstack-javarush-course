# Creating a Dynamic URL Using Integers
#
# 1. Create a route in the `urls.py` file that will handle a URL of the form `/article/<int:article_id>/`.
#
# 2. The `article_detail(request, article_id)` view function must return a string in the following format: "You selected the article with ID: <article_id>".
#
# 3. Example: when navigating to `/article/5/`, "You selected the article with ID: 5" must be displayed.
#
# Requirements:
#
# 1. The `urls.py` file must contain a route that accepts the dynamic integer parameter `<int:article_id>`.
# 2. The dynamic route must be configured using the `path()` function from the `django.urls` module.
# 3. The `article_detail` view function must be imported in the `urls.py` file.
# 4. The dynamic parameter `<int:article_id>` specified in the route must be passed as an argument to the `article_detail` view function.
# 5. The `article_detail` view function must implement code that accepts the `article_id` parameter and forms a response.
# 6. The `article_detail` view function must return a string in the following format: "You selected the article with ID: <article_id>", where `<article_id>` is the passed value.
# 7. When navigating to the URL `/article/5/` in the browser, the message "You selected the article with ID: 5" must be displayed.
#
# 🇺🇦 Ukrainian version:
#
# Створення динамічного URL з використанням цілих чисел
#
# 1. Створи маршрут у файлі `urls.py`, який буде обробляти URL виду `/article/<int:article_id>/`.
#
# 2. У view-функції `article_detail(request, article_id)` має повертатися рядок такого вигляду: "Ви обрали статтю з ID: <article_id>".
#
# 3. Приклад: при переході на `/article/5/` повинно відобразитись "Ви обрали статтю з ID: 5".
#
# Вимоги:
#
# 1. У файлі `urls.py` повинен бути прописаний маршрут, який приймає динамічний цілий параметр `<int:article_id>`.
# 2. Динамічний маршрут має бути налаштований за допомогою функції `path()` з модуля `django.urls`.
# 3. У файлі `urls.py` треба імпортувати функцію view `article_detail`.
# 4. Динамічний параметр `<int:article_id>`, вказаний у маршруті, має передаватися як аргумент у функцію view `article_detail`.
# 5. У функції view `article_detail` має бути реалізовано код, який приймає параметр `article_id` і формує відповідь.
# 6. Функція view `article_detail` повинна повертати рядок такого вигляду: "Ви обрали статтю з ID: <article_id>", де `<article_id>` — передане значення.
# 7. При переході на URL `/article/5/` у браузері має відображатися повідомлення "Ви обрали статтю з ID: 5".

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
