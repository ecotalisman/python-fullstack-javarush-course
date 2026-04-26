# Creating and Checking a bridge Network
# Create a custom bridge network named my_bridge_network.
# Then start two containers: one with Nginx and another with BusyBox.
# Both containers must be connected to this network.
# Check connectivity between them using the ping command.
#
# Requirements:
# • A custom bridge network named my_bridge_network must be created.
# • A container with Nginx connected to the my_bridge_network network must be started.
# • A container with BusyBox connected to the my_bridge_network network must be started.
# • Connectivity between the containers must be checked using the ping command,
#   confirming that both containers are connected to the same network.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення та перевірка bridge мережі
# Створіть користувацьку мережу типу bridge з іменем my_bridge_network.
# Потім запустіть два контейнери: один з Nginx, інший з Busybox.
# Обидва контейнери повинні бути підключені до цієї мережі.
# Перевірте зв'язок між ними за допомогою команди ping.
#
# Вимоги:
# • Повинна бути створена користувацька мережа типу bridge з іменем my_bridge_network.
# • Необхідно запустити контейнер з Nginx, який підключений до мережі my_bridge_network.
# • Необхідно запустити контейнер з Busybox, який підключений до мережі my_bridge_network.
# • Зв'язок між контейнерами повинен бути перевірений за допомогою команди ping, підтверджуючи, що обидва контейнери підключені до однієї мережі.

# Creating a custom bridge network named my_bridge_network
docker network create --driver bridge my_bridge_network

# Starting a container with Nginx and connecting it to my_bridge_network
docker run -d --name webserver --network my_bridge_network nginx

# Starting a container with BusyBox and connecting it to my_bridge_network
docker run -d --name appserver --network my_bridge_network busybox sleep 1000

# Checking connectivity between containers using the ping command
docker exec appserver ping -c 4 webserver