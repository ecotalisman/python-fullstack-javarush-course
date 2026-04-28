# Resolving an IP Address Conflict
# A Docker network has an IP address conflict issue.
# Create a new network named my_custom_network with the subnet 192.168.2.0/24
# to avoid conflicts, and connect the web container to this network.
#
# Requirements:
# • Create a new Docker network named my_custom_network and specify the 192.168.2.0/24 subnet
#   to avoid IP address conflicts.
# • Connect the web container to the created my_custom_network network.
# • Make sure that after connecting the web container to the my_custom_network network,
#   the container receives an IP address from the 192.168.2.0/24 subnet range.
#
# ## 🇺🇦 Ukrainian version:
#
# Розв'язання проблеми з конфліктом IP-адрес
# У мережі Docker виникла проблема з конфліктом IP-адрес.
# Створіть нову мережу з назвою my_custom_network та підмережею 192.168.2.0/24,
# щоб уникнути конфліктів, і підключіть контейнер web до цієї мережі.
#
# Вимоги:
# • Створіть нову мережу Docker з назвою my_custom_network і вкажіть підмережу 192.168.2.0/24 для уникнення конфліктів IP-адрес.
# • Підключіть контейнер web до створеної мережі my_custom_network.
# • Переконайтеся, що після підключення контейнера web до мережі my_custom_network, контейнер отримує IP-адресу з діапазону підмережі 192.168.2.0/24.

# Make sure that the web container is running
docker ps

# Stop the web container before changing the network
docker stop web

# Create a new network named my_custom_network with the subnet 192.168.2.0/24
docker network create --subnet 192.168.2.0/24 my_custom_network

# Connect the web container to the new my_custom_network network
docker network connect my_custom_network web

# Start the web container after connecting it to the new network
docker start web

# Check the web container connection to the new network
docker network inspect my_custom_network