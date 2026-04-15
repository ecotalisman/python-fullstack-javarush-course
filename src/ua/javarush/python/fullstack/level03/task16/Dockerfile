# First stage: building the React application
FROM node AS build

# Setting the working directory
WORKDIR /app

# Copying package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Installing dependencies
RUN npm install

# Copying the remaining application source files into the container
COPY . .

# Building the application
RUN npm run build

# Second stage: creating an Nginx-based server to serve static files
FROM nginx

# Copying the build files into the Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Exposing the port used by the container
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]