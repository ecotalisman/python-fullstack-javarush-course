# Using Multi-Stage Build with FROM and COPY
# Create a multi-stage Dockerfile for a React application.
# The first stage must use the node:14 image to build the application,
# and the second stage must use nginx:alpine to host the static files.
# The built files must be copied into the Nginx directory.
#
# Requirements:
# • The Dockerfile must use the node:14 image in the first stage to build the React application.
# • In the first stage, all necessary commands must be executed to install dependencies and build the React application.
# • The Dockerfile must use the nginx:alpine image in the second stage to host the static files of the application.
# • The built static files of the React application must be copied from the first stage to the second stage
#   into the appropriate Nginx directory.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання багатостадійної збірки з FROM і COPY
# Створіть багатостадійний Dockerfile для React-додатка.
# Перший етап повинен використовувати образ node:14 для збірки додатка,
# другий — nginx:alpine для хостингу статичних файлів.
# Зібрані файли повинні бути скопійовані в директорію Nginx.
#
# Вимоги:
# • Dockerfile повинен використовувати образ node:14 на першому етапі для збірки React-додатка.
# • На першому етапі повинні бути виконані всі необхідні команди для встановлення залежностей і збірки React-додатка.
# • Dockerfile повинен використовувати образ nginx:alpine на другому етапі для хостингу статичних файлів додатка.
# • Зібрані статичні файли React-додатка повинні бути скопійовані з першого етапу на другий етап
#   у відповідну директорію Nginx.

# First stage: building the React application
FROM node:14 as build

WORKDIR /app

# Installing dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copying the source code and building the Node.js application
COPY . .
RUN npm run build

# Second stage: configuring Nginx to host static files
FROM nginx:alpine

# Copying the build files from the first stage into the Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Nginx configuration
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]