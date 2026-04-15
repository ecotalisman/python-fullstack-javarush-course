# Basic Image Build
# Create a Dockerfile for a simple Node.js application that runs on port 4000.
# Build an image named my_node_app with the latest tag.
# After building, run a container based on this image, binding container port 4000
# to port 4000 on the host machine.
#
# Requirements:
# • A Dockerfile describing the steps for building a Docker image for a simple Node.js application must be created.
# • The application must be configured to listen on port 4000.
# • Build the Docker image using the Dockerfile and assign it the name my_node_app with the latest tag.
# • After building the Docker image, run a container, binding container port 4000 to port 4000 on the host machine.
#
# ## 🇺🇦 Ukrainian version:
#
# Базова збірка образу
# Створіть Dockerfile для простого Node.js додатка, який працює на порту 4000.
# Зберіть образ з ім'ям my_node_app і тегом latest.
# Після збірки запустіть контейнер на основі цього образу, прив'язавши порт 4000 контейнера
# до порту 4000 хост-машини.
#
# Вимоги:
# • Необхідно створити Dockerfile, який описує кроки збірки Docker-образу для простого Node.js додатка.
# • Додаток має бути налаштований для прослуховування на порту 4000.
# • Зібрати Docker-образ, використовуючи Dockerfile, і присвоїти йому ім'я my_node_app з тегом latest.
# • Після збірки Docker-образу, запустіть контейнер, прив'язавши порт 4000 контейнера до порту 4000 хост-машини.

# Build the Docker image:
docker build -t my_node_app:latest .

# Run the container:
docker run -p 4000:4000 my_node_app:latest
