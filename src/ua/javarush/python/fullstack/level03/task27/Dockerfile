# First stage: building the React application
FROM node:14 AS builder

# Setting the working directory
WORKDIR /app

# Copying package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Installing dependencies
RUN npm install

# Copying the entire project source code
COPY . .

# Building the application
RUN npm run build

# Second stage: deployment using nginx
FROM nginx:alpine

# Copying the built application from the first stage
COPY --from=builder /app/build /usr/share/nginx/html

# Ports that will be used for running the application
EXPOSE 80

# Starting Nginx
CMD ["nginx", "-g", "daemon off;"]