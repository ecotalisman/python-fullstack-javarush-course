# pip Manager Installation
#
# Write a command for Linux that installs the pip manager for Python.
#
# Requirements:
#
# 1. The command must be correctly written to install the pip manager.
# 2. The command must be written with the Linux environment in mind.
# 3. The installation must use a standard Linux package manager, such as apt or apt-get.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення pip-менеджера.
#
# Напиши команду для Linux, яка встановить pip менеджер для Python.
#
# Вимоги:
#
# 1. Команда повинна бути правильно складена для встановлення pip менеджера.
# 2. Команда повинна бути написана з урахуванням середовища Linux.
# 3. Для встановлення має використовуватись стандартний менеджер пакетів Linux, наприклад apt або apt-get.

#!/bin/bash
# Update the package list to get up-to-date information about available updates
sudo apt update

# Install the pip manager for Python
sudo apt install -y python3-pip