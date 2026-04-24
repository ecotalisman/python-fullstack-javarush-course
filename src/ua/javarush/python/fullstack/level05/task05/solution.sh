# Creating a bridge Network
# Create a new network with the bridge driver named my_bridge_network.
# Start two containers — one with Nginx and the other with Redis —
# and connect them to this network.
#
# Requirements:
# • A new network must be created using the bridge driver and assigned the name my_bridge_network.
# • A container with the Nginx image must be started and connected to the my_bridge_network network.
# • A container with the Redis image must be started and connected to the my_bridge_network network.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення bridge-мережі
# Створіть нову мережу з драйвером bridge, яка буде називатися my_bridge_network.
# Запустіть два контейнери — один з Nginx і інший з Redis — та підключіть їх до цієї мережі.
#
# Вимоги:
# • Необхідно створити нову мережу з використанням драйвера bridge, присвоївши їй ім'я my_bridge_network.
# • Необхідно запустити контейнер з образом Nginx і підключити його до мережі my_bridge_network.
# • Необхідно запустити контейнер з образом Redis і підключити його до мережі my_bridge_network.

# Creating a new network with the bridge driver
docker network create -d bridge my_bridge_network

# Starting a container with Nginx and connecting it to the network
docker run -d --name nginx_container --network my_bridge_network nginx

# Starting a container with Redis and connecting it to the network
docker run -d --name redis_container --network my_bridge_network redis

# Checking that the containers are working in the network
docker network inspect my_bridge_network