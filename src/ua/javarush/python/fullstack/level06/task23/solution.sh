# Removing a Configuration and a Secret
# Remove the configuration and secret from Docker after they are no longer used.
# The corresponding services must be stopped.
#
# Requirements:
# • The Docker configuration must be removed after it is no longer used
#   in any containers or services.
# • The Docker secret must be removed after it is no longer used
#   in any containers or services.
# • All services that use this configuration or secret must be stopped
#   before they are removed.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення конфігурації та секрету
# Видаліть конфігурацію та секрет із Docker після того, як вони більше не використовуються.
# Відповідні сервіси повинні бути зупинені.
#
# Вимоги:
# • Конфігурація Docker повинна бути видалена після того, як вона більше не використовується
#   в яких-небудь контейнерах або сервісах.
# • Секрет Docker повинен бути видалений після того, як він більше не використовується
#   в яких-небудь контейнерах або сервісах.
# • Усі сервіси, які використовують дану конфігурацію або секрет,
#   повинні бути зупинені перед їх видаленням.

# Stop and remove the Nginx service
docker service rm nginx_service

# Remove the Nginx configuration, for example nginx_config_v1 and nginx_config_v2
docker config rm nginx_config_v1 nginx_config_v2

# Remove the PostgreSQL database secret, for example postgres_password
docker secret rm postgres_password

# Check that the configurations and secrets have been removed
docker config ls
docker secret ls
docker service ls