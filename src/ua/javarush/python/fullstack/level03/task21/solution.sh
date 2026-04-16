# Using a Minimal Base Image
# Create a Dockerfile for a Python application using the minimal Alpine base image.
# Install Python and copy the application source code into the container.
# Example code: app.py must simply output "Hello, World!".
# After that, build and run the container.
#
# Requirements:
# • The Dockerfile must use the minimal Alpine base image as the foundation for creating the container.
# • The Dockerfile must contain instructions for installing Python in the container to ensure the Python application can run.
# • The Dockerfile must include a command to copy the application source code file (app.py) into the container.
# • The app.py file must contain code that outputs the line "Hello, World!" when executed.
# • After creating the Dockerfile, the container must be successfully built and run to output "Hello, World!" to the console.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання мінімального базового образу
# Створіть Dockerfile для Python-додатка, використовуючи мінімальний базовий образ alpine.
# Встановіть Python та скопіюйте вихідний код додатка в контейнер.
# Приклад коду: app.py повинен просто виводити "Hello, World!".
# Після цього створіть і запустіть контейнер.
#
# Вимоги:
# • Dockerfile повинен використовувати мінімальний базовий образ Alpine як основу для створення контейнера.
# • Dockerfile повинен містити інструкції для встановлення Python у контейнері, щоб забезпечити виконання Python-додатка.
# • Dockerfile повинен включати команду для копіювання файлу вихідного коду додатка (app.py) у контейнер.
# • Файл app.py повинен містити код, який при виконанні виводить рядок "Hello, World!".
# • Після створення Dockerfile необхідно успішно створити контейнер і запустити його, щоб вивести "Hello, World!" в консоль.

# Building the image
docker build -t myapp .

# Running the container
docker run myapp