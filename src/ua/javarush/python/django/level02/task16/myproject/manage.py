# Applying Migrations and Checking the Database
#
# 1. Create a new application named "library".
#
# 2. In the `models.py` file of this application, create a model named `Book` that will have the following fields:
#
# - `title` of type `CharField` with a maximum length of 200 characters.
#
# - `author` of type `CharField` with a maximum length of 100 characters.
#
# - `published_date` of type `DateField`.
#
# 3. Use the `makemigrations` command to create a migration for this model.
#
# 4. Create and apply a migration that adds the `Book` model to the database.
#
# 5. The table for the `Book` model must be created in the database.
#
# 6. Using the Django shell (`python manage.py shell`), create a new `Book` object with the following data:
#
# - `title`: "Learning Django"
#
# - `author`: "John Doe"
#
# - `published_date`: "2023-10-15"
#
# 7. Save the object to the database and display it on the screen in the terminal.
#
# Requirements:
#
# 1. Create a new Django application named "library" using the Django `startapp` command.
# 2. In the `models.py` file of the "library" application, a model named `Book` must be defined with three fields:
#    - `title` of type `CharField` with a maximum length of 200 characters.
#    - `author` of type `CharField` with a maximum length of 100 characters.
#    - `published_date` of type `DateField`.
# 3. The program must use the `python manage.py makemigrations` command to create a migration containing the changes related to the `Book` model.
# 4. The program must use the `python manage.py migrate` command to apply the created migration and make changes to the database.
# 5. The migration must create a table for the `Book` model in the database.
# 6. In the Django shell, an object of the `Book` model must be created with the following values:
#    - `title`: "Learning Django"
#    - `author`: "John Doe"
#    - `published_date`: "2023-10-15".
# 7. The created `Book` object must be saved to the database using the `save()` method.
# 8. After saving, the `Book` model object must be displayed on the screen in the terminal through the Django shell.
#
# 🇺🇦 Ukrainian version:
#
# Застосування міграцій та перевірка бази даних
#
# 1. Створи новий застосунок із іменем "library".
#
# 2. У файлі `models.py` цього застосунку створи модель з іменем `Book`, яка буде мати такі поля:
#
# - `title` типу `CharField` з максимальною довжиною 200 символів.
#
# - `author` типу `CharField` з максимальною довжиною 100 символів.
#
# - `published_date` типу `DateField`.
#
# 3. За допомогою команди `makemigrations` створи міграцію для цієї моделі.
#
# 4. Створи та застосуй міграцію, яка додає модель `Book` у базу даних.
#
# 5. Таблиця для моделі `Book` повинна бути створена у базі даних.
#
# 6. Використовуючи Django-shell (`python manage.py shell`), створи новий об'єкт `Book` з такими даними:
#
# - `title`: "Learning Django"
#
# - `author`: "John Doe"
#
# - `published_date`: "2023-10-15"
#
# 7. Збережи об'єкт у базі даних і виведи його на екран у терміналі.
#
# Вимоги:
#
# 1. Створи новий Django-застосунок із іменем "library" за допомогою команди Django `startapp`.
# 2. У файлі `models.py` застосунку "library" має бути визначена модель із назвою `Book`, що містить три поля:
#    - `title` з типом `CharField` і максимальною довжиною 200 символів.
#    - `author` з типом `CharField` і максимальною довжиною 100 символів.
#    - `published_date` з типом `DateField`.
# 3. Програма має використовувати команду `python manage.py makemigrations` для створення міграції, що містить зміни, пов’язані з моделлю `Book`.
# 4. Програма має використовувати команду `python manage.py migrate` для застосування створеної міграції та внесення змін у базу даних.
# 5. Міграція має призвести до створення таблиці для моделі `Book` у базі даних.
# 6. У Django-shell необхідно створити об'єкт моделі `Book` з такими значеннями:
#    - `title`: "Learning Django"
#    - `author`: "John Doe"
#    - `published_date`: "2023-10-15".
# 7. Створений об'єкт `Book` потрібно зберегти у базі даних за допомогою методу `save()`.
# 8. Після збереження об'єкт моделі `Book` потрібно вивести на екран у терміналі через Django-shell.

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
