# Using Ubuntu as the Base Image
# Create a Dockerfile using the ubuntu:20.04 base image that installs Python
# and all required dependencies for running the application.
# The application must be located in the /app directory and output
# "Docker and Python on Ubuntu" when started.
#
# Requirements:
# • The Dockerfile must use the ubuntu:20.04 image as the base image.
# • The Dockerfile must include commands to install Python based on the chosen base image.
# • The application must be placed in the /app directory inside the container, as specified in the Dockerfile.
# • When the container starts, the application must output the line "Docker and Python on Ubuntu".
#
# ## 🇺🇦 Ukrainian version:
#
# Використання Ubuntu як базового образу
# Створіть Dockerfile, використовуючи базовий образ ubuntu:20.04, який встановлює Python
# і всі необхідні залежності для роботи застосунку.
# Застосунок має знаходитись у директорії /app і виводити "Docker and Python on Ubuntu" при запуску.
#
# Вимоги:
# • Dockerfile повинен використовувати образ ubuntu:20.04 як базовий.
# • Dockerfile повинен включати команди для встановлення Python на основі вибраного базового образу.
# • Застосунок має бути розміщено в директорії /app всередині контейнера, як вказано у Dockerfile.
# • При запуску контейнера застосунок має виводити рядок "Docker and Python on Ubuntu".

# Building the Docker image:
docker build -t python_ubuntu_app .

# Running the container:
docker run --name hello_world_container python_ubuntu_app