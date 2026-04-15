# Using the Alpine base image
FROM alpine:latest

# Defining the build argument
ARG APP_VERSION

# Setting the environment variable using the value of the build argument
ENV MY_VERSION=${APP_VERSION}

# A simple command to check the version
CMD echo "Application version: $MY_VERSION"