# Installing and Configuring Logstash
# Install Logstash on the server and create a logstash.conf configuration file
# that will collect Docker logs through Filebeat.
# The configuration must send data to Elasticsearch with an index in the format "docker-logs-YYYY.MM.dd".
#
# Requirements:
# • Logstash must be installed on the server to ensure log collection and processing.
# • A logstash.conf file must be created to define how Logstash processes and routes data.
# • The logstash.conf configuration must include settings for receiving logs from Filebeat, which collects Docker logs.
# • The configuration must provide sending the processed data to Elasticsearch.
# • The data sent to Elasticsearch must have an index in the format "docker-logs-YYYY.MM.dd".
#
# 🇺🇦 Ukrainian version:
#
# Встановіть Logstash на сервер і створіть конфігураційний файл logstash.conf, який буде збирати логи Docker через Filebeat. Конфігурація повинна відправляти дані в Elasticsearch з індексом виду "docker-logs-YYYY.MM.dd".
#
# Вимоги:
# • Logstash має бути встановлений на сервері для забезпечення збору та обробки логів.
# • Необхідно створити файл logstash.conf, який визначатиме, як Logstash обробляє та маршрутизує дані.
# • Конфігурація logstash.conf повинна включати налаштування для отримання логів від Filebeat, який збирає логи Docker.
# • Конфігурація повинна передбачати відправку оброблених даних в Elasticsearch.
# • Відправлені в Elasticsearch дані повинні мати індекс у форматі "docker-logs-YYYY.MM.dd".

# Adding the public key:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Adding the Logstash repository:
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'

# Updating the package list:
sudo apt-get update

# Installing Logstash:
sudo apt-get install logstash

# Starting the service:
sudo systemctl start logstash

# Configuring autostart:
sudo systemctl enable logstash
