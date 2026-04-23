# Passing Variables via the Command Line
# Start Docker Compose by passing the values of the NGINX_VERSION and HOST_PORT variables
# through the command line using the export command.
#
# Requirements:
# • The NGINX_VERSION variable must be set using the `export` command in the command line before starting Docker Compose.
# • The HOST_PORT variable must be set using the `export` command in the command line before starting Docker Compose.
# • Docker Compose must be started after setting the NGINX_VERSION and HOST_PORT variables,
#   which will allow their values to be used during the container deployment process.
#
# ## 🇺🇦 Ukrainian version:
#
# Передача змінних через команду
# Запустіть Docker Compose, передавши значення змінних NGINX_VERSION та HOST_PORT
# через командний рядок за допомогою команди export.
#
# Вимоги:
# • Змінна NGINX_VERSION має бути встановлена з використанням команди `export`
#   у командному рядку перед запуском Docker Compose.
# • Змінна HOST_PORT має бути встановлена з використанням команди `export`
#   у командному рядку перед запуском Docker Compose.
# • Docker Compose має бути запущений після встановлення змінних NGINX_VERSION та HOST_PORT,
#   що дозволить використовувати їх значення в процесі розгортання контейнерів.

# Set the required environment variables using the `export` command:
export NGINX_VERSION=latest
export HOST_PORT=8080

# After setting the variables, start Docker Compose:
docker compose up