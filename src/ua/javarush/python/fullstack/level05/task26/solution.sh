# Creating Services in an overlay Network
# Create two services in Docker Swarm: an Nginx web server and a PostgreSQL database.
# Both services must be connected to the previously created overlay network my_overlay_network.
# The web server must publish port 80 to host port 8080,
# and the database must have the password mypassword set.
#
# Requirements:
# • Both services must be connected to the existing overlay network named my_overlay_network.
# • The Nginx web server must be configured so that port 80 inside the container
#   is published to host port 8080.
# • The PostgreSQL database service must be configured with the password mypassword
#   for database access.
# • Both services, Nginx and PostgreSQL, must be deployed in the Docker Swarm environment.
# • Port 80 of the Nginx web server inside the container must be accessible on host port 8080.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення сервісів в overlay мережі
# Створіть два сервіси в Docker Swarm: веб-сервер Nginx і базу даних PostgreSQL.
# Обидва сервіси мають бути підключені до раніше створеної overlay мережі my_overlay_network.
# Веб-сервер має публікувати порт 80 на 8080 хоста, а для бази даних потрібно встановити пароль mypassword.
#
# Вимоги:
# • Обидва сервіси мають бути підключені до вже існуючої overlay мережі з іменем my_overlay_network.
# • Веб-сервер Nginx має бути налаштований таким чином, щоб порт 80 всередині контейнера був опублікований на порт 8080 хоста.
# • Сервіс бази даних PostgreSQL має бути сконфігурований з паролем mypassword для доступу до бази даних.
# • Обидва сервіси, Nginx і PostgreSQL, мають бути розгорнуті в середовищі Docker Swarm.
# • Порт 80 веб-сервера Nginx всередині контейнера має бути доступним на порту 8080 хоста.

# Initializing Docker Swarm
docker swarm init

# Creating an overlay network for communication between services
docker network create -d overlay my_overlay_network

# Creating the Nginx web server service, connecting it to the overlay network,
# and publishing port 80 to host port 8080
docker service create --name webserver --network my_overlay_network -p 8080:80 nginx

# Creating the PostgreSQL database service, connecting it to the overlay network,
# and setting the password for the root user
docker service create --name database --network my_overlay_network -e POSTGRES_PASSWORD=mypassword postgres