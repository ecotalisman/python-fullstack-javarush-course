# Creating and Running a Docker Image
# Create a Dockerfile for a Python application that outputs "Hello, Docker!".
# Build an image named my_python_app and run a container based on it.
#
# Requirements:
# • A Dockerfile must be created and configured for a Python application that outputs "Hello, Docker!".
# • The image must be built with the name my_python_app using the Dockerfile.
# • The container must be started based on the built my_python_app image and output "Hello, Docker!" when launched.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення та запуск Docker Image
# Створіть Dockerfile для Python-додатка, який виводить "Hello, Docker!".
# Зберіть образ із ім'ям my_python_app та запустіть контейнер на його основі.
#
# Вимоги:
# • Dockerfile має бути створеним і налаштованим для Python-додатка, який виводить "Hello, Docker!".
# • Образ має бути зібраний із ім'ям my_python_app, використовуючи Dockerfile.
# • Контейнер має бути запущеним на основі зібраного образу my_python_app і виводити "Hello, Docker!" при запуску.

# Building the Docker image named my_python_app
docker build -t my_python_app .

# Running a container based on the built image
docker run --rm my_python_app