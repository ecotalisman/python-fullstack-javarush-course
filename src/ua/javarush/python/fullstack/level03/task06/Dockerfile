# Optimizing a Dockerfile with Dependency Installation
# Create a Dockerfile in which the package.json file is copied first,
# dependencies are installed using npm install, and only then the entire application code is copied.
# Use Node.js version 20 and specify the environment variable NODE_ENV=production.
# The application must run on port 8080.
#
# Requirements:
# • The Dockerfile must first copy the package.json file into the container before running the command to install dependencies.
# • The Dockerfile must include the npm install command to install the dependencies specified in package.json.
# • After installing dependencies, the Dockerfile must copy the entire application code into the container.
# • The Dockerfile must use a base image with Node.js version 20 installed.
# • The Dockerfile must specify the NODE_ENV environment variable with the value production.
# • The application inside the container must be configured to run on port 8080.
#
# ## 🇺🇦 Ukrainian version:
#
# Оптимізація Dockerfile з установкою залежностей
# Створіть Dockerfile, в якому спочатку копіюється файл package.json,
# встановлюються залежності через npm install, а потім копіюється весь код застосунку.
# Використовуйте версію Node.js 20 і вкажіть змінну оточення NODE_ENV=production.
# Застосунок має запускатися на порту 8080.
#
# Вимоги:
# • Dockerfile повинен спочатку копіювати файл package.json у контейнер перед виконанням команди для встановлення залежностей.
# • Dockerfile повинен включати команду npm install для встановлення залежностей, вказаних у package.json.
# • Після встановлення залежностей, Dockerfile повинен копіювати весь код застосунку в контейнер.
# • Dockerfile повинен використовувати базовий образ із встановленою версією Node.js 20.
# • Dockerfile повинен вказувати змінну оточення NODE_ENV зі значенням production.
# • Застосунок у контейнері має бути налаштований на запуск на порту 8080.

# Using the Node.js version 20 base image
FROM node:20

# Setting the working directory
WORKDIR /app

# Copying the package.json and package-lock.json files
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the entire application code
COPY . .

# Setting the NODE_ENV environment variable
ENV NODE_ENV=production

# Exposing port 8080
EXPOSE 8080

# Command to start the application
CMD [ "npm", "start" ]