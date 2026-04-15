# Using the official Node.js image
FROM node:latest

# Creating a working directory
WORKDIR /app

# Copying package.json and package-lock.json
COPY package.json ./

# Installing dependencies
RUN npm install

# Copying the rest of the application
COPY app.js ./

# The container will listen on port 4000
EXPOSE 4000

# Command to start the application
CMD ["node", "app.js"]