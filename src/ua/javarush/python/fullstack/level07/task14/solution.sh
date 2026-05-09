# Installing Grafana
# Install Grafana on your system.
# Add the official Grafana repository, update the system, and install Grafana.
#
# Requirements:
# • The script must include a command to add the official Grafana repository to the system repository list.
# • The script must contain a command to update the system package list after adding the new repository.
# • The script must include a command to install the Grafana package using the system package manager.
#
# 🇺🇦 Ukrainian version:
#
# Встановлення Grafana
# Встановіть Grafana на вашій системі. Додайте офіційний репозиторій Grafana, оновіть систему і встановіть Grafana.
#
# Вимоги:
# • Скрипт повинен включати команду для додавання офіційного репозиторію Grafana до списку репозиторіїв системи.
# • Скрипт повинен містити команду для оновлення списку пакетів системи після додавання нового репозиторію.
# • Скрипт повинен включати команду для встановлення пакету Grafana за допомогою пакетного менеджера системи.

# Adding the official Grafana repository
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

# Updating the package list
sudo apt-get update

# Installing Grafana
apt-get install grafana