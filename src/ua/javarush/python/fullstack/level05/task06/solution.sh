# Connecting to an Existing Network
# Start a container named my_container without specifying a network.
# Then connect this container to the my_bridge_network network.
#
# Requirements:
# • The container named my_container must be started without being connected to any network.
# • The my_container container must be connected to the existing network named my_bridge_network.
# • The my_bridge_network network must be created in advance and ready for use before connecting the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Підключення до існуючої мережі
# Запустіть контейнер з ім'ям my_container без вказівки мережі.
# Потім підключіть цей контейнер до мережі my_bridge_network.
#
# Вимоги:
# • Контейнер з ім'ям my_container має бути запущений без підключення до будь-якої мережі.
# • Контейнер my_container має бути підключений до існуючої мережі з ім'ям my_bridge_network.
# • Мережа my_bridge_network має бути створена заздалегідь і готова до використання перед підключенням контейнера.

# Starting the my_container container without connecting it to any network
docker run -d --name my_container nginx

# Connecting the my_container container to the existing my_bridge_network network
docker network connect my_bridge_network my_container