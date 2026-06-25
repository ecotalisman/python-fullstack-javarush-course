# Installing Dependencies from the requirements.txt File
#
# 1. Create a new folder for the project. Simulating teamwork, copy the `requirements.txt` file into this folder.
#
# 2. Create a new virtual environment and install the dependencies specified in `requirements.txt` using the `pip install` command.
#
# 3. All dependencies from the `requirements.txt` file must be installed into the virtual environment.
#
# Requirements:
#
# 1. Create a new folder that will serve as the root directory for the project.
# 2. The `requirements.txt` file must be copied into the created folder to simulate a team collaboration situation.
# 3. A new virtual environment must be created within the project.
# 4. All dependencies specified in the `requirements.txt` file must be installed into this virtual environment using the `pip install` command.
# 5. All dependency installation actions must be performed in the activated virtual environment.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення залежностей із файлу requirements.txt
#
# 1. Створи нову папку для проєкту. Імітуючи колективну роботу в команді, скопіюй файл `requirements.txt` у цю папку.
#
# 2. Створи нове віртуальне оточення та встанови залежності, зазначені у `requirements.txt`, за допомогою команди `pip install`.
#
# 3. Усі залежності з файлу `requirements.txt` повинні бути встановлені у віртуальне оточення.
#
# Вимоги:
#
# 1. Створи нову папку, яка буде слугувати кореневою директорією для проєкту.
# 2. Файл `requirements.txt` має бути скопійований у створену папку, щоб імітувати ситуацію спільної роботи в команді.
# 3. Повинно бути створене нове віртуальне оточення в межах проєкту.
# 4. Усі залежності, зазначені у файлі `requirements.txt`, повинні бути встановлені у це віртуальне оточення за допомогою команди `pip install`.
# 5. Всі дії з встановлення залежностей повинні відбуватись в активованому віртуальному оточенні.

#!/bin/bash

# Create a new folder for the project
mkdir test_folder

# Copy the requirements.txt file into the project folder
cp requirements.txt test_folder/

# Go to the project folder
cd test_folder

# Create a virtual environment, name it venv
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt