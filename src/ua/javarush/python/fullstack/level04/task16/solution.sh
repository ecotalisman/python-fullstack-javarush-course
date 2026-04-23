# Stopping and Removing Volumes
# Write a command to stop all services and also remove the volumes used by the containers.
#
# Requirements:
# • It is necessary to use a command that guarantees stopping all running Docker services.
# • The command must include the removal of volumes used by the containers.
#
# ## 🇺🇦 Ukrainian version:
#
# Зупинка і видалення томів
# Напишіть команду для зупинки всіх сервісів, а також видалення томів, які використовувалися контейнерами.
#
# Вимоги:
# • Необхідно використовувати команду, яка гарантує зупинку всіх запущених сервісів Docker.
# • Команда має включати видалення томів, які використовувалися контейнерами.

# Stopping all running Docker services
docker compose down --volumes