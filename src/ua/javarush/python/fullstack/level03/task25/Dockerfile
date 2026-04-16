# Using the minimal Alpine base image
FROM alpine:3.12

# Installing Python
RUN apk add --no-cache python3 py3-pip

# Setting the working directory
WORKDIR /app

# Copying the Python application into the container
COPY app.py /app/app.py

# Command to run the application
CMD ["python3", "app.py"]