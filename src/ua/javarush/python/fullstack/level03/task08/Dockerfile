# Using a Minimal Base Image
# Create a Dockerfile that uses a minimal Node.js base image (node:14-alpine).
# The application must run on port 5000, and the APP_ENV environment variable
# must be set to production.
#
# Requirements:
# • The Dockerfile must use a minimal Node.js base image, such as node:14-alpine.
# • The APP_ENV environment variable must be set to production in the Dockerfile.
# • The application described in the Dockerfile must be configured to run on port 5000.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання мінімального базового образу
# Створіть Dockerfile, який використовує мінімальний базовий образ Node.js (node:14-alpine).
# Додаток має запускатися на порту 5000, а змінна оточення APP_ENV має бути встановлена
# в значення production.
#
# Вимоги:
# • Dockerfile має використовувати мінімальний базовий образ Node.js, такий як node:14-alpine.
# • Змінна оточення APP_ENV має бути встановлена у значення production у Dockerfile.
# • Додаток, описаний у Dockerfile, має бути налаштований на запуск на порту 5000.

# Using a minimal Node.js base image
FROM node:14-alpine

# Setting the working directory
WORKDIR /app

# Copying package.json and package-lock.json
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the entire application source code
COPY server.js ./

# Setting the environment variable
ENV APP_ENV=production

# Exposing the port on which the application will run
EXPOSE 5000

# Command to start the application
CMD ["npm", "start"]