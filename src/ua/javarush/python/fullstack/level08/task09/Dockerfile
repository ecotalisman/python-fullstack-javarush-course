# Creating a Dockerfile for a React Application
# Create a Dockerfile for the ReactJS frontend service that will use Node.js as the base image.
# Ensure that the application runs on port 3000 and is ready to be built in Docker.
#
# Requirements:
# • The Dockerfile must use a Node.js image as the base image for running the React application.
# • The Dockerfile must include commands to install all required React application dependencies using the npm or yarn package manager.
# • The Dockerfile must ensure that the application runs on port 3000, including the appropriate EXPOSE command.
# • The Dockerfile must contain a command to run the React application, usually npm start or a similar command.
# • The Dockerfile must be correctly structured and include all necessary steps for successfully building and running the container with the React application.
#
# 🇺🇦 Ukrainian version:
#
# Створення Dockerfile для React-додатку
# Створіть Dockerfile для фронтенд-сервісу на ReactJS, який буде використовувати Node.js як базовий образ. Забезпечте, щоб додаток запускався на порту 3000 і був готовий до збірки в Docker.
#
# Вимоги:
# • Dockerfile повинен використовувати образ Node.js як базовий для запуску React-додатку.
# • Dockerfile повинен включати команди для встановлення всіх необхідних залежностей React-додатку з використанням пакетного менеджера npm або yarn.
# • Dockerfile повинен забезпечити, щоб додаток працював на порту 3000, включаючи відповідну команду EXPOSE.
# • Dockerfile повинен містити команду для запуску React-додатку, зазвичай це команда npm start або аналогічна.
# • Dockerfile повинен бути коректно складений і включати всі необхідні кроки для успішної збірки і запуску контейнера з React-додатком.

# Step 1: Specify the base image
FROM node:22.22.3-alpine3.23

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the package.json and package-lock.json files into the container
COPY package*.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy all project files into the container
COPY . .

# Step 6: Build the React application
RUN npm run build

# Step 7: Specify the port on which the application will run
EXPOSE 3000

# Step 8: Run the application
CMD ["npm", "start"]