# Updating the Nginx Configuration
# Update the Nginx configuration file on the host and create a new version
# of the configuration in Docker. Then update the existing Nginx service
# to use the new configuration.
#
# Requirements:
# • The Nginx configuration file on the host must be changed according to the new requirements.
# • A new version of the Nginx configuration file must be created in Docker,
#   reflecting the changes made on the host.
# • The existing Nginx service in Docker must be updated
#   to use the new version of the configuration file.
#
# ## 🇺🇦 Ukrainian version:
#
# Оновлення конфігурації Nginx
# Оновіть конфігураційний файл Nginx на хості
# та створіть нову версію конфігурації в Docker.
# Потім оновіть існуючий сервіс Nginx для використання нової конфігурації.
#
# Вимоги:
# • Конфігураційний файл Nginx на хості має бути змінений відповідно до нових вимог.
# • Необхідно створити нову версію конфігураційного файлу Nginx у Docker,
#   яка відображає зміни, зроблені на хості.
# • Існуючий сервіс Nginx у Docker має бути оновлений
#   для використання нової версії конфігураційного файлу.

# Creating the nginx_config_v1 configuration in Docker
docker config create nginx_config_v1 nginx-v1.conf

# Creating an Nginx service using the nginx_config_v1 configuration
docker service create --name nginx_service \
  --config source=nginx_config_v1,target=/etc/nginx/nginx.conf \
  --publish 8080:80 \
  nginx


# Create a new version of the configuration in Docker
docker config create nginx_config_v2 nginx-v2.conf

# Update the existing Nginx service to use the new configuration
docker service update \
  --config-rm nginx_config_v1 \
  --config-add source=nginx_config_v2,target=/etc/nginx/nginx.conf \
  nginx_service