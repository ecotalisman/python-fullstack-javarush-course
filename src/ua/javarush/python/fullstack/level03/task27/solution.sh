# Optimization Using Multi-Stage Build
# Create a multi-stage Dockerfile for a React application.
# The first stage must use the node:14 image to build the application,
# and the second stage must use nginx:alpine to deploy it.
# Build and run a container that will serve the React application through Nginx.
#
# Requirements:
# • The Dockerfile must be designed using a multi-stage build, where the first stage uses the node:14 image to build the React application, and the second stage uses the nginx:alpine image to deploy the built application.
# • In the first stage, the React application source code must be copied and the build command must be executed using Node.js.
# • In the second stage, Nginx must be configured to serve the static files of the React application, using either the default configuration or a provided configuration.
# • After writing the Dockerfile, it is necessary to build the Docker image and run a container that will serve the React application through Nginx on the specified ports.
# • The multi-stage build must be optimized to minimize the size of the final Docker image by removing intermediate layers and unnecessary files.
#
# ## 🇺🇦 Ukrainian version:
#
# Оптимізація з використанням багатоступеневої збірки
# Створіть багатоступеневий Dockerfile для React-додатка.
# Перший етап має використовувати образ node:14 для збірки додатка,
# а другий етап має використовувати nginx:alpine для його розгортання.
# Зберіть і запустіть контейнер, який буде обслуговувати React-додаток через Nginx.
#
# Вимоги:
# • Dockerfile має бути розроблений з використанням багатоступеневої збірки, де перший етап використовує образ node:14 для збірки React-додатка, а другий етап використовує образ nginx:alpine для розгортання зібраного додатка.
# • На першому етапі має виконуватися копіювання вихідного коду React-додатка і виконання команди збірки з використанням Node.js.
# • На другому етапі Nginx має бути налаштований для обслуговування статичних файлів React-додатка, з використанням конфігурації за замовчуванням або наданої конфігурації.
# • Після написання Dockerfile необхідно зібрати Docker образ і запустити контейнер, який буде обслуговувати React-додаток через Nginx на зазначених портах.
# • Багатоступенева збірка має бути оптимізована для мінімізації розміру кінцевого Docker образу шляхом видалення проміжних шарів і непотрібних файлів.

# Building the Docker image:
docker build -t app .

# Running the container:
docker run -p 8080:80 app