# Combining URL Parameters and GET Requests
#
# 1. Write a view and a route that allow displaying a list of users, filtering them by age and name.
#
# 2. The route must have a `min_age` parameter to specify the minimum age.
#
# 3. The user can pass the `name` parameter in a GET request to filter by name.
#
# 4. Example: when opening the URL `/users/18/?name=John`, users named "John" whose age is greater than or equal to 18 must be displayed.
#
# Requirements:
#
# 1. The view must be implemented to filter users by minimum age, using the `min_age` parameter in the route, and by name, using the `name` parameter in the GET request.
# 2. A URL route containing the required `min_age` parameter must be configured.
# 3. The view must filter users whose age is greater than or equal to the `min_age` value passed in the URL.
# 4. If the `name` parameter is specified in the GET request, the view must filter users by the specified name.
# 5. The view must be able to combine both filters, age and name, to find matching users.
# 6. When accessing the route `/users/18/?name=John`, only users whose name is "John" and whose age is 18 or older must be returned.
#
# 🇺🇦 Ukrainian version:
#
# Комбінація параметрів у URL та GET-запитах
#
# 1. Напиши view і маршрут, які дозволяють виводити список користувачів, фільтруючи їх за віком та ім'ям.
#
# 2. У маршруті повинен бути параметр `min_age` для задання мінімального віку.
#
# 3. У GET-запиті користувача можна передати параметр `name` для фільтрації за ім'ям.
#
# 4. Приклад: при відкритті URL `/users/18/?name=John`, мають виводитися користувачі з ім'ям "John", вік яких більше або дорівнює 18 років.
#
# Вимоги:
#
# 1. View має бути реалізовано для фільтрації користувачів за мінімальним віком (параметр `min_age` у маршруті) та ім'ям (параметр `name` у GET-запиті).
# 2. Потрібно налаштувати маршрут URL, що містить обов'язковий параметр `min_age`.
# 3. View повинне фільтрувати користувачів, чий вік більший або дорівнює значенню `min_age`, переданому в URL.
# 4. Якщо у GET-запиті вказано параметр `name`, view має фільтрувати користувачів за зазначеним ім'ям.
# 5. View повинне вміти комбінувати обидва фільтри (вік і ім'я) для пошуку відповідних користувачів.
# 6. При зверненні до маршруту `/users/18/?name=John`, мають повертатися лише ті користувачі, у кого ім'я "John" і вік 18 років або більше.

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
