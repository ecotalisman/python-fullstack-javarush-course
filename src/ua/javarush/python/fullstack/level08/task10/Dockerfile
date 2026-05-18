# Dockerfile for a Flask Backend
# Create a Dockerfile for the Python backend service using Flask.
# The Flask application must run through the run.py file and work on port 5000.
#
# Requirements:
# • The Dockerfile must be created to containerize the Python Flask application.
# • The Dockerfile must use a base image for Python.
# • The Dockerfile must copy the run.py file into the container.
# • The Flask application must be started using the run.py file.
# • The application must be configured to work on port 5000.
#
# 🇺🇦 Ukrainian version:
#
# Dockerfile для Flask-бекенда
# Створіть Dockerfile для бекенд-сервісу на Python (Flask). Flask-додаток має запускатися через файл run.py і працювати на порту 5000.
#
# Вимоги:
# • Dockerfile має бути створений для контейнеризації Flask-додатку на Python.
# • Dockerfile має використовувати базове зображення для Python.
# • Dockerfile має копіювати файл run.py у контейнер.
# • Flask-додаток має запускатися з використанням файлу run.py.
# • Додаток має бути налаштований для роботи на порту 5000.

# Specify the base image for Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the run.py file into the container
COPY run.py /app/

# Install the required packages for Flask
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the Flask application
CMD ["python", "run.py"]

# Configure the port for the application to work
EXPOSE 5000