# Extracting Parameters from a URL
#
# 1. Create a route in your Django application that accepts the `id` parameter in the URL and returns a page with the text: "Your ID: X", where X is the value of the `id` parameter.
#
# 2. Example: when opening the URL `/get-id/15/`, "Your ID: 15" must be displayed.
#
# Requirements:
#
# 1. The route must be configured to accept the `id` parameter in the URL.
# 2. The built-in `path()` method from the django.urls module must be used to configure the route.
# 3. The route must extract the `id` parameter as a dynamic part of the URL.
# 4. A view must be created that accepts the `id` parameter from the URL.
# 5. The value of the `id` parameter must be processed in the view to form the response text.
# 6. The view must return a string with the text "Your ID: X", where X is the value of the `id` parameter.
# 7. A request to the `/get-id/15/` route must return the string "Your ID: 15".
#
# 🇺🇦 Ukrainian version:
#
# Витяг параметрів з URL
#
# 1. Створи маршрут у своєму Django-додатку, який приймає параметр `id` у URL та повертає сторінку з текстом: "Ваш ID: X", де X — це значення параметра `id`.
#
# 2. Приклад: при відкритті URL `/get-id/15/` має відображатися "Ваш ID: 15".
#
# Вимоги:
#
# 1. Маршрут має бути налаштований так, щоб приймати параметр `id` у URL.
# 2. Потрібно використати вбудований метод `path()` з модуля django.urls для налаштування маршруту.
# 3. Маршрут має витягувати параметр `id` як динамічну частину URL.
# 4. Має бути створене представлення (view), яке приймає параметр `id` з URL.
# 5. Значення параметра `id` має бути оброблено у view для формування тексту відповіді.
# 6. Представлення має повертати рядок з текстом "Ваш ID: X", де X — значення параметра `id`.
# 7. Запит до маршруту `/get-id/15/` має повертати рядок "Ваш ID: 15".

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
