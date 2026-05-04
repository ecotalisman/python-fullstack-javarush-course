# Using the official Python runtime as the parent image
FROM python:3.8-slim

# Setting the working directory in the container to /app
WORKDIR /app

# Copying the contents of the current directory into the container at /app
COPY . /app

# Running the application
CMD ["python", "disk_io_application.py"]