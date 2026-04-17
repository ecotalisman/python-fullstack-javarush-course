# Updating and Republishing an Image to Docker Hub
# You have a Node.js application image published on Docker Hub under the tag yourusername/mynodeapp:1.0. Update the Dockerfile to add the new text "App updated", build the updated image, and publish it as yourusername/mynodeapp:2.0.
#
# Requirements:
# • The Dockerfile must be modified to add the new text message "App updated".
# • Use the updated Dockerfile to build a new Node.js application image with the tag yourusername/mynodeapp:2.0.
# • The image with the tag yourusername/mynodeapp:2.0 must be published to Docker Hub.
#
# ## 🇺🇦 Ukrainian version:
# Оновлення та повторна публікація образу в Docker Hub
# У вас є образ застосунку Node.js, опублікований у Docker Hub під тегом yourusername/mynodeapp:1.0. Оновіть Dockerfile, щоб додати новий текст "App updated", зберіть оновлений образ і опублікуйте його як yourusername/mynodeapp:2.0.
#
# Вимоги:
# • Dockerfile має бути змінено для додавання нового текстового повідомлення "App updated".
# • Використовуйте оновлений Dockerfile для збирання нового образу застосунку Node.js з тегом yourusername/mynodeapp:2.0.
# • Образ з тегом yourusername/mynodeapp:2.0 має бути опублікований у Docker Hub.

# Building the updated image
docker build -t yourusername/mynodeapp:2.0 .

# Authenticating with Docker Hub (this will require entering credentials)
docker tag mynodeapp:2.0 yourusername/mynodeapp:2.0

# Publishing the image to Docker Hub
docker login
docker push yourusername/mynodeapp:2.0