# Using .dockerignore to Reduce the Build Context
# Create a Dockerfile for a Node.js application that copies all project files into the container.
# To reduce the size of the build context, add a .dockerignore file to exclude the node_modules and dist directories,
# as well as files with the .log extension.
#
# Requirements:
# • A Dockerfile must be created for the Node.js application and include commands to copy all necessary project files into the container.
# • A .dockerignore file must be created to exclude the node_modules and dist directories, as well as files with the .log extension, from the build context.
# • The .dockerignore file must work correctly by excluding the specified directories and files to reduce the size of the build context.
# • The Dockerfile and .dockerignore must be configured in such a way as to avoid build errors related to missing required files.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання .dockerignore для зменшення контексту збірки
# Створіть Dockerfile для Node.js застосунку, який копіює всі файли проєкту в контейнер.
# Для зменшення розміру контексту збірки додайте файл .dockerignore, щоб виключити каталоги node_modules, dist,
# і файли з розширенням .log.
#
# Вимоги:
# • Dockerfile має бути створений для Node.js застосунку і включати команди для копіювання всіх необхідних файлів проєкту в контейнер.
# • Повинен бути створений файл .dockerignore, який виключає каталоги node_modules і dist, а також файли з розширенням .log з контексту збірки.
# • Файл .dockerignore має коректно працювати, виключаючи зазначені каталоги і файли, щоб зменшити розмір контексту збірки.
# • Dockerfile та .dockerignore повинні бути налаштовані таким чином, щоб уникнути помилок під час збірки образу, пов'язаних із відсутністю необхідних файлів.

# Using the official Node.js image as the base image
FROM node:14

# Setting the working directory inside the container
WORKDIR /usr/src/app

# Copying package.json and package-lock.json to install dependencies
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the other project files
COPY . .

# Specifying the command to run the application
CMD ["npm", "start"]

