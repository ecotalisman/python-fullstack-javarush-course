# Viewing Container Logs
#
# To debug your multi-container application, use the docker compose logs command
# to view the logs of all running containers.
# Find the line in the logs that confirms the successful startup
# of the Nginx server.
#
# Requirements:
#
# 1. The script must use the docker compose logs command
#    to retrieve and display the logs of all running containers.
# 2. A line confirming the successful startup of the Nginx server
#    must be found in the logs.
# 3. The application must be multi-container, which means it includes
#    several containers, including the Nginx server.
#
# 🇺🇦 Ukrainian version:
#
# Перегляд логів контейнерів
#
# Для налагодження вашого багатоконтейнерного додатка
# використовуйте команду docker compose logs,
# щоб переглянути логи всіх запущених контейнерів.
# Знайдіть у логах рядок, який підтверджує успішний запуск сервера Nginx.
#
# Вимоги:
#
# 1. Скрипт має використовувати команду docker compose logs
#    для отримання та відображення логів усіх запущених контейнерів.
# 2. У логах необхідно знайти рядок,
#    який підтверджує успішний запуск сервера Nginx.
# 3. Додаток має бути багатоконтейнерним,
#    що передбачає наявність декількох контейнерів,
#    включаючи сервер Nginx.

# Use docker compose logs to get the logs of all running containers
logs=$(docker compose logs)

# Search the logs for a line that confirms the successful startup of the Nginx server
if echo "$logs" | grep -q "nginx started"; then
    echo "Nginx server has successfully started."
else
    echo "Nginx server start confirmation not found in logs."
fi