# Checking Service Logs
# Create a docker-compose.yml file with two services:
# an Nginx web server and a PostgreSQL database.
# After starting the application, display the logs of the web server.
#
# Requirements:
# • The docker-compose.yml file must contain definitions for two services:
#   an Nginx-based web server and a PostgreSQL-based database.
# • The services described in docker-compose.yml must be started with the `docker compose up` command.
# • After the services are started successfully, the logs of the Nginx web server
#   must be displayed and reviewed using the `docker compose logs` command.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка логів сервісу
# Створіть файл docker-compose.yml з двома сервісами: вебсервером на Nginx та базою даних PostgreSQL.
# Після запуску додатку відобразіть логи вебсервера.
#
# Вимоги:
# • Файл docker-compose.yml повинен містити опис двох сервісів: вебсервер на базі Nginx та базу даних на базі PostgreSQL.
# • Сервіси, описані в docker-compose.yml, повинні запускатися командою `docker compose up`.
# • Після успішного запуску сервісів необхідно за допомогою команди `docker compose logs` відобразити та переглянути логи
# вебсервера Nginx.

# Start Docker Compose
docker compose up -d

# Checking the logs of the Nginx web server
docker compose logs web