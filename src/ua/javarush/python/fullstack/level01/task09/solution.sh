# Running and Managing a Container
# Perform the following actions:
#
# 1. Run a container from the nginx image in detached mode with the name web_container.
# 2. Display the list of running containers.
# 3. Stop the container.
# 4. Restart the container.
# 5. Remove the container after stopping it.
#
# Requirements:
# • The container must be started using the nginx image in detached mode and have the name web_container.
# • Display the list of currently running containers after starting the web_container container.
# • The web_container container must be successfully stopped after it is started.
# • After being stopped, the web_container container must be restarted.
# • The web_container container must be removed after its final stop.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск і управління контейнером
# Виконайте наступні дії:
#
# 1. Запустіть контейнер з образом nginx у фоновому режимі з ім'ям web_container.
# 2. Виведіть список запущених контейнерів.
# 3. Зупиніть контейнер.
# 4. Перезапустіть контейнер.
# 5. Видаліть контейнер після його зупинки.
#
# Вимоги:
# • Контейнер повинен бути запущений з використанням образу nginx у фоновому режимі і мати ім'я web_container.
# • Відобразіть список поточних запущених контейнерів після запуску контейнера web_container.
# • Контейнер web_container повинен бути успішно зупинений після його запуску.
# • Після зупинки контейнер web_container повинен бути перезапущений.
# • Контейнер web_container повинен бути видалений після його остаточної зупинки.

# Running a container from the nginx image in detached mode with the name web_container
docker run -d --name web_container nginx

# Displaying the list of running containers
docker ps

# Stopping the web_container container
docker stop web_container

# Restarting the web_container container
docker start web_container

# Stopping the web_container container before removal
docker restart web_container

# Removing the web_container container
docker stop web_container
docker rm web_container