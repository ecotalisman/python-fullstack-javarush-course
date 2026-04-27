# Deploying a Stack Using an overlay Network
# Create a docker-compose.yml file that describes two services:
# an Nginx-based web server and a PostgreSQL database.
# Both services must be connected to an overlay network named my_overlay_network.
# Use Docker Compose to deploy these services in Docker Swarm.
#
# Requirements:
# • A file named docker-compose.yml must be created,
#   containing the configuration for two services.
# • The docker-compose.yml file must include a definition
#   for the web server service that uses the Nginx image.
# • The docker-compose.yml file must include a definition
#   for the database service that uses the PostgreSQL image.
# • Both services, the web server and the database,
#   must be connected to the overlay network named my_overlay_network.
# • Docker Compose must be used to deploy the services in Docker Swarm.
#
# ## 🇺🇦 Ukrainian version:
#
# Розгортання стека з використанням overlay мережі
# Створіть файл docker-compose.yml, у якому будуть описані два сервіси:
# вебсервер на базі Nginx і база даних PostgreSQL.
# Обидва сервіси мають бути підключені до overlay мережі з іменем my_overlay_network.
# Використовуйте Docker Compose для розгортання цих сервісів у Docker Swarm.
#
# Вимоги:
# • Необхідно створити файл з ім'ям docker-compose.yml, у якому буде описана конфігурація для двох сервісів.
# • Файл docker-compose.yml має включати опис сервісу вебсервера, що використовує образ Nginx.
# • Файл docker-compose.yml має включати опис сервісу бази даних, що використовує образ PostgreSQL.
# • Обидва сервіси, вебсервер і база даних, мають бути підключені до overlay мережі з іменем my_overlay_network.
# • Для розгортання сервісів у Docker Swarm необхідно використовувати Docker Compose.

# Initializing Docker Swarm
docker swarm init

# Creating the network
docker network create -d overlay my_overlay_network

# Deploying the stack using Docker Compose
docker stack deploy -c docker-compose.yml my_stack

# Checking the deployed services
docker stack services my_stack