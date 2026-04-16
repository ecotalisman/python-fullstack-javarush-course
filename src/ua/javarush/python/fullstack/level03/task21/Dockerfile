# Using the minimal Alpine base image
FROM python:alpine

# Installing updates and python3
RUN apk add --no-cache python3-dev && \
    pip install --upgrade pip

# Creating the working directory
WORKDIR /app

# Copying the application source code into the container
COPY . .

# Command to run the Python application
CMD ["python3", "app.py"]