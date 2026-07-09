# Dynamic URL for String Parameters
#
# 1. Create a route in the `urls.py` file that will handle a URL of the form `/user/<str:username>/`.
#
# 2. The `user_profile(request, username)` view must return the string: "Welcome, <username>!".
#
# 3. Example: when navigating to `/user/johndoe/`, "Welcome, johndoe!" must be displayed.
#
# Requirements:
#
# 1. In the `urls.py` file, a route that accepts the string parameter `<str:username>` must be defined.
# 2. The `user_profile(request, username)` function must be implemented in the views file, for example, `views.py`.
# 3. In the `urls.py` file, the `/user/<str:username>/` route must be connected to the `user_profile` function.
# 4. The `user_profile` view must accept the `username` parameter and use it in the returned response.
# 5. The view must return a string of the form "Welcome, <username>!", where `<username>` is dynamically replaced with the value passed in the URL.
# 6. When navigating to the URL `/user/johndoe/` in the browser, "Welcome, johndoe!" must be displayed.
#
# 🇺🇦 Ukrainian version:
#
# Динамічний URL для рядкових параметрів
#
# 1. Створи маршрут у файлі `urls.py`, який буде обробляти URL виду `/user/<str:username>/`.
#
# 2. У представленні `user_profile(request, username)` має повертатися рядок: "Ласкаво просимо, <username>!".
#
# 3. Приклад: при переході на `/user/johndoe/` має відобразитись "Ласкаво просимо, johndoe!".
#
# Вимоги:
#
# 1. У файлі `urls.py` потрібно визначити маршрут, який приймає рядковий параметр `<str:username>`.
# 2. Функція `user_profile(request, username)` має бути реалізована у файлі представлень, наприклад, `views.py`.
# 3. У файлі `urls.py` маршрут `/user/<str:username>/` має бути зв'язаний з функцією `user_profile`.
# 4. Представлення `user_profile` повинно приймати параметр `username` і використовувати його у повернутій відповіді.
# 5. Представлення повинно повертати рядок виду "Ласкаво просимо, <username>!", де `<username>` динамічно підставляється значенням, переданим у URL.
# 6. При переході на URL `/user/johndoe/` у браузері має відображатися "Ласкаво просимо, johndoe!".

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
