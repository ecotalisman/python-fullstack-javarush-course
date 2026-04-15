# Creating a Simple Dockerfile for a Node.js Application
# Create a Dockerfile for a simple Node.js application that runs on port 4000.
# The application must be copied into the container, and its dependencies must be installed using npm install.
# After creating the Dockerfile, build an image named my_node_app and run a container,
# binding container port 4000 to port 4000 on the host machine.
#
# Requirements:
# • A Dockerfile must be created for containerizing the Node.js application.
# • The application must be copied into the container during the Dockerfile build process.
# • The application dependencies must be installed using the npm install command in the Dockerfile.
# • The created image must be named my_node_app.
# • The container must be started with container port 4000 bound to port 4000 on the host machine.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення простого Dockerfile для Node.js застосунку
# Створіть Dockerfile для простого застосунку на Node.js, який запускається на порту 4000.
# Застосунок має бути скопійований у контейнер, а залежності повинні бути встановлені через npm install.
# Після створення Dockerfile зберіть образ з ім'ям my_node_app і запустіть контейнер,
# прив'язавши порт 4000 контейнера до порту 4000 хост-машини.
#
# Вимоги:
# • Dockerfile має бути створений для контейнеризації застосунку на Node.js.
# • Застосунок повинен бути скопійований у контейнер у процесі зборки Dockerfile.
# • Залежності застосунку мають бути встановлені командою npm install у Dockerfile.
# • Створений образ має мати ім'я my_node_app.
# • Контейнер повинен запускатися з прив'язкою порту 4000 контейнера до порту 4000 на хост-машині.

# Building the Docker image:
docker build -t my_node_app .

# Running the container:
docker run -p 4000:4000 --name my_node_app my_node_app