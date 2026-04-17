# Using a minimal Python base image
FROM python:3.9-alpine

# Setting the working directory
WORKDIR /app

# Copying the application file into the container (it will differ for each version)
COPY app.py /app/app.py

# Command to run the application
CMD ["python", "app.py"]