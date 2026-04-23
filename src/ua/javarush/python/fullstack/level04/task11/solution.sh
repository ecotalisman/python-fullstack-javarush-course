# Running All Services
# Write a command that starts all services defined in the docker-compose.yml file.
# All containers must start and output their logs to the console.
#
# Requirements:
# • The script must use a command to start all services defined in the docker-compose.yml file.
# • All containers must output their logs to the console immediately after startup.
# • The command must use the docker-compose tool to manage the services.
# • The command must correctly process the docker-compose.yml file to start all services described in it.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск усіх сервісів
# Напишіть команду, яка запустить усі сервіси, визначені у файлі docker-compose.yml.
# Усі контейнери повинні запускатися та виводити свої логи в консоль.
#
# Вимоги:
# • Скрипт має використовувати команду для запуску усіх сервісів, визначених у файлі docker-compose.yml.
# • Усі контейнери повинні виводити свої логи до консолі одразу після запуску.
# • Команда має використовувати інструмент docker-compose для управління сервісами.
# • Команда має коректно обробляти файл docker-compose.yml для запуску усіх описаних у ньому сервісів.

# Running all services in parallel and outputting logs to the console
docker compose up