# Managing Docker Networks
# Perform the following actions:
#
# 1. Create a new network named app_network.
# 2. Connect the container named app_container to this network.
# 3. Display a list of all available networks.
# 4. Disconnect the app_container container from the network.
#
# Requirements:
# • Create a new network named app_network.
# • Connect the container named app_container to the app_network network.
# • Display a list of all available networks.
# • Disconnect the app_container container from the app_network network.
#
# ## 🇺🇦 Ukrainian version:
#
# Керування мережами Docker
# Виконайте наступні дії:
#
# 1. Створіть нову мережу з іменем app_network.
# 2. Підключіть контейнер з іменем app_container до цієї мережі.
# 3. Виведіть список усіх доступних мереж.
# 4. Відключіть контейнер app_container від мережі.
#
# Вимоги:
# • Створіть нову мережу з іменем app_network.
# • Підключіть контейнер з іменем app_container до мережі app_network.
# • Відобразіть список усіх доступних мереж.
# • Відключіть контейнер app_container від мережі app_network.

# Creating a new network named app_network
docker network create app_network

# Connecting the container named app_container to the app_network network
docker network connect app_network app_container

# Displaying the list of all available networks
docker network ls

# Disconnecting the app_container container from the app_network network
docker network disconnect app_network app_container