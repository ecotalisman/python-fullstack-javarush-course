# Handling Multiple URLs and Requests
#
# 1. Create a `views.py` file inside your Django application, for example, `myapp`.
#
# 2. In the `views.py` file, create a `calculate` function for handling requests that:
#
# - For a GET request, returns the string `"Please send two numbers for calculation."`.
#
# - For a POST request, expects two numbers (`a` and `b`) in the request body, adds them, and returns the result as a string, for example, `"Result: 15"`.
#
# 3. In the `urls.py` file, create a `/calculate/` route that connects the URL with the `calculate` function.
#
# 4. When sending a POST request to `http://127.0.0.1:8000/calculate/`:
#
# - Send a POST request with the body `{"a": 5, "b": 10}`
#
# - The result `"Result: 15"` must be returned.
#
# Requirements:
#
# 1. The `calculate` function must be defined in the `views.py` file.
# 2. The `calculate` function must handle GET requests and return the string `"Please send two numbers for calculation."`.
# 3. The `calculate` function must handle POST requests.
# 4. When receiving a POST request, the function must extract two numbers (`a` and `b`) from the request body.
# 5. The function must add the numbers `a` and `b` and return a string in the format `"Result: N"`, where N is the sum result.
# 6. In the application's `urls.py` file, a `/calculate/` route must be created that connects the URL with the `calculate` function from the `views.py` file.
# 7. When sending a GET request to the `/calculate/` route, the text `"Please send two numbers for calculation."` must be returned.
# 8. When sending a POST request to `/calculate/` with the body `{"a": 5, "b": 10}`, the response `"Result: 15"` must be returned.
# 9. Data from the POST request must be extracted correctly, for example, through `request.POST` or `request.body`.
# 10. The URL `/calculate/` must be available on the development server at `http://127.0.0.1:8000/calculate/`.
#
# 🇺🇦 Ukrainian version:
#
# Обробка декількох URL та запитів
#
# 1. Створи файл `views.py` всередині свого Django-додатку (наприклад, `myapp`).
#
# 2. У файлі `views.py` створи функцію `calculate` для обробки запитів, яка:
#
# - При GET-запиті повертає рядок `"Please send two numbers for calculation."`.
#
# - При POST-запиті очікує два числа (`a` та `b`) в тілі запиту, підсумовує їх і повертає результат у вигляді рядка, наприклад `"Result: 15"`.
#
# 3. У файлі `urls.py` створи маршрут `/calculate/`, який зв'язує URL із функцією `calculate`.
#
# 4. При відправці POST-запиту на `http://127.0.0.1:8000/calculate/`:
#
# - Надішли POST-запит із тілом `{"a": 5, "b": 10}`
#
# - Повинен повертатися результат `"Result: 15"`.
#
# Вимоги:
#
# 1. У файлі `views.py` має бути визначена функція `calculate`.
# 2. Функція `calculate` повинна обробляти GET-запити та повертати рядок `"Please send two numbers for calculation."`.
# 3. Функція `calculate` повинна обробляти POST-запити.
# 4. При отриманні POST-запиту функція повинна витягувати два числа (`a` і `b`) з тіла запиту.
# 5. Функція повинна виконувати додавання чисел `a` та `b` і повертати рядок у форматі `"Result: N"`, де N — результат суми.
# 6. У файлі `urls.py` додатку має бути створено маршрут `/calculate/`, який зв'язує URL із функцією `calculate` з файлу `views.py`.
# 7. При відправці GET-запиту на маршрут `/calculate/` повинен повертатися текст `"Please send two numbers for calculation."`.
# 8. При відправці POST-запиту на `/calculate/` з тілом `{"a": 5, "b": 10}` повинен повертатися відповідь `"Result: 15"`.
# 9. Дані з POST-запиту мають бути витягнуті коректно (наприклад, через `request.POST` або `request.body`).
# 10. URL `/calculate/` має бути доступний на сервері розробки за адресою `http://127.0.0.1:8000/calculate/`.

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
