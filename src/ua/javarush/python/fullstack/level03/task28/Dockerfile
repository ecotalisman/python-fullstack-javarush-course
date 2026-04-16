# Using the Official Image for Node.js
# Create a Dockerfile for a simple Node.js application using the node:14 base image.
# The application must run on port 3000 and output "Hello from Node.js!" when accessed
# through a browser or curl. All required dependencies must be installed.
#
# Requirements:
# • The Dockerfile must use the node:14 base image to create the container.
# • The application must be configured to run on port 3000 inside the container.
# • The application must output "Hello from Node.js!" when accessed through a browser or with curl.
# • All required dependencies for the application must be installed in the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання офіційного образу для Node.js
# Створіть Dockerfile для простого Node.js застосунку, використовуючи базовий образ node:14.
# Застосунок має запускатися на порту 3000 та виводити "Hello from Node.js!" при зверненні
# через браузер або curl. Усі необхідні залежності мають бути встановлені.
#
# Вимоги:
# • У Dockerfile має використовуватися базовий образ node:14 для створення контейнера.
# • Застосунок має бути налаштований для роботи на порту 3000 всередині контейнера.
# • Застосунок має виводити "Hello from Node.js!" при зверненні через браузер або за допомогою curl.
# • Усі необхідні залежності для роботи застосунку мають бути встановлені у контейнері.

# Using the Node.js version 14 base image
FROM node:14

# Setting the working directory
WORKDIR /app

# Copying package.json and package-lock.json (if present)
COPY package*.json ./

# Installing dependencies
RUN  npm install

# Copying the application source code
COPY . .

# Exposing the port that will be used
EXPOSE 3000

# Command to start the application
CMD ["node", "app.js"]