# Using the Node.js base image
FROM node

# Setting the working directory
WORKDIR /usr/src/app

# Copying package.json and package-lock.json
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the application source code
COPY . .

# Exposing the port on which the application will run
EXPOSE 4000

# Defining the command to start the application
CMD ["node", "app.js"]