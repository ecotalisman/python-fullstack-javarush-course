# Creating a Superuser and Configuring the Admin Panel
#
# 1. Create a new Django project and name it `myproject`.
#
# 2. Using the `createsuperuser` command, create a new superuser with the username `admin` and the password `987654321`.
#
# Requirements:
#
# 1. A new Django project named `myproject` must be created using the `django-admin startproject` command.
# 2. The `manage.py` command must be used to complete the task.
# 3. The `python manage.py createsuperuser` command must be used to create the superuser.
# 4. The new superuser must be given the username `admin`.
# 5. The password `987654321` must be set for the superuser.
#
# 🇺🇦 Ukrainian version:
#
# Створення superuser та налаштування адміністративної панелі
#
# 1. Створи новий проект Django, назви його `myproject`.
#
# 2. За допомогою команди `createsuperuser` створи нового суперкористувача з іменем `admin` та паролем `987654321`.
#
# Вимоги:
#
# 1. Потрібно створити новий проект Django з іменем `myproject` за допомогою команди `django-admin startproject`.
# 2. Для виконання завдання треба використовувати команду `manage.py`.
# 3. Потрібно використати команду `python manage.py createsuperuser` для створення superuser.
# 4. Новому superuser потрібно задати ім'я `admin`.
# 5. Для superuser має бути встановлений пароль `987654321`.

#!/bin/bash

# Create a new Django project named myproject
django-admin startproject myproject

# Go to the project directory
cd myproject

# Apply migrations to configure the database
python manage.py migrate

# Create a superuser with username=admin and password=987654321
# When prompted for the password, enter: 987654321
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=987654321
python manage.py createsuperuser --noinput