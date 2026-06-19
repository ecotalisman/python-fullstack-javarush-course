# Working with requirements.txt
#
# 1. Install Django in your virtual environment.
#
# 2. Use the `pip freeze` command to output the list of all installed dependencies to `requirements.txt`.
#
# 3. Delete your current virtual environment, create a new one, and activate it.
#
# 4. Install all dependencies described in the `requirements.txt` file using the `pip install -r requirements.txt` command.
#
# 5. Display the installed dependencies using the `pip list` command.
#
# Requirements:
#
# 1. You must install Django in the activated virtual environment using the `pip install django` command.
# 2. The list of all dependencies installed in the virtual environment must be output to the `requirements.txt` file using the `pip freeze > requirements.txt` command.
# 3. The current virtual environment must be completely deleted.
# 4. After deleting the old environment, a new virtual environment must be created and activated.
# 5. All dependencies specified in the `requirements.txt` file must be installed using the `pip install -r requirements.txt` command.
# 6. After installing the dependencies, the `pip list` command must display the list of all installed libraries to verify their installation.
#
# 🇺🇦 Ukrainian version:
#
# Робота з requirements.txt
#
# 1. Встановіть Django у ваше віртуальне оточення.
#
# 2. Використайте команду `pip freeze`, щоб вивести список усіх встановлених залежностей у `requirements.txt`.
#
# 3. Видаліть ваше поточне віртуальне оточення, створіть нове та активуйте його.
#
# 4. Встановіть усі залежності, описані у файлі `requirements.txt`, використовуючи команду `pip install -r requirements.txt`.
#
# 5. Відобразіть встановлені залежності за допомогою команди `pip list`.
#
# Вимоги:
#
# 1. Ви повинні встановити Django в активоване віртуальне оточення, використовуючи команду `pip install django`.
# 2. Необхідно вивести список усіх встановлених у віртуальному оточенні залежностей у файл `requirements.txt` за допомогою команди `pip freeze > requirements.txt`.
# 3. Поточне віртуальне оточення повинно бути повністю видалене.
# 4. Після видалення старого оточення має бути створене і активоване нове віртуальне оточення.
# 5. Необхідно встановити усі залежності, вказані у файлі `requirements.txt`, за допомогою команди `pip install -r requirements.txt`.
# 6. Після встановлення залежностей за допомогою команди `pip list` має бути виведений список усіх встановлених бібліотек для перевірки їх інсталяції.

#!/bin/bash

# Step 1: Create and activate a virtual environment
python -m venv my_env && my_env\Scripts\activate

# Step 2: Install Django
pip install django

# Step 3: Save the list of all installed dependencies to requirements.txt
pip freeze > requirements.txt

# Step 4: Deactivate the current virtual environment
deactivate

# Step 5: Delete the old virtual environment
rm -r my_env

# Step 6: Create a new virtual environment and activate it
python -m venv new_env && new_env\Scripts\activate

# Step 7: Install dependencies from the requirements.txt file
pip install -r requirements.txt

# Step 8: Check the installed dependencies
pip list