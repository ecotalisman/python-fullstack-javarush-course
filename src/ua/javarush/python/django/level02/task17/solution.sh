# Creating a requirements.txt File
#
# 1. Create a virtual environment and install the packages `Django==4.2.9` and `djangorestframework==4.12.4` into it.
#
# 2. Save the list of installed dependencies to the `requirements.txt` file using the `pip freeze` command.
#
# 3. A `requirements.txt` file with the specified dependencies must appear in the project folder.
#
# Requirements:
#
# 1. Create a virtual environment to isolate the installed dependencies.
# 2. The specified packages with exact versions must be installed in the virtual environment: `Django==4.2.9` and `djangorestframework==4.12.4`.
# 3. The list of dependencies installed in the virtual environment must be saved to the `requirements.txt` file using the `pip freeze` command.
# 4. The `requirements.txt` file must contain lines for the dependencies `Django==4.2.9` and `djangorestframework==4.12.4`, as well as any related dependencies.
# 5. The `requirements.txt` file must be created in the project folder where the task is being performed.
# 6. The `pip freeze` command must be used to save the dependencies to the file.
#
# 🇺🇦 Ukrainian version:
#
# Створення файлу requirements.txt
#
# 1. Створи віртуальне оточення та встанови в нього пакети `Django==4.2.9` і `djangorestframework==4.12.4`.
#
# 2. Збережи список встановлених залежностей у файл `requirements.txt` за допомогою команди `pip freeze`.
#
# 3. У папці проєкту має зʼявитися файл `requirements.txt` з вказаними залежностями.
#
# Вимоги:
#
# 1. Створи віртуальне оточення для ізоляції встановлених залежностей.
# 2. У віртуальному оточенні повинні бути встановлені зазначені пакети з конкретними версіями: `Django==4.2.9` та `djangorestframework==4.12.4`.
# 3. Список встановлених у віртуальному оточенні залежностей має бути збережений у файл `requirements.txt` за допомогою команди `pip freeze`.
# 4. Файл `requirements.txt` має містити рядки для залежностей `Django==4.2.9` та `djangorestframework==4.12.4`, а також будь-які супутні залежності.
# 5. Файл `requirements.txt` має бути створений у папці проєкту, де виконується завдання.
# 6. Для збереження залежностей у файл повинна бути використана команда `pip freeze`.

#!/bin/bash

# Create a virtual environment
python -m venv my_venv && source my_venv/bin/activate

# Install the required packages
pip install django==4.2.9 djangorestframework==4.12.4

# Save dependencies to the requirements.txt file
pip freeze > requirements.txt

# Deactivate the virtual environment
deactivate

# Output a completion message
echo "The requirements.txt file has been created successfully."
