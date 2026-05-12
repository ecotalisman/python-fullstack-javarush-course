# Installing Elasticsearch
# Install Elasticsearch on your server by adding the appropriate repository and downloading the required public key.
# After that, start the Elasticsearch service and configure it to start automatically.
#
# Requirements:
# • The installation script must include a command that adds the appropriate Elasticsearch repository to the system.
# • Before installation, the Elasticsearch public key must be downloaded and added to verify the security of the source.
# • After installation, the Elasticsearch service must be started to make sure it is working correctly.
# • After the service has started successfully, Elasticsearch autostart must be configured so that it starts automatically when the system starts.
#
# 🇺🇦 Ukrainian version:
#
# Встановіть Elasticsearch на ваш сервер, додавши відповідний репозиторій та завантаживши необхідний публічний ключ. Після цього запустіть службу Elasticsearch і налаштуйте її автозапуск.
#
# Вимоги:
# • Встановлювальний сценарій має включати команду, що додає відповідний репозиторій для Elasticsearch у систему.
# • Перед встановленням необхідно завантажити та додати публічний ключ Elasticsearch для підтвердження безпеки джерела.
# • Після встановлення слід запустити службу Elasticsearch, щоб переконатися, що вона працює коректно.
# • Після успішного запуску служби необхідно налаштувати автозапуск Elasticsearch, щоб він автоматично запускався під час старту системи.

# Adding the public key:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Adding the Elasticsearch repository:
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'

# Updating the package list:
sudo apt-get update

# Installing Elasticsearch:
sudo apt-get install elasticsearch

# Starting the service:
sudo systemctl start elasticsearch

# Configuring autostart:
sudo systemctl enable elasticsearch