# Publishing Your Own Image to Docker Hub
# Write a Dockerfile for a simple Python application that outputs "Hello, Docker!". Build this image, assign it a tag with your Docker Hub username, and publish it to a Docker Hub repository.
#
# Requirements:
# • It is necessary to create a Dockerfile that describes the image build process for a Python application that outputs "Hello, Docker!".
# • The image must be built based on the created Dockerfile and must run the application correctly when the container starts.
# • The image must be tagged with a tag that includes the Docker Hub username for identification during publishing.
# • The built and tagged image must be published to your Docker Hub repository for public access.
#
# ## 🇺🇦 Ukrainian version:
# Публікація власного образу в Docker Hub
# Напишіть Dockerfile для простого Python-додатка, який виводить "Hello, Docker!". Зберіть цей образ, присвойте йому тег з вашим ім'ям користувача Docker Hub і опублікуйте його в репозиторії Docker Hub.
#
# Вимоги:
# • Необхідно створити Dockerfile, що описує процес збирання образу для Python-додатка, який виводить "Hello, Docker!".
# • Образ має бути зібраний на основі створеного Dockerfile і повинен коректно виконувати додаток при запуску контейнера.
# • Образ має бути помічений тегом, який включає ім'я користувача Docker Hub, для ідентифікації при публікації.
# • Зібраний і позначений образ необхідно опублікувати у вашому репозиторії на Docker Hub для загального доступу.

# Building the Docker image with your Docker Hub username:
docker build -t app:1.0 .

# Logging in to Docker Hub:
docker tag app:1.0 username/app:1.0

# Publishing the image to Docker Hub:
docker push username/app:1.0