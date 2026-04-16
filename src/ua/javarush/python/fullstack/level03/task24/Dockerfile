# Multi-Stage Build to Reduce the Final Image Size
# Use a multi-stage build to create a final image that contains only the build results.
# Build an image for a React application, using node for the build stage and nginx for deployment.
#
# Requirements:
# • The Dockerfile must be written using a multi-stage build to reduce the size of the final image by separating the build stage from the deployment stage.
# • In the first stage of the multi-stage build, use the Node.js image to install dependencies and build the React application.
# • In the final stage of the multi-stage build, use the Nginx image to configure and deploy the prebuilt React application.
#
# ## 🇺🇦 Ukrainian version:
#
# Багатостадійна збірка для зменшення фінального образу
# Використовуйте багатостадійну збірку для створення фінального образу, який буде містити лише результати збірки.
# Побудуйте образ для React-додатка, використовуючи node для збірки і nginx для розгортання.
#
# Вимоги:
# • Dockerfile має бути написаний з використанням багатостадійної збірки, щоб зменшити розмір фінального образу за рахунок розділення етапу збірки від етапу розгортання.
# • На першому етапі багатостадійної збірки використовуйте образ Node.js для встановлення залежностей і збірки React-додатка.
# • На фінальному етапі багатостадійної збірки використовуйте образ Nginx для налаштування і розгортання заздалегідь зібраного React-додатка.

# Stage 1: Building the React application
FROM node AS builder

WORKDIR /app

# Copying the package.json and package-lock.json files
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the rest of the application source code
COPY . .

# Building the React application
RUN npm run build

# Stage 2: Serving the application with Nginx
FROM nginx

# Copying the built React application from the previous stage
COPY --from=builder /app/build /usr/share/nginx/html

# Exposing port 80
EXPOSE 80

# Starting Nginx
CMD ["nginx", "-g", "daemon off;"]