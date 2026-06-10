# Activating a Virtual Environment and Installing a Dependency
#
# 1. Create a virtual environment named "venv" inside the "my_project" folder.
#
# 2. Activate the created virtual environment.
#
# 3. Install the Django library inside the activated virtual environment.
#
# 4. Display the list of installed packages by running the `pip list` command.
#
# Requirements:
#
# 1. You must create a virtual environment named "venv" inside the "my_project" folder.
# 2. After creating the virtual environment, it must be activated.
# 3. After activating the virtual environment, the Django library must be installed using pip.
# 4. After installing Django, the `pip list` command must be run to display the list of all installed packages.
# 5. The virtual environment must be strictly named "venv" and located inside the "my_project" folder.
# 6. All installation actions and the `pip list` command must be performed inside the activated virtual environment.
#
# 🇺🇦 Ukrainian version:
#
# Активація віртуального оточення та встановлення залежності
#
# 1. Створи віртуальне оточення з іменем "venv" всередині папки "my_project".
#
# 2. Активуй створене віртуальне оточення.
#
# 3. Встанови бібліотеку Django всередині активованого віртуального оточення.
#
# 4. Відобрази список встановлених пакетів, викликавши команду `pip list`.
#
# Вимоги:
#
# 1. Ти повинен створити віртуальне оточення з іменем "venv" у межах папки "my_project".
# 2. Після створення віртуального оточення його потрібно активувати.
# 3. Після активації віртуального оточення необхідно встановити бібліотеку Django використовуючи pip.
# 4. Після встановлення Django треба викликати команду `pip list` для відображення списку всіх встановлених пакетів.
# 5. Віртуальне оточення має бути строго названо "venv" та знаходитися у папці "my_project".
# 6. Усі дії зі встановлення та виклику команди `pip list` потрібно виконувати в активованому віртуальному оточенні.

#!/bin/bash

# Step 1: Create the "my_project" folder if it does not exist
mkdir -p my_project

# Step 2: Create a virtual environment named "venv"
python3 -m venv my_project/venv

# Step 3: Activate the virtual environment
source my_project/venv/bin/activate

# Step 4: Install Django using pip
pip install Django

# Step 5: Display the list of installed packages
pip list