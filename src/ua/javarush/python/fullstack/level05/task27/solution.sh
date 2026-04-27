# Checking Connectivity Between Services
# Create two services in Docker Swarm: an Nginx web server and a PostgreSQL database.
# Both services must be connected to the previously created overlay network my_overlay_network.
#
# After creating the services, check connectivity between them inside the overlay network.
# Run a BusyBox container, connect it to the overlay network, and execute the ping command
# to check the availability of the web server and the database by their hostnames.
#
# Requirements:
# • Create an overlay network to which all required services will be connected,
#   including the web server and the database.
# • Run the web server and the database as separate services connected to the created overlay network.
# • Run a BusyBox container and connect it to the same overlay network as the web server and database
#   for further availability checks.
# • From the BusyBox container, execute the `ping` command to check the availability
#   of the web server by its hostname.
# • From the BusyBox container, execute the `ping` command to check the availability
#   of the database by its hostname.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка зв'язку між сервісами
# Створіть два сервіси у Docker Swarm: веб-сервер Nginx і базу даних PostgreSQL.
# Обидва сервіси мають бути підключені до раніше створеної overlay мережі my_overlay_network.
#
# Після створення сервісів, перевірте зв'язок між ними всередині overlay мережі.
# Запустіть контейнер BusyBox, підключіть його до overlay мережі та виконайте команду ping
# для перевірки доступності веб-сервера та бази даних за їх іменами хостів.
#
# Вимоги:
# • Створіть overlay мережу, до якої будуть підключені всі необхідні сервіси, включаючи веб-сервер і базу даних.
# • Запустіть веб-сервер і базу даних як окремі сервіси, підключені до створеної overlay мережі.
# • Запустіть контейнер BusyBox і підключіть його до тієї ж overlay мережі, що і веб-сервер та база даних, для подальшої перевірки доступності.
# • З контейнера BusyBox виконайте команду `ping`, щоб перевірити доступність веб-сервера за ім'ям його хоста.
# • З контейнера BusyBox виконайте команду `ping`, щоб перевірити доступність бази даних за ім'ям її хоста.

# Initializing Docker Swarm
docker swarm init

# Creating an overlay network for communication between services
docker network create -d overlay --attachable my_overlay_network

# Creating the Nginx web server service, connecting it to the overlay network,
# and publishing port 80 to host port 8080
docker service create --name web_server --network my_overlay_network -p 8080:80 nginx

# Creating the PostgreSQL database service, connecting it to the overlay network,
# and setting the password for the default database superuser
docker service create --name postgres_db --network my_overlay_network -e POSTGRES_PASSWORD=mypassword postgres:latest

# Checking the availability of the web server using ping through a BusyBox container
docker run -d --name tester --network my_overlay_network busybox sleep 1000
docker exec tester ping -c 4 web_server

# Checking the availability of the database using ping through a BusyBox container
docker exec tester ping -c 4 postgres_db