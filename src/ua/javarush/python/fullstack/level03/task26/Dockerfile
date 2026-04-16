# Using the ubuntu:20.04 image as the base image
FROM ubuntu:20.04

# Updating packages and installing Python
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Creating a directory for the application
WORKDIR /app

# Copying the Python application to the working directory
COPY . /app

# Command to run the application
CMD ["python3", "app.py"]