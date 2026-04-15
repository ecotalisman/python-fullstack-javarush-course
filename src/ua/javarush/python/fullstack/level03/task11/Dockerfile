# Using the COPY Instruction
# Create a Dockerfile that copies the server.js file and the package.json file
# from the current directory into the container, into the /app directory.
# Use the Node.js version 14 image. After that, install the dependencies
# and specify the command to run the application.
#
# Requirements:
# • The Dockerfile must use the COPY instruction to copy the server.js file
#   from the current directory into the /app directory inside the container.
# • The Dockerfile must use the COPY instruction to copy the package.json file
#   from the current directory into the /app directory inside the container.
# • The Dockerfile must use the official Node.js version 14 image as the base image
#   for creating the container.
# • After copying the files into the /app directory, the Dockerfile must run
#   a command to install the dependencies specified in the package.json file.
# • The Dockerfile must specify a command (for example, CMD or ENTRYPOINT)
#   to run the Node.js application using the server.js file.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання інструкції COPY
# Створіть Dockerfile, який копіює файл server.js та файл package.json
# із поточної директорії в контейнер, у директорію /app.
# Використовуйте образ Node.js версії 14. Після цього виконайте установку
# залежностей і задайте команду для запуску застосунку.
#
# Вимоги:
# • Dockerfile має використовувати інструкцію COPY, щоб скопіювати файл server.js
#   із поточної директорії в директорію /app всередині контейнера.
# • Dockerfile має використовувати інструкцію COPY, щоб скопіювати файл package.json
#   із поточної директорії в директорію /app всередині контейнера.
# • Dockerfile має використовувати офіційний образ Node.js версії 14
#   як базовий образ для створення контейнера.
# • Після копіювання файлів у директорію /app, Dockerfile має виконати команду
#   для встановлення залежностей, зазначених у файлі package.json.
# • Dockerfile має задати команду (наприклад, CMD або ENTRYPOINT)
#   для запуску застосунку на Node.js, використовуючи файл server.js.

# Using the official Node.js version 14 image as the base image
FROM node:14

# Setting the working directory inside the container
WORKDIR /app

# Copying the package.json file into the working directory
COPY package.json /app/

# Copying the server.js file into the working directory
COPY server.js /app/

# Installing dependencies using NPM
RUN npm install

# Defining the command to run the application
CMD ["node", "server.js"]