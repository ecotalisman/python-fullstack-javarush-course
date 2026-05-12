# Configuring Filebeat to Collect Docker Logs
# Install and configure Filebeat to collect logs from all Docker containers.
# Filebeat must send logs to Logstash, which runs on port 5044.
# Update the filebeat.yml configuration file.
#
# Requirements:
# • Filebeat must be installed on the same machine where the Docker containers are running to ensure that their logs can be collected.
# • The filebeat.yml configuration must be updated to enable the Docker module, which provides log collection from all running Docker containers.
# • Filebeat must be configured to send the collected logs to Logstash, which runs on port 5044, for further processing.
# • Filebeat must be configured and started as a service so that log collection starts automatically after a system reboot or power failure.
# • It is necessary to make sure that Filebeat successfully connects to Logstash on port 5044 and sends data without errors.
#
# 🇺🇦 Ukrainian version:
#
# Налаштування Filebeat для збору логів Docker
# Встановіть і налаштуйте Filebeat для збору логів усіх Docker-контейнерів. Filebeat повинен надсилати логи в Logstash, який працює на порту 5044. Оновіть файл конфігурації filebeat.yml.
#
# Вимоги:
# • Filebeat повинен бути встановлений на тій же машині, де запущені Docker-контейнери, для забезпечення можливості збору їх логів.
# • Конфігурація filebeat.yml повинна бути оновлена для включення модуля Docker, який забезпечує збір логів з усіх запущених Docker-контейнерів.
# • Filebeat повинен бути налаштований на надсилання зібраних логів у Logstash, який працює на порту 5044, для подальшої обробки.
# • Filebeat повинен бути налаштований і запущений як служба, щоб автоматично починати збір логів під час перезавантаження системи або після відключення живлення.
# • Необхідно переконатися, що Filebeat успішно підключається до Logstash на порту 5044 і передає дані без помилок.

# Installing apt-transport-https:
sudo apt-get install apt-transport-https

# Adding the public key:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Adding the Filebeat repository:
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'

# Updating the package list:
sudo apt-get update

# Installing Filebeat:
sudo apt-get install filebeat

# Enabling the Docker module in Filebeat:
sudo filebeat modules enable docker

# Starting the service:
sudo systemctl start filebeat

# Configuring autostart:
sudo systemctl enable filebeat

# Checking Filebeat operation:
sudo systemctl status filebeat