# Formatting the Output of the Container List
# Display a list of all running containers, showing only their names, status, and published ports.
# Use the formatting parameter for the docker ps command.
#
# Requirements:
# • The script must use the `docker ps` command to get the list of all running containers.
# • Use the formatting parameter to display only container names.
# • Use the formatting parameter to display only the status of each container.
# • Use the formatting parameter to display only the published ports for each container.
# • Use command-line formatting parameters to display the names, status, and published ports of containers
# in a single output.
#
# ## 🇺🇦 Ukrainian version:
#
# Форматування виводу списку контейнерів
# Виведіть список усіх запущених контейнерів, відобразивши тільки їхні імена, статус та перенаправлені порти.
# Використовуйте параметр форматування для команди docker ps.
#
# Вимоги:
# • Скрипт має використовувати команду `docker ps` для отримання списку всіх запущених контейнерів.
# • Використовуйте параметр форматування, щоб вивести лише імена контейнерів.
# • Використовуйте параметр форматування, щоб вивести тільки статус кожного контейнера.
# • Використовуйте параметр форматування, щоб вивести лише перенаправлені порти для кожного контейнера.
# • Використовуйте параметри форматування командного рядка для одночасного відображення імен, статусу і
# перенаправлених портів контейнерів в одному виводі.

# Displaying a list of all running containers with names, status, and published ports
docker ps --format "{{.Names}}\t{{.Status}}\t{{.Ports}}"