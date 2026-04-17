# Stopping and Removing All Application Containers
# After starting the application, stop and remove all containers, networks, and volumes created by Docker Compose.
#
# Requirements:
# • The web application must be started using the `docker compose up` command, which should bring up all services defined in docker-compose.yml.
# • To stop all containers created by Docker Compose, the `docker compose down` command or an equivalent solution must be used.
# • The containers must be removed after they are stopped, which can be achieved using the `docker compose down` command, since it removes stopped containers by default.
# • All networks and volumes created by Docker Compose must also be removed, for which the `docker compose down` command should be run with the appropriate flags, such as `--volumes` to remove volumes.
#
# ## 🇺🇦 Ukrainian version:
# Зупинка та видалення всіх контейнерів застосунку
# Після запуску застосунку, зупиніть та видаліть усі контейнери, мережі та томи, створені Docker Compose.
#
# Вимоги:
# • Веб-застосунок повинен бути запущений за допомогою команди `docker compose up`, що забезпечить підняття всіх описаних у docker-compose.yml сервісів.
# • Для зупинки всіх контейнерів, створених Docker Compose, необхідно використовувати команду `docker compose down` або аналогічне рішення.
# • Контейнери повинні бути видалені після їх зупинки, чого можна досягти за допомогою команди `docker compose down`, яка видаляє зупинені контейнери за замовчуванням.
# • Усі мережі та томи, створені Docker Compose, повинні бути також видалені, для чого команда `docker compose down` має бути виконана з відповідними прапорами, такими як `--volumes` для видалення томів.
#
# Stopping and removing all containers, networks, and volumes created by Docker Compose
docker compose up
docker compose down --volumes