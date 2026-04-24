# Removing a Network
# Create a network with the bridge driver and connect the container container1 to it.
# Then disconnect the container from the network and remove the created network.
#
# Requirements:
# • A network must be created using the bridge driver to provide an isolated environment for containers.
# • The container container1 must be connected to the created network to enable its interaction
#   with other containers on this network.
# • The container container1 must be disconnected from the created network
#   to prepare for network removal without conflicts.
# • After disconnecting the container from the network, the created network must be removed
#   to free resources and complete the task.
#
# ## 🇺🇦 Ukrainian version:
#
# Видалення мережі
# Створіть мережу з драйвером bridge, підключіть до неї контейнер container1.
# Потім відключіть контейнер від мережі та видаліть створену мережу.
#
# Вимоги:
# • Необхідно створити мережу з використанням драйвера bridge для забезпечення ізольованого середовища для контейнерів.
# • Контейнер container1 має бути підключений до створеної мережі, щоб забезпечити його взаємодію з іншими контейнерами в цій мережі.
# • Контейнер container1 повинен бути відключений від створеної мережі, щоб підготуватися до видалення мережі без конфліктів.
# • Після відключення контейнера від мережі необхідно видалити створену мережу, щоб звільнити ресурси та завершити задачу.

# Creating a network with the bridge driver
docker network create -d bridge my_bridge

# Running a container and connecting it to the network
docker run -d --name container1 --network my_bridge

# Disconnecting the container from the network
docker network disconnect my_bridge container1

# Removing the created network
docker network rm my_bridge