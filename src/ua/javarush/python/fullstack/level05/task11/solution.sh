# Creating a Custom Network
# Create a custom network with the bridge driver and start two containers:
# one with Nginx and another with BusyBox.
# Both containers must be connected to this network.
# There must be connectivity between them by hostname.
#
# Requirements:
# • The script must create a custom network using the bridge driver.
# • The script must start a container with Nginx connected to the created custom network.
# • The script must start a container with BusyBox also connected to the created custom network.
# • The Nginx and BusyBox containers must be able to communicate with each other by hostname
#   within the created network.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення користувацької мережі
# Створіть користувацьку мережу з драйвером bridge та запустіть два контейнери:
# один з Nginx та інший з Busybox.
# Обидва контейнери повинні бути підключені до цієї мережі.
# Між ними має бути зв'язок за іменем хоста.
#
# Вимоги:
# • Скрипт повинен створити користувацьку мережу з використанням драйвера bridge.
# • Скрипт повинен запустити контейнер з Nginx, який підключений до створеної користувацької мережі.
# • Скрипт повинен запустити контейнер з Busybox, який також підключений до створеної користувацької мережі.
# • Контейнери Nginx та Busybox повинні мати можливість спілкуватися один з одним за іменем хоста у межах створеної мережі.

# Creating a custom network with the bridge driver.
docker network create --driver bridge bridge_netw

# Starting a container with Nginx connected to the custom network.
docker run -d --name webserver --network bridge_netw nginx

# Starting a container with BusyBox connected to the custom network.
docker run -d --name appserver --network bridge_netw busybox sleep 1000

# Testing connectivity by hostname from the BusyBox container.
docker exec appserver ping -c 4 webserver