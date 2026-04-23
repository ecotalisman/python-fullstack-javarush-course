# Using Multiple Environments
# Create two .env files for development and production.
# Run the project using each file.
#
# Requirements:
# • Two separate .env files must be created, one for development and one for production.
# • The .env file for development must contain the variables: `NGINX_VERSION=latest` and `HOST_PORT=8080`.
# • The .env file for production must contain the variables: `NGINX_VERSION=1.19.3` and `HOST_PORT=80`.
# • The project must be run twice, once with each .env file to use the corresponding environment variables.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання декількох оточень
# Створіть два файли .env для розробки та продакшену.
# Запустіть проєкт із використанням кожного файлу.
#
# Вимоги:
# • Мають бути створені два окремі файли .env, один для розробки та один для продакшену.
# • Файл .env для розробки повинен містити змінні: `NGINX_VERSION=latest` і `HOST_PORT=8080`.
# • Файл .env для продакшену повинен містити змінні: `NGINX_VERSION=1.19.3` і `HOST_PORT=80`.
# • Проєкт має бути запущений двічі, один раз із кожним файлом .env для використання відповідних змінних оточення.

# Running for development
docker compose --env-file .env.development up

# Running for production
docker compose --env-file .env.production up