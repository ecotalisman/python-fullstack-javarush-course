# Creating and Using an Nginx Configuration
# Create an Nginx configuration file on the host
# and add it as a Docker configuration using the docker config create command.
# Then create an Nginx service that will use this configuration.
#
# Requirements:
# • An Nginx configuration file with the required settings must be created on the host.
# • The Nginx configuration file must be added to Docker as a configuration
#   using the docker config create command.
# • An Nginx service must be created that will use the previously created configuration.
# • The Nginx service must be configured so that it uses the added Docker configuration.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення та використання конфігурації Nginx
# Створіть конфігураційний файл Nginx на хості
# та додайте його як конфігурацію в Docker за допомогою команди docker config create.
# Потім створіть сервіс Nginx, який буде використовувати цю конфігурацію.
#
# Вимоги:
# • На хості має бути створений конфігураційний файл Nginx з необхідними налаштуваннями.
# • Конфігураційний файл Nginx має бути доданий у Docker як конфігурація за допомогою команди docker config create.
# • Необхідно створити сервіс Nginx, який буде використовувати створену раніше конфігурацію.
# • Сервіс Nginx має бути налаштований так, щоб він використовував додану конфігурацію з Docker.

# Create a configuration in Docker using the docker config create command
docker config create nginx_config ./nginx.conf

# Create an Nginx service that will use this configuration
docker service create --name nginx --config source=nginx_config,target=/etc/nginx/nginx.conf nginx