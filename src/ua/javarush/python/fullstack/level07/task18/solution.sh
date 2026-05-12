# Viewing Container Logs
# Run a container with the name my_container and view its logs using the docker logs command.
# Use the standard command format to output all container logs.
#
# Requirements:
# • The container must be running with the name my_container.
# • The docker logs command must be used to view the container logs.
# • To output all container logs, the standard docker logs command format must be used without additional filters or parameters.
#
# 🇺🇦 Ukrainian version:
#
# Перегляд логів контейнера
# Запустіть контейнер з іменем my_container і перегляньте його логи за допомогою команди docker logs. Використовуйте стандартний формат команди для виводу всіх логів контейнера.
#
# Вимоги:
# • Контейнер повинен бути запущений з ім’ям my_container.
# • Повинна бути використана команда docker logs для перегляду логів контейнера.
# • Для виводу всіх логів контейнера необхідно використовувати стандартний формат команди docker logs без додаткових фільтрів і параметрів.

# Running a container with the name my_container
docker run -d --name my_container nginx

# Viewing the logs of the my_container container
docker logs my_container