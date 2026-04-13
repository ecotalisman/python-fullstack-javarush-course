# Viewing All Containers, Including Stopped Ones
# Display a list of all containers on your system, including both running and stopped containers.
# Use the appropriate option with the docker ps command.
#
# Requirements:
# • Use the `docker ps` command to display the list of containers on the system.
# • Add the appropriate option to the `docker ps` command to display both running and stopped containers.
# • Ensure that information about all containers is displayed, regardless of their current status (running or stopped).
#
# ## 🇺🇦 Ukrainian version:
#
# Перегляд усіх контейнерів, включаючи зупинені
# Відобразіть список усіх контейнерів на вашій системі, включаючи як запущені, так і зупинені контейнери.
# Використовуйте відповідну опцію для команди docker ps.
#
# Вимоги:
# • Використайте команду `docker ps` для відображення списку контейнерів на системі.
# • Додайте відповідну опцію в команду `docker ps`, щоб відобразити як запущені, так і зупинені контейнери.
# • Забезпечте виведення інформації про всі контейнери, незалежно від їх поточного статусу (запущені чи зупинені).

# Script for displaying all containers, including stopped ones
docker ps -a