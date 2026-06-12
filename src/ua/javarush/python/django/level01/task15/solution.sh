# Starting a Local Server
#
# 1. Create a new Django project named "local_project".
#
# 2. Start the local dev server on port 8888.
#
# Requirements:
#
# 1. The project must be created using the `django-admin startproject` command and must be named "local_project".
# 2. The local development server must be started using the `python manage.py runserver` command.
# 3. The server must be started on port 8888. This must be explicitly specified when running the `runserver` command.
#
# 🇺🇦 Ukrainian version:
#
# Запуск локального сервера
#
# 1. Створи новий проект Django з іменем "local_project".
#
# 2. Запусти локальний dev-сервер на порту 8888.
#
# Вимоги:
#
# 1. Проект має бути створений за допомогою команди `django-admin startproject` та мати ім'я "local_project".
# 2. Локальний сервер розробки має бути запущений за допомогою команди `python manage.py runserver`.
# 3. Сервер повинен бути запущений на порту 8888. Це треба явно вказати під час запуску команди `runserver`.

#!/bin/bash

# Create the "local_project" project
django-admin startproject local_project

# Go to the project directory
cd local_project

# Start the development server on port 8888
python manage.py runserver 8888