# Using the base Node.js image
FROM node:14

# Setting the directory for the application
WORKDIR /usr/src/app

# Copying package.json and package-lock.json
COPY package*.json ./

# Installing dependencies
RUN npm install

# Copying the application source code
COPY . .

# Adding a new text message
RUN echo "App updated" > updated.txt

# Exposing the application port
EXPOSE 8080

# Defining the command to run the application
CMD ["node", "app.js"]