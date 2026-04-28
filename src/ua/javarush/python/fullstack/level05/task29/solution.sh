# Checking Connectivity Between Containers
# You have two containers, web and db, connected to the same network webnet.
# Using the ping utility, check whether the containers can communicate with each other inside the network.
#
# Requirements:
# • A network named webnet must be created, to which both containers, web and db, will be connected.
# • Both containers, web and db, must be connected to the same webnet network to enable communication.
# • The ping utility must be used inside the web container to check connectivity with the db container through the webnet network.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка підключення між контейнерами
# У вас є два контейнери, web та db, підключені до однієї мережі webnet.
# Використовуючи утиліту ping, перевірте, чи можуть контейнери взаємодіяти між собою всередині мережі.
#
# Вимоги:
# • Необхідно створити мережу з іменем webnet, до якої будуть підключені обидва контейнери: web і db.
# • Обидва контейнери, web і db, повинні бути підключені до однієї й тієї ж мережі webnet для можливості взаємодії.
# • Використати утиліту ping всередині контейнера web для перевірки можливості взаємодії з контейнером db через мережу webnet.

# Creating the network
docker network create webnet

# Running the web container with Nginx, connected to the webnet network
docker run -d --name web --network webnet nginx

# Running the db container with PostgreSQL, connected to the webnet network
docker run -d --name db --network webnet postgres

# Checking connectivity using ping
docker exec -it web ping db