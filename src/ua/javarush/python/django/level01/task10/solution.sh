# Project Settings Personalization
#
# 1. Create a virtual environment for your project and activate it.
#
# 2. Install Django in your virtual environment using `pip install django`.
#
# 3. Make changes to the `settings.py` file:
#
# - Change the `LANGUAGE_CODE` parameter to `'uk'`.
#
# - Change the `TIME_ZONE` parameter to `'Europe/Kyiv'`.
#
# 4. Start the local dev server using the `python manage.py runserver` command.
#
# Requirements:
#
# 1. Create a virtual environment for your project and activate it.
# 2. Django must be installed in the virtual environment using the `pip install django` command.
# 3. In the project’s `settings.py` file, the value of the `LANGUAGE_CODE` parameter must be set to `'uk'`.
# 4. In the project’s `settings.py` file, the value of the `TIME_ZONE` parameter must be set to `'Europe/Kyiv'`.
# 5. Start the local dev server using the `python manage.py runserver` command.
#
# 🇺🇦 Ukrainian version:
#
# Персоналізація налаштувань проєкту.
#
# 1. Створи віртуальне оточення для свого проєкту та активуй його.
#
# 2. Встанови Django у своє віртуальне оточення за допомогою `pip install django`.
#
# 3. Внеси зміни до файлу `settings.py`:
#
# - Змiни параметр `LANGUAGE_CODE` на `'uk'`.
#
# - Змiни параметр `TIME_ZONE` на `'Europe/Kyiv'`.
#
# 4. Запусти локальний dev-сервер за допомогою команди `python manage.py runserver`.
#
# Вимоги:
#
# 1. Створи віртуальне оточення для свого проєкту та активуй його.
# 2. У віртуальне оточення потрібно встановити Django за допомогою команди `pip install django`.
# 3. У файлі `settings.py` проєкту потрібно встановити значення параметра `LANGUAGE_CODE` рівним `'uk'`.
# 4. У файлі `settings.py` проєкту потрібно встановити значення параметра `TIME_ZONE` як `'Europe/Kyiv'`.
# 5. Запусти локальний dev-сервер за допомогою команди `python manage.py runserver`.

#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Django
pip install Django==5.1

# Create a new Django project
django-admin startproject myproject

# Make changes to settings.py
# Manually make the required changes

# Start the local dev server
python manage.py runserver