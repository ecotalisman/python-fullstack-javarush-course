# Viewing Logs of the Running Application
# Start the application and display the logs of all services
# (the web server and the database) using the docker compose logs command.
# Use the flag for continuous monitoring of new log entries.
#
# Requirements:
# • The web application must be started using the `docker compose up` command, which should bring up all services defined in docker-compose.yml.
# • The `docker compose logs` command must be used to display the logs of all services, including the web server and the database.
# • The appropriate flag must be used with the `docker compose logs` command for continuous monitoring of new log entries.
#
# ## 🇺🇦 Ukrainian version:
# Перегляд логів запущеного додатку
# Запустіть додаток і виведіть логи всіх сервісів
# (веб-сервера та бази даних) за допомогою команди docker compose logs.
# Використовуйте прапор для безперервного відстеження нових записів у логах.
#
# Вимоги:
# • Веб-додаток повинен бути запущений за допомогою команди `docker compose up`, що забезпечить підйом всіх описаних у docker-compose.yml сервісів.
# • Команда `docker compose logs` повинна бути використана для виводу логів всіх сервісів, включаючи веб-сервер та базу даних.
# • Необхідно використовувати відповідний прапор з командою `docker compose logs` для безперервного відстеження нових записів у логах.
#
# Make sure the application from task 1 is running
docker compose up -d

# Continuously monitor the logs of all services
docker compose logs -f