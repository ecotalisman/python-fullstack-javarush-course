# Checking Connectivity Between Containers by IP
#
# Start two containers: one with Nginx and another with BusyBox.
# Both must be connected to the default bridge network.
# Then determine their IP addresses and check connectivity between them
# using the ping command from the BusyBox container.
#
# Requirements:
# • A container with Nginx installed must be created and started,
#   connected to the default bridge network.
# • A container with BusyBox installed must be created and started,
#   connected to the default bridge network.
# • The IP addresses of both running containers must be determined.
# • From the BusyBox container, the ping command must be executed
#   for the IP address of the Nginx container to make sure that connectivity is established.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка зв'язку між контейнерами за IP
#
# Запустіть два контейнери: один із Nginx, а інший із Busybox,
# обидва повинні бути підключені до мережі bridge за замовчуванням.
# Потім визначте їх IP-адреси та перевірте зв'язок між ними,
# використовуючи команду ping із контейнера Busybox.
#
# Вимоги:
# • Необхідно створити та запустити контейнер із встановленим Nginx,
#   підключений до мережі bridge за замовчуванням.
# • Необхідно створити та запустити контейнер із встановленим Busybox,
#   підключений до мережі bridge за замовчуванням.
# • Необхідно визначити IP-адреси обох запущених контейнерів.
# • Необхідно з контейнера Busybox виконати команду ping для IP-адреси контейнера з Nginx
#   і переконатися, що зв'язок встановлюється.

# Starting a container with Nginx on the default bridge network
docker run -d --name container1 nginx

# Starting a container with BusyBox on the default bridge network
docker run -d --name container2 busybox sleep 1000

# Determining the IP addresses of the containers
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container1
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container2

# Checking connectivity between containers using the ping command
docker exec container2 ping -c 4 <IP_ADDRESS_OF_CONTAINER1>