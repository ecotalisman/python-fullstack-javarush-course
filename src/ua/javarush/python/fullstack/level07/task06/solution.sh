# Using the docker stats Command to Monitor All Containers
# Start several containers, for example Nginx and Postgres,
# then use the docker stats command to monitor their operation.
# Determine which container consumes the most memory and CPU.
#
# Requirements:
# • Several containers, including Nginx and Postgres, must be started
#   for further monitoring of their operation.
# • The docker stats command must be used to get statistics
#   about resource consumption by the running containers.
# • It is necessary to visually determine which of the running containers
#   consumes the most memory and CPU based on the data obtained
#   using docker stats.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання команди docker stats для моніторингу всіх контейнерів
# Запустіть кілька контейнерів (наприклад, Nginx і Postgres),
# потім використовуйте команду docker stats, щоб моніторити їхню роботу.
# Визначте, який контейнер споживає найбільше пам'яті та CPU.
#
# Вимоги:
# • Необхідно запустити кілька контейнерів, включаючи Nginx і Postgres,
#   для подальшого моніторингу їхньої роботи.
# • Потрібно використати команду docker stats для отримання статистики
#   про споживання ресурсів запущеними контейнерами.
# • Необхідно візуально визначити, який із запущених контейнерів
#   споживає найбільше пам'яті та CPU на основі даних,
#   отриманих за допомогою docker stats.

# Starting a container with Nginx
docker run -d --name web nginx

# Starting a container with PostgreSQL
docker run -d --name db -e POSTRES_PASSWORD=mysecretpassword postgres

# Monitoring CPU and memory usage
docker stats