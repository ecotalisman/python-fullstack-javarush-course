# Recreating Containers
# Write a command to start all services that recreates containers
# even if the configuration has not changed.
# This is useful when it is necessary to fully recreate the environment.
#
# Requirements:
# • The script must include a command that recreates all containers,
#   even if their configuration has not changed.
# • The command must use the Docker Compose utility
#   to manage services and containers.
# • The command must ensure that containers are recreated
#   without changes to the existing service configurations.
#
# ## 🇺🇦 Ukrainian version:
#
# Перестворення контейнерів
# Напишіть команду для запуску всіх сервісів, яка перестворює контейнери,
# навіть якщо конфігурація не змінилася.
# Це корисно, коли необхідно повністю перестворити середовище.
#
# Вимоги:
# • Скрипт повинен включати команду, яка перестворює всі контейнери,
#   навіть якщо їх конфігурація не змінилася.
# • Команда повинна використовувати утиліту Docker Compose для керування сервісами та контейнерами.
# • Команда повинна забезпечувати перестворення контейнерів без змін в існуючих конфігураціях сервісів.

# Recreating all containers with Docker Compose, even if the configuration has not changed.
docker compose up --force-recreate