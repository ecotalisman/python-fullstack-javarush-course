# Forming an HTML Response
#
# 1. Create a view function named `hello_html` that returns an HTML page with the heading "Welcome to Django!" and the text below the heading "This is an HTML response.".
#
# 2. Register this view in the `urls.py` file with the path `html/`.
#
# 3. When navigating to the URL `http://localhost:8000/html/`, a message in HTML format must be displayed.
#
# Requirements:
#
# 1. A view function named `hello_html` must be created in the project.
# 2. The `hello_html` function must return an HTTP response in HTML format with the heading "Welcome to Django!" and the text "This is an HTML response.".
# 3. `HttpResponse` from `django.http` must be imported in the view.
# 4. The view function must be registered in the `urls.py` file with the path `html/`.
# 5. The `path()` function must be used to register the route in `urls.py`.
# 6. When navigating to `http://localhost:8000/html/`, the page returned by the `hello_html` function must be displayed.
#
# 🇺🇦 Ukrainian version:
#
# Формування HTML-відповіді
#
# 1. Створи функцію представлення `hello_html`, яка повертає HTML-сторінку із заголовком "Welcome to Django!" і текстом під заголовком "This is an HTML response.".
#
# 2. Зареєструй це представлення у файлі `urls.py` з шляхом `html/`.
#
# 3. При переході за URL `http://localhost:8000/html/` має відображатися повідомлення у HTML-форматі.
#
# Вимоги:
#
# 1. У проєкті має бути створена функція представлення з ім’ям `hello_html`.
# 2. Функція `hello_html` повинна повертати HTTP-відповідь у форматі HTML із заголовком "Welcome to Django!" і текстом "This is an HTML response.".
# 3. У представленні має бути імпортований `HttpResponse` із `django.http`.
# 4. Функція представлення повинна бути зареєстрована у файлі `urls.py` із шляхом `html/`.
# 5. Для реєстрації маршруту в `urls.py` потрібно використовувати функцію `path()`.
# 6. При переході за адресою `http://localhost:8000/html/` повинна відображатися сторінка, яку повертає функція `hello_html`.

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
