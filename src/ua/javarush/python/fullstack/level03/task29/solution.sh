# Assigning a Tag When Building an Image
# Write a Dockerfile for a simple Python application that outputs "Hello, Docker!".
# When building the image, assign it the tag myapp:1.0 and run a container based on this image.
#
# Requirements:
# • The Dockerfile must be written in such a way that when the container starts, the message "Hello, Docker!" is displayed.
# • When building the Docker image, it must be assigned the tag myapp:1.0.
# • The container must be run based on the created image with the tag myapp:1.0.
#
# ## 🇺🇦 Ukrainian version:
#
# Присвоєння тега при збірці образу
# Напишіть Dockerfile для простого Python-додатка, яке виводить "Hello, Docker!".
# При збірці образу присвойте йому тег myapp:1.0 і запустіть контейнер на основі цього образу.
#
# Вимоги:
# • Dockerfile має бути написаний таким чином, щоб під час запуску контейнера виводилося повідомлення "Hello, Docker!".
# • Під час збірки Docker-образу необхідно присвоїти йому тег myapp:1.0.
# • Контейнер має бути запущений на основі створеного образу з тегом myapp:1.0.

# Building the Docker image with the tag myapp:1.0
docker build -t myapp:1.0 .

# Running a container based on the image with the tag myapp:1.0
docker run myapp:1.0