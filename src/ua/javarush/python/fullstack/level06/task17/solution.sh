# Mounting a Configuration File
# Create an Nginx configuration file on the host and mount it into the Nginx container.
# The container must use this configuration file.
#
# Requirements:
# • An Nginx configuration file must be created on the host machine,
#   containing the required settings for the web server.
# • The Nginx configuration file created on the host must be correctly mounted
#   into the Nginx container.
# • The Nginx container must use the mounted configuration file
#   instead of the default configuration file.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування конфігураційного файлу
# Створіть файл конфігурації Nginx на хості та змонтуйте його в контейнер Nginx.
# Контейнер повинен використовувати цей файл конфігурації.
#
# Вимоги:
# • На хостовій машині повинен бути створений файл конфігурації Nginx,
#   що містить необхідні параметри для вебсервера.
# • Файл конфігурації Nginx, створений на хості, повинен бути коректно змонтований
#   у контейнер Nginx.
# • Контейнер Nginx повинен використовувати змонтований файл конфігурації
#   замість стандартного файлу конфігурації.

# Run a container with Nginx, mounting the configuration file into the container
docker run -d --name nginx_custom -v $(pwd)/host/nginx.conf:/etc/nginx/nginx.conf nginx