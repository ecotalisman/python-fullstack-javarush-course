# Starting a Local Server with Network Access
#
# 1. Create a new Django project named "network_project".
#
# 2. Start the local dev server on port 8080 with network access.
#
# Requirements:
#
# 1. The program must create a new Django project named "network_project".
# 2. The local Django dev server must be started.
# 3. The local server must be started on port 8080. To do this, the appropriate parameter must be used when starting the server.
# 4. The server must be accessible not only on localhost, but also from the network. To do this, the address `0.0.0.0` should be specified when starting the server.
#
# 🇺🇦 Ukrainian version:
#
# Запуск локального сервера з доступом в мережу
#
# 1. Створи новий Django-проект з ім'ям "network_project".
#
# 2. Запусти локальний dev-сервер на порту 8080 з доступом із мережі.
#
# Вимоги:
#
# 1. Програма повинна створити новий Django-проект з ім'ям "network_project".
# 2. Необхідно запустити локальний dev-сервер Django.
# 3. Локальний сервер має бути запущений на порту 8080. Для цього треба використати відповідний параметр під час запуску сервера.
# 4. Сервер повинен бути доступний не лише на localhost, а й з мережі. Для цього слід вказати адресу `0.0.0.0` під час запуску сервера.

#!/bin/bash

# Create a Django project
django-admin startproject network_project

# Start the server on port 8080 with network access
cd network_project
python manage.py runserver 0.0.0.0:8080