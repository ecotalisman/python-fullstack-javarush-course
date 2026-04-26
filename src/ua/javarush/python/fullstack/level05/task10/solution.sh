# Checking Connectivity by Hostname
# Start two containers with Nginx and BusyBox, and connect them to a bridge network.
# Check connectivity between them using the Nginx container name
# for pinging from the BusyBox container.
#
# Requirements:
# • The script must create a bridge network to which both containers will be connected.
# • The script must start a container with Nginx and connect it to the created bridge network.
# • The script must start a container with BusyBox and connect it to the created bridge network.
# • The script must ping the Nginx container by its container name from the BusyBox container
#   to check connectivity between them.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка зв'язку за ім'ям хоста
# Запустіть два контейнери з Nginx та Busybox, підключіть їх до мережі bridge.
# Перевірте зв'язок між ними, використовуючи ім'я контейнера Nginx для пінгу з контейнера Busybox.
#
# Вимоги:
# • Скрипт повинен створити мережу типу bridge, до якої будуть підключені обидва контейнери.
# • Скрипт повинен запустити контейнер з Nginx і підключити його до створеної мережі bridge.
# • Скрипт повинен запустити контейнер з Busybox і підключити його до створеної мережі bridge.
# • Скрипт повинен виконати пінг за ім'ям контейнера Nginx з контейнера Busybox, щоб перевірити їх зв'язок.

# Creating a bridge network
docker network create --driver bridge my_bridge

# Starting a container with Nginx and connecting it to the created network
docker run -d --name webserver --network my_bridge nginx

# Starting a container with BusyBox and connecting it to the created network
docker run -d --name appserver --network my_bridge busybox sleep 1000

# Checking connectivity between containers using the container name
docker exec appserver ping -c 4 webserver