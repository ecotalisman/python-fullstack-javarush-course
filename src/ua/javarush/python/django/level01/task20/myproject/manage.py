# Working with Model Data in a View
#
# 1. Write a `homepage` function that returns the text "Welcome to our site!".
#
# 2. Use `django.http.HttpResponse`.
#
# Requirements:
#
# 1. Create a new Django project named `myproject`.
# 2. The code must define a function named `homepage`.
# 3. The `homepage` function must return the text response "Welcome to our site!".
# 4. The `django.http.HttpResponse` class must be used to return the response in the function.
# 5. The function must be implemented according to the principles of Django views.
#
# 🇺🇦 Ukrainian version:
#
# Робота з даними з моделі у представленні
#
# 1. Напиши функцію homepage, яка повертає текст "Ласкаво просимо на наш сайт!".
#
# 2. Використовуй django.http.HttpResponse
#
# Вимоги:
#
# 1. Створи новий Django-проєкт з імʼям `myproject`.
# 2. У коді повинна бути визначена функція з імʼям `homepage`.
# 3. Функція `homepage` повинна повертати текстову відповідь "Ласкаво просимо на наш сайт!".
# 4. Для повернення відповіді у функції потрібно використати клас `django.http.HttpResponse`.
# 5. Функція має бути реалізована згідно з принципами роботи Django-представлень.


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
