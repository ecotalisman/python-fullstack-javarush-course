# Viewing Only Stopped Containers
# Display a list of only stopped containers. Use status-based filtering with the docker ps command.
#
# Requirements:
# • The script must use the `docker ps` command to display containers.
# • It is necessary to apply status filtering to display only stopped containers.
# • The result of the command must show a list of containers that are exclusively in the "stopped" state.
#
# ## 🇺🇦 Ukrainian version:
#
# Відобразіть список тільки зупинених контейнерів
# Використовуйте фільтрацію за статусом для команди docker ps.
#
# Вимоги:
# • Скрипт має використовувати команду `docker ps` для відображення контейнерів.
# • Необхідно застосувати фільтрацію за статусом, щоб відобразити тільки зупинені контейнери.
# • Результат виконання команди має показати список контейнерів, які перебувають виключно у стані "зупинено".

# Script for displaying only stopped Docker containers
docker ps -f "status=exited"