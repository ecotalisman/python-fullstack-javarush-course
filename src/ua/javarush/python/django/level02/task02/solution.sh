# Activating a Virtual Environment
#
# 1. Create a new virtual environment using the built-in `venv` module. Name it "test_env".
#
# 2. Activate the previously created "test_env" virtual environment.
#
# 3. After activating the virtual environment, run the `pip list` command.
#
# 4. Deactivate the previously activated virtual environment.
#
# Requirements:
#
# 1. A new virtual environment must be created using the built-in Python `venv` module.
# 2. The created virtual environment must be named "test_env".
# 3. The "test_env" virtual environment must be correctly activated.
# 4. After activating the virtual environment, the `pip list` command must be run to check the installed packages.
# 5. After finishing work with the virtual environment, the program must deactivate it.
#
# 🇺🇦 Ukrainian version:
#
# Активація віртуального оточення
#
# 1. Створи нове віртуальне оточення за допомогою вбудованого модуля `venv`. Назви його "test_env".
#
# 2. Активуй раніше створене віртуальне оточення "test_env".
#
# 3. Після активації віртуального оточення виконай команду `pip list`.
#
# 4. Деактивуй раніше активоване віртуальне оточення.
#
# Вимоги:
#
# 1. Необхідно створити нове віртуальне оточення з використанням вбудованого модуля Python `venv`.
# 2. Створене віртуальне оточення повинно називатися "test_env".
# 3. Необхідно правильно активувати віртуальне оточення "test_env".
# 4. Після активації віртуального оточення необхідно виконати команду `pip list` для перевірки встановлених пакетів.
# 5. Після завершення роботи з віртуальним оточенням програма має виконати його деактивацію.

#!/bin/bash

# Create a virtual environment using the venv module
python -m venv test_env

# Activate the virtual environment for Unix-based systems
source test_env\Scripts\activate

# Display the list of installed packages in the activated environment
pip list

# Deactivate the virtual environment
deactivate