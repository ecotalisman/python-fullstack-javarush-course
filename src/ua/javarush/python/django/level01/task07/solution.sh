# Creating a Virtual Environment
#
# 1. Create a new directory named "my_project".
#
# 2. Go to this directory.
#
# 3. Create a virtual environment named "venv" inside this folder using the `venv` tool.
#
# Requirements:
#
# 1. The script must create a new directory named "my_project".
# 2. The script must execute the command to go to the created "my_project" directory.
# 3. The built-in Python `venv` tool must be used to create the virtual environment.
# 4. The virtual environment must be created with the name "venv".
# 5. The "venv" virtual environment must be located inside the "my_project" directory.
#
# 🇺🇦 Ukrainian version:
#
# Створення віртуального оточення
#
# 1. Створи нову директорію з іменем "my_project".
#
# 2. Перейди в цю директорію.
#
# 3. Створи віртуальне оточення з іменем "venv" всередині цієї папки з використанням інструменту `venv`.
#
# Вимоги:
#
# 1. Скрипт повинен створити нову директорію з іменем "my_project".
# 2. Скрипт повинен виконати команду для переходу у створену директорію "my_project".
# 3. Для створення віртуального оточення необхідно використати вбудований інструмент Python `venv`.
# 4. Віртуальне оточення має бути створене з іменем "venv".
# 5. Віртуальне оточення "venv" повинно знаходитися всередині директорії "my_project".

#!/bin/bash

# Step 1: Create a new directory named "my_project"
mkdir my_project

# Step 2: Go to the created directory "my_project"
cd my_project

# Step 3: Create a virtual environment named "venv" inside this directory using the `venv` tool
python -m venv venv