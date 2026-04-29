# Creating and Using a Volume
# Create a volume named website_data and run a container with Nginx,
# mounting this volume into the /usr/share/nginx/html directory.
# The container must use this volume to store website data.
#
# Requirements:
# • A Docker volume named website_data must be created.
# • The Nginx container must be started using the website_data volume.
# • The website_data volume must be mounted into the /usr/share/nginx/html directory inside the container.
# • The container must use the volume to store website data.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення та використання тому
# Створіть том з іменем website_data і запустіть контейнер з Nginx,
# монтувавши цей том у директорію /usr/share/nginx/html.
# Контейнер повинен використовувати цей том для зберігання даних веб-сайту.
#
# Вимоги:
# • Необхідно створити Docker том з іменем website_data.
# • Контейнер з Nginx повинен бути запущений із використанням тому website_data.
# • Том website_data повинен бути змонтований у директорію /usr/share/nginx/html всередині контейнера.
# • Контейнер повинен використовувати том для зберігання даних веб-сайту.

# Create a volume named website_data for storing website data
docker volume create website_data

# Run a container with Nginx, mounting the website_data volume
# into the /usr/share/nginx/html directory inside the container
docker run -d --name web -v website_data:/usr/share/nginx/html nginx