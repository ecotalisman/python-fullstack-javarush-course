# Choosing a Minimal Base Image
# Write a Dockerfile for a Python application that uses the minimal alpine base image.
# The application must output "Hello, World!" when it starts.
# Pay attention to installing Python and the required dependencies using a minimal set of commands.
# After creating the Dockerfile, build and run the container.
#
# Requirements:
# • The Dockerfile must be based on the minimal Alpine Linux base image to reduce the size of the final image.
# • The Dockerfile must describe how to install Python on Alpine using a minimal set of commands.
# • The application located in the container must output "Hello, World!" when the container starts.
# • The Dockerfile must contain a minimal number of steps to install Python and run the application in order to reduce build time and image size.
# • After creating the Dockerfile, the container must be built and run, ensuring that it executes the application correctly and outputs "Hello, World!".
#
# ## 🇺🇦 Ukrainian version:
#
# Вибір мінімального базового образу
# Напишіть Dockerfile для Python-додатку, який використовує мінімальний базовий образ alpine.
# Додаток повинен виводити "Hello, World!" під час запуску.
# Зверніть увагу на встановлення Python та необхідних залежностей з мінімальним набором команд.
# Після створення Dockerfile, зберіть і запустіть контейнер.
#
# Вимоги:
# • Dockerfile повинен бути заснований на мінімальному базовому образі Alpine Linux для зменшення розміру кінцевого образу.
# • У Dockerfile має бути написано, як встановити Python на Alpine, використовуючи мінімальний набір команд.
# • Додаток, розташований у контейнері, повинен виводити "Hello, World!" під час запуску контейнера.
# • Dockerfile має містити мінімальну кількість кроків для встановлення Python і запуску додатку, щоб скоротити час збирання та розмір образу.
# • Після створення Dockerfile необхідно зібрати та запустити контейнер, переконавшись, що він правильно виконує додаток і виводить "Hello, World!".

# Building the Docker image:
docker build -t app .

# Running the container:
docker run app