# Publishing Ports in Docker Compose
# Create a docker-compose.yml file that describes a container with Nginx
# that publishes ports: 8080 for HTTP and 8443 for HTTPS.
# Use Docker Compose to start the container.
#
# Requirements:
# • A file named docker-compose.yml must be created, containing the configuration for the container.
# • The docker-compose.yml file must describe a container with Nginx installed.
# • The docker-compose.yml file must configure a parameter that publishes and forwards port 8080
#   to the standard HTTP port inside the container.
# • The docker-compose.yml file must configure a parameter that publishes and forwards port 8443
#   to the standard HTTPS port inside the container.
# • The container must be started using the Docker Compose command based on the configuration
#   defined in the docker-compose.yml file.
#
# ## 🇺🇦 Ukrainian version:
#
# Публікація портів у Docker Compose
# Створіть файл docker-compose.yml, який описує контейнер з Nginx,
# що публікує порти: 8080 для HTTP і 8443 для HTTPS.
# Використовуйте Docker Compose для запуску контейнера.
#
# Вимоги:
# • Необхідно створити файл з іменем docker-compose.yml, який буде містити конфігурацію для контейнера.
# • Файл docker-compose.yml має описувати контейнер, в якому встановлено Nginx.
# • У файлі docker-compose.yml має бути налаштовано параметр, який публікує та перенаправляє порт 8080
#   на стандартний HTTP порт всередині контейнера.
# • У файлі docker-compose.yml має бути налаштовано параметр, який публікує та перенаправляє порт 8443
#   на стандартний HTTPS порт всередині контейнера.
# • Контейнер має бути запущеним за допомогою команди Docker Compose на основі конфігурації,
#   заданої у файлі docker-compose.yml.

# Starting the container using Docker Compose
docker compose up -d