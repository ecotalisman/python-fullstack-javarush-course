# Creating a URL File and Routing for an Application
#
# 1. Create a new Django project named "website" and add an application named "store" to it.
#
# 2. In the "store" application directory, create a `urls.py` file if it does not already exist.
#
# 3. Configure the project routes so that the `/store/` URL is sent to the "store" application. To do this:
#
# - Add the `path('store/', include('store.urls'))` route to the `urls.py` file of the "website" project.
#
# - Add the `path('', views.index, name='store_index')` route to the `store/urls.py` file.
#
# 4. Create an `index` function in the `views.py` file of the "store" application that returns a simple HTTP response with the string "Welcome to the online store!".
#
# 5. Start the dev server.
#
# Requirements:
#
# 1. A Django project named "website" must be created.
# 2. An application named "store" must be added to the "website" project.
# 3. The "store" application directory must contain a `urls.py` file. If it does not exist, it must be created.
# 4. The `path('store/', include('store.urls'))` route must be added to the `urls.py` file of the "website" project to redirect the `/store/` URL to the "store" application.
# 5. The `path('', views.index, name='store_index')` route must be added to the `store/urls.py` file of the "store" application.
# 6. The `index` function must be defined in the `views.py` file of the "store" application. It must return an HTTP response with the string "Welcome to the online store!".
# 7. The local Django development server must be started to test the routing.
#
# 🇺🇦 Ukrainian version:
#
# Створення файлу URL та маршрутизації для застосунку
#
# 1. Створи новий проект Django з ім'ям "website" і додай в нього застосунок з ім'ям "store".
#
# 2. У каталозі застосунку "store" створи файл `urls.py`, якщо його ще немає.
#
# 3. Налаштуй маршрути проекту так, щоб URL `/store/` відправлявся на застосунок "store". Для цього:
#
# - Додай у файл `urls.py` проекту `website` маршрут `path('store/', include('store.urls'))`.
#
# - Додай у файл `store/urls.py` маршрут `path('', views.index, name='store_index')`.
#
# 4. Створи функцію `index` у `views.py` застосунку "store", яка повертає просту HTTP-відповідь з рядком "Ласкаво просимо в інтернет-магазин!".
#
# 5. Запусти dev-сервер.
#
# Вимоги:
#
# 1. Потрібно створити проект Django з ім'ям "website".
# 2. У проекті "website" треба додати застосунок з ім'ям "store".
# 3. У каталозі застосунку "store" має бути файл `urls.py`, якщо його немає — потрібно створити.
# 4. У файлі `urls.py` проекту "website" має бути доданий маршрут `path('store/', include('store.urls'))`, щоб перенаправляти URL `/store/` на застосунок "store".
# 5. У файлі `store/urls.py` застосунку "store" потрібно додати маршрут `path('', views.index, name='store_index')`.
# 6. У файлі `views.py` застосунку "store" потрібно визначити функцію `index`, яка повертає HTTP-відповідь з рядком "Ласкаво просимо в інтернет-магазин!".
# 7. Потрібно запустити локальний сервер розробки Django для тестування маршрутизації.

"""
Main file for managing the Django project.
It is run with commands such as "python manage.py runserver".
"""

import os
import sys


def main():
    try:
        # Set the environment variable to use the Django settings
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

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
