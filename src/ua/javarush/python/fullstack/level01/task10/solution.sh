# Working with Docker Images
# Perform the following actions:
#
# 1. Pull the nginx image with the latest tag from Docker Hub.
# 2. Build an image from the Dockerfile located in the current directory and assign it the tag my_custom_image.
# 3. Display the list of local images.
# 4. Remove the my_custom_image image.
#
# Requirements:
# • Pull the nginx image with the latest tag from Docker Hub.
# • Build an image from the Dockerfile located in the current directory and assign it the tag my_custom_image.
# • Display the list of all local Docker images.
# • Remove the image with the tag my_custom_image from the list of local images.
#
# ## 🇺🇦 Ukrainian version:
#
# Робота з образами Docker
# Виконайте наступні дії:
#
# 1. Завантажте образ nginx з тегом latest із Docker Hub.
# 2. Зберіть образ із Dockerfile, який знаходиться в поточному каталозі, та призначте йому тег my_custom_image.
# 3. Виведіть список локальних образів.
# 4. Видаліть образ my_custom_image.
#
# Вимоги:
# • Завантажте образ nginx з тегом latest із Docker Hub.
# • Зберіть (build) образ із Dockerfile, який знаходиться в поточному каталозі, та призначте йому тег my_custom_image.
# • Виведіть список усіх локальних образів Docker.
# • Видаліть образ із тегом my_custom_image зі списку локальних образів.

# Pulling the nginx image with the latest tag from Docker Hub
docker pull nginx:latest

# Building an image from the Dockerfile in the current directory with the tag my_custom_image
docker build -t my_custom_image .

# Displaying the list of local Docker images
docker images

# Removing the my_custom_image image
docker rmi my_custom_image