# Creating a macvlan Network
# Create a macvlan network with the subnet 192.168.1.0/24 and the gateway 192.168.1.1,
# which will use the eth0 network interface of your host.
# Start two containers (Nginx and BusyBox), connecting them to this network.
#
# Requirements:
# • A macvlan network must be created using the 192.168.1.0/24 subnet.
# • The macvlan network must have a gateway with the IP address 192.168.1.1.
# • When creating the macvlan network, the use of the host's eth0 network interface must be specified.
# • Start a container with the Nginx image and connect it to the created macvlan network.
# • Start a container with the BusyBox image and connect it to the created macvlan network.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення мережі macvlan
# Створіть мережу macvlan з підмережею 192.168.1.0/24 та шлюзом 192.168.1.1,
# яка буде використовувати мережевий інтерфейс eth0 вашого хоста.
# Запустіть два контейнери (Nginx і Busybox), підключивши їх до цієї мережі.
#
# Вимоги:
# • Необхідно створити мережу macvlan, використовуючи підмережу 192.168.1.0/24.
# • Мережа macvlan повинна мати шлюз з IP-адресою 192.168.1.1.
# • Під час створення мережі macvlan слід вказати використання мережевого інтерфейсу eth0 хоста.
# • Запустіть контейнер з образом Nginx і підключіть його до створеної мережі macvlan.
# • Запустіть контейнер з образом Busybox і підключіть його до створеної мережі macvlan.

# Creating the macvlan network
docker network create -d macvlan --subnet=192.168.1.0/24 --gateway=192.168.1.1 -o parent=eth0 my_macvlan_network

# Starting a container with Nginx and connecting it to the macvlan network
docker run -d --name webserver --network my_macvlan_network nginx

# Starting a container with BusyBox and connecting it to the macvlan network
docker run -d --name appserver --network my_macvlan_network busybox sleep 1000

# Checking connectivity between containers using the ping command
docker exec appserver ping -c 4 webserver

# Checking the network
docker network inspect my_macvlan_network