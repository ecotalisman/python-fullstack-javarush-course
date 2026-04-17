# Running All Application Containers
# Create a docker-compose.yml file to run a simple web application based on Nginx. The web server must be available on port 8080. Run the application using Docker Compose.
#
# Requirements:
# • The docker-compose.yml file must be created in the root directory of the application.
# • The docker-compose.yml file must describe an Nginx service that uses the official Nginx image from Docker Hub.
# • The Nginx web server must be configured to map port 80 inside the container to port 8080 on the host machine.
# • The web application must be run using the `docker compose up` command, which will bring up all services described in docker-compose.yml.
#
# ## 🇺🇦 Ukrainian version:
# Запуск усіх контейнерів застосунку
# Створіть файл docker-compose.yml для запуску простого веб-застосунку на базі Nginx. Веб-сервер має бути доступний на порту 8080. Запустіть застосунок за допомогою Docker Compose.
#
# Вимоги:
# • Файл docker-compose.yml має бути створений у кореневій директорії застосунку.
# • У файлі docker-compose.yml має бути описаний сервіс Nginx, який використовуватиме офіційний образ Nginx з Docker Hub.
# • Веб-сервер Nginx має бути налаштований так, щоб мапувати порт 80 всередині контейнера на порт 8080 на хост-машині.
# • Веб-застосунок має бути запущений за допомогою команди `docker compose up`, що забезпечить підняття всіх описаних у docker-compose.yml сервісів.

# Running the application using Docker Compose
docker compose up