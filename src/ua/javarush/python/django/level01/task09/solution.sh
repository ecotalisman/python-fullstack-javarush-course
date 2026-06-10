# Creating a New Django Project
#
# 1. Create a virtual environment for your project and activate it.
#
# 2. Install Django in your virtual environment using `pip install django`.
#
# 3. Create a new Django project named `mywebsite` using the `django-admin startproject` command.
#
# 4. Start the local dev server using the `python manage.py runserver` command.
#
# Requirements:
#
# 1. A virtual environment must be created for the project and activated before further work.
# 2. Django must be installed inside the virtual environment using the `pip install django` command.
# 3. A new Django project named `mywebsite` must be created using the `django-admin startproject` command.
# 4. After completing all previous steps, the local dev server must be started using the `python manage.py runserver` command.
#
# 🇺🇦 Ukrainian version:
#
# Створення нового проекту Django.
#
# 1. Створи віртуальне оточення для твого проекту та активуй його.
#
# 2. Встанови Django у твоє віртуальне оточення за допомогою `pip install django`.
#
# 3. Створи новий Django-проект з назвою `mywebsite` за допомогою команди `django-admin startproject`.
#
# 4. Запусти локальний dev-сервер за допомогою команди `python manage.py runserver`.
#
# Вимоги:
#
# 1. Потрібно створити віртуальне оточення для проекту та активувати його перед подальшою роботою.
# 2. Django повинен бути встановлений всередині віртуального оточення за допомогою команди `pip install django`.
# 3. Потрібно створити новий Django-проект з назвою `mywebsite` з використанням команди `django-admin startproject`.
# 4. Після виконання всіх попередніх кроків локальний dev-сервер має бути запущений за допомогою команди `python manage.py runserver`.

#!/bin/bash

# 1. Create a virtual environment for the project
python -m venv venv

# 2. Activate the virtual environment
venv\Scripts\activate

# 3. Install Django in the virtual environment
pip install django

# 4. Create a new Django project named "mywebsite"
django-admin startproject mywebsite

# Go to the directory of the created project
cd mywebsite

# 5. Start the local Django dev server
python manage.py runserver