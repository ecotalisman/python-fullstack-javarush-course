# Using the official Node.js image as the base image
FROM node:14

# Setting the working directory inside the container
WORKDIR /app

# Copying package.json and yarn.lock into the container
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the contents of the current directory into the container
COPY . .

# Specifying the command to run the application
CMD ["node", "app.js"]