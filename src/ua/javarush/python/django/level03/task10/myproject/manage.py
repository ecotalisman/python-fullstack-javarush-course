# Using re_path() for a Complex Route
#
# Add a route using the `re_path()` function in your application. The route must handle the URL `/blog/<year>/<month>/<day>/`, where year, month, and day are passed as parameters, but only if they match the format `year — four digits`, `month — one or two digits`, `day — one or two digits`. Create a view function named `blog_archive` in the `views.py` file that accepts the parameters `year`, `month`, and `day`. This function must return the text "Blog archive for <year>-<month>-<day>".
#
# Requirements:
#
# 1. The task requires using the `re_path()` function to define a complex route with a regular expression.
# 2. The route must handle the URL `/blog/<year>/<month>/<day>/`, where:
#    - Year — four digits.
#    - Month — one or two digits.
#    - Day — one or two digits.
# 3. The route regular expression must extract the `year`, `month`, and `day` parameters from the URL and pass them as arguments to the view function.
# 4. In the `views.py` file, a view function named `blog_archive` must be created.
# 5. The `blog_archive` function must accept three parameters: `year`, `month`, `day`.
# 6. The view function must return a string in the format "Blog archive for <year>-<month>-<day>", where the values `<year>`, `<month>`, and `<day>` are inserted from the function parameters.
# 7. The route defined using `re_path()` must be added to the `urls.py` file of your application.
# 8. The URL `/blog/<year>/<month>/<day>/` must be correctly handled by the application and pass the parameters to the view function.
#
# 🇺🇦 Ukrainian version:
#
# Використання re_path() для складного маршруту
#
# Додай маршрут з використанням функції `re_path()` у своєму застосунку. Маршрут має обробляти URL `/blog/<рік>/<місяць>/<день>/`, де рік, місяць і день задаються як параметри, але тільки якщо вони відповідають формату `рік — чотири цифри`, `місяць — одна або дві цифри`, `день — одна або дві цифри`. Створи функцію-представлення `blog_archive` у файлі `views.py`, яка приймає параметри `year`, `month` і `day`. Ця функція повинна повертати текст "Архів блогу за <рік>-<місяць>-<день>".
#
# Вимоги:
#
# 1. Завдання передбачає використання функції `re_path()` для визначення складного маршруту з регулярним виразом.
# 2. Маршрут повинен обробляти URL `/blog/<рік>/<місяць>/<день>/`, де:
#    - Рік — чотири цифри.
#    - Місяць — одна або дві цифри.
#    - День — одна або дві цифри.
# 3. Регулярний вираз маршруту має витягати параметри `рік`, `місяць` і `день` з URL і передавати їх як аргументи у функцію-представлення.
# 4. У файлі `views.py` необхідно створити функцію-представлення з іменем `blog_archive`.
# 5. Функція `blog_archive` повинна приймати три параметри: `year`, `month`, `day`.
# 6. Функція-представлення повинна повертати рядок у форматі "Архів блогу за <рік>-<місяць>-<день>", де значення `<рік>`, `<місяць>` і `<день>` підставляються з параметрів функції.
# 7. Визначений маршрут із використанням `re_path()` має бути доданий до файлу `urls.py` твого застосунку.
# 8. URL `/blog/<рік>/<місяць>/<день>/` має коректно оброблятися застосунком і передавати параметри у функцію-представлення.

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
