# Handling the POST Method
#
# 1. Write a Django view that handles only POST requests.
#
# 2. If the request method is POST, a JSON response with the text `{"status": "Data received successfully"}` is returned.
#
# 3. If the request is not a POST request, a JSON response with the text `{"error": "Invalid request method"}` and status 400 is returned.
#
# Requirements:
#
# 1. The view must be written as a function that handles HTTP requests.
# 2. It is necessary to check that the request uses exactly the POST method.
# 3. If the request method is POST, the view must return a JSON response with the text `{"status": "Data received successfully"}`.
# 4. If the request is not a POST request, the view must return a JSON response with the text `{"error": "Invalid request method"}`.
# 5. For non-POST requests, the response status must be set to 400.
# 6. Responses must be returned using the `JsonResponse` class.
#
# 🇺🇦 Ukrainian version:
#
# Обробка методу POST
#
# 1. Напиши Django-представлення, яке обробляє тільки POST-запити.
#
# 2. Якщо запит має метод POST, повертається JSON-відповідь з текстом `{"status": "Дані успішно отримані"}`.
#
# 3. Якщо запит не є POST-запитом, повертається JSON-відповідь з текстом `{"error": "Невірний метод запиту"}` і статусом 400.
#
# Вимоги:
#
# 1. Представлення має бути написано як функція, яка обробляє HTTP-запити.
# 2. Потрібно перевірити, що запит використовує саме метод POST.
# 3. Якщо метод запиту - POST, представлення має повертати JSON-відповідь з текстом `{"status": "Дані успішно отримані"}`.
# 4. Якщо запит не є POST-запитом, представлення має повертати JSON-відповідь з текстом `{"error": "Невірний метод запиту"}`.
# 5. Для не-POST запитів потрібно встановлювати статус відповіді 400.
# 6. Відповіді мають повертатися з використанням класу `JsonResponse`.

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
