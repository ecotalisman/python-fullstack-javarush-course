# Using the base Python image
FROM python:3.9-slim

# Configuring environment variables for each stage
# These variables can be changed during the build using arguments
ARG ENVIRONMENT
ENV MY_ENVIRONMENT=${ENVIRONMENT}

# Adding the application file to the container
COPY app.py /app.py

# Setting the working directory
WORKDIR /

# Running the application
CMD ["python", "app.py"]