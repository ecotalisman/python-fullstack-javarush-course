# Simple URL Binding with a View
#
# 1. Create a `views.py` file inside your Django application, for example, `myapp`.
#
# 2. Write a simple view function named `welcome_view` that returns the response `"Welcome to Django!"`.
#
# 3. In the `urls.py` file of the same application, create a `/welcome/` route that connects the specified URL with the `welcome_view` view function.
#
# 4. When navigating to the URL `http://localhost:8000/welcome/` in the browser, the string `"Welcome to Django!"` must be displayed.
#
# Requirements:
#
# 1. A `views.py` file must be created in the specified Django application, for example, `myapp`, if it does not already exist.
# 2. A view function named `welcome_view` must be implemented in the `views.py` file. It must return the text response `"Welcome to Django!"`.
# 3. The `welcome_view` function must return an `HttpResponse` object with the specified response text.
# 4. A `urls.py` file must be created in the application if it does not exist.
# 5. In the `urls.py` file, the `/welcome/` route must be defined, connecting the URL with the `welcome_view` view function.
# 6. To bind the `/welcome/` route with the `welcome_view` function, the `path()` function should be used to define the route.
# 7. The application routes must be registered in the main `urls.py` file of the project using `include()`.
# 8. After starting the local Django server, when navigating to `http://localhost:8000/welcome/` in the browser, the string `"Welcome to Django!"` must be displayed.
#
# 🇺🇦 Ukrainian version:
#
# Просте зв'язування URL з представленням
#
# 1. Створи файл `views.py` всередині свого Django-додатку (наприклад, `myapp`).
#
# 2. Напиши просту функцію представлення `welcome_view`, яка повертає відповідь `"Welcome to Django!"`.
#
# 3. У файлі `urls.py` (цього ж додатку) створи маршрут `/welcome/`, який зв'язує вказаний URL з функцією представлення `welcome_view`.
#
# 4. При переході за URL `http://localhost:8000/welcome/` у браузері має відображатися рядок `"Welcome to Django!"`.
#
# Вимоги:
#
# 1. Необхідно створити файл `views.py` у вказаному Django-додатку (наприклад, `myapp`), якщо його ще не існує.
# 2. Функція представлення з ім'ям `welcome_view` має бути реалізована у файлі `views.py`. Вона повинна повертати текстову відповідь `"Welcome to Django!"`.
# 3. Функція `welcome_view` повинна повертати об'єкт `HttpResponse` з зазначеним текстом відповіді.
# 4. У додатку має бути створений файл `urls.py`, якщо він відсутній.
# 5. У файлі `urls.py` потрібно прописати маршрут `/welcome/`, який зв'язує URL з функцією представлення `welcome_view`.
# 6. Для зв'язування маршруту `/welcome/` з функцією `welcome_view` слід використати функцію `path()` для визначення маршруту.
# 7. Маршрути додатку мають бути зареєстровані в основному файлі `urls.py` проекту (підключення через `include()`).
# 8. Після запуску локального сервера Django при переході за адресою `http://localhost:8000/welcome/` у браузері має відображатися рядок `"Welcome to Django!"`.

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
