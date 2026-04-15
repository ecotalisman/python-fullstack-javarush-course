# Multi-Stage Build
# Create a multi-stage Dockerfile for a React application.
# The first stage must use Node.js to build the application,
# and the second stage must use Nginx as a server to serve static files.
# Build an image named react_nginx_app.
#
# Requirements:
# • The Dockerfile must be written using a multi-stage build that contains at least two different stages.
# • The first stage in the Dockerfile must use a Node.js image to build the React application.
# • The second stage in the Dockerfile must use an Nginx image to create a server that serves static files.
# • The resulting Docker image must be built with the name react_nginx_app.
#
# ## 🇺🇦 Ukrainian version:
#
# Багатоетапна збірка
# Створіть багатоетапний Dockerfile для React-додатка.
# Перший етап повинен використовувати Node.js для збірки додатка,
# а другий — Nginx для сервера, який обслуговує статичні файли.
# Зберіть образ з іменем react_nginx_app.
#
# Вимоги:
# • Dockerfile має бути написаний із використанням багатоетапної збірки, що містить як мінімум два різні етапи.
# • Перший етап у Dockerfile має використовувати образ Node.js для збірки React-додатка.
# • Другий етап у Dockerfile має використовувати образ Nginx для створення сервера, який обслуговує статичні файли.
# • Результуючий Docker образ має бути зібраний з іменем react_nginx_app.

# Building the Docker image:
docker build -t react_nginx_app .

# Running the container:
docker run -p 8080:80 react_nginx_app