# Installing Django via pip
#
# 1. Create a virtual environment in your working directory.
#
# 2. Activate the created environment.
#
# 3. Install Django version 5.1 using `pip`.
#
# 4. Display the installed Django version.
#
# Requirements:
#
# 1. A new virtual environment must be created in the current working directory.
# 2. Activate the created virtual environment.
# 3. Use the `pip` command to install Django version 5.1 in the activated virtual environment.
# 4. Display the installed Django version on the screen after successful installation.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення Django через pip
#
# 1. Створи віртуальне оточення у своїй робочій директорії.
#
# 2. Активуй створене оточення.
#
# 3. Встанови Django версії 5.1 за допомогою `pip`.
#
# 4. Виведи версію встановленого Django.
#
# Вимоги:
#
# 1. Потрібно створити нове віртуальне оточення в поточній робочій директорії.
# 2. Активуй створене віртуальне оточення.
# 3. Використовуй команду `pip` для встановлення Django версії 5.1 в активоване віртуальне оточення.
# 4. Виведи на екран версію встановленого Django після успішної інсталяції.

#!/bin/bash

# Command to create a virtual environment in the current working directory
python -m venv my_env

# Activate the virtual environment
my_env\Scripts\activate

# Install Django version 5.1
pip install django==5.1

# Display the installed Django version for verification
pip list