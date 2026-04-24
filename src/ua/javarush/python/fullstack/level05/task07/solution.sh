# Disconnecting a Container from a Network
# Disconnect the my_container container from the my_bridge_network network.
# The container must continue running after this.
#
# Requirements:
# • The script must identify the container named my_container to perform the network disconnection operation.
# • The script must identify the network named my_bridge_network from which the container must be disconnected.
# • The script must execute a command that disconnects the my_container container from the my_bridge_network network,
#   while the container must continue running.
# • After being disconnected from the network, the my_container container must continue working without being restarted or stopped.
#
# ## 🇺🇦 Ukrainian version:
#
# Відключення контейнера від мережі
# Відключіть контейнер my_container від мережі my_bridge_network.
# Контейнер повинен продовжувати працювати після цього.
#
# Вимоги:
# • Скрипт має ідентифікувати контейнер із ім'ям my_container для виконання операції відключення від мережі.
# • Скрипт має ідентифікувати мережу з ім'ям my_bridge_network, від якої необхідно відключити контейнер.
# • Скрипт має виконати команду, яка відключить контейнер my_container від мережі my_bridge_network, при цьому контейнер має продовжувати функціонувати.
# • Після відключення від мережі контейнер my_container має продовжувати свою роботу без перезапуску чи зупинки.

# Disconnecting the container from the network
docker network disconnect my_bridge_network my_container

# Checking the container status
docker ps
