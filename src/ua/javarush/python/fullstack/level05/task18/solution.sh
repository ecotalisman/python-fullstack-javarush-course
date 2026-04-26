# Using a Network in Docker Compose
# Create a docker-compose.yml file that starts two containers:
# one with Nginx (the web service) and another with a custom application (the app service).
# Both services must be connected to the custom my_bridge_network network,
# which must be described in this file.
# Start both services using Docker Compose.
#
# Requirements:
# • The script must include creating a docker-compose.yml file
#   that describes the configuration for two containers.
# • The docker-compose.yml file must contain definitions for two services:
#   web (using the Nginx image) and app (using a custom application).
# • Both services, web and app, must be connected to the custom my_bridge_network network,
#   which must be described in the docker-compose.yml file.
# • Both services must be started using the Docker Compose command
#   so that they can communicate through the specified network.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання мережі в Docker Compose
# Створіть файл docker-compose.yml, який запускає два контейнери:
# один з Nginx (сервіс web), інший з користувацьким додатком (сервіс app).
# Обидва сервіси мають бути підключені до користувацької мережі my_bridge_network,
# яку необхідно описати в цьому файлі.
# Запустіть обидва сервіси за допомогою Docker Compose.
#
# Вимоги:
# • Скрипт має включати створення файлу docker-compose.yml, у якому буде описана конфігурація для двох контейнерів.
# • Файл docker-compose.yml має містити опис двох сервісів: web (з використанням образу Nginx) та app (з використанням користувацького додатка).
# • Обидва сервіси, web і app, мають бути підключені до користувацької мережі my_bridge_network, яка має бути описана у файлі docker-compose.yml.
# • Необхідно запустити обидва сервіси за допомогою команди Docker Compose, щоб вони взаємодіяли через зазначену мережу.

docker compose up -d