# Creating an overlay Network
# Initialize a Docker Swarm cluster on your host
# and create an overlay network named my_overlay_network,
# which will be used for communication between containers on different nodes.
#
# Requirements:
# • It is necessary to initialize a Docker Swarm cluster on the current host.
#   This will allow containers on multiple nodes to be managed as a single system.
# • After initializing the cluster, it is necessary to create an overlay network
#   with the exact name my_overlay_network. This network will enable communication
#   between containers located on different nodes in Docker Swarm.
# • The created my_overlay_network overlay network must be configured
#   for use by containers that are planned to be deployed in this cluster.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення overlay мережі
# Ініціалізуйте кластер Docker Swarm на вашому хості та створіть overlay мережу
# з ім'ям my_overlay_network, яка буде використовуватися для зв'язку між контейнерами
# на різних вузлах.
#
# Вимоги:
# • Необхідно ініціалізувати Docker Swarm кластер на поточному хості.
#   Це дозволить управляти контейнерами на декількох вузлах як єдиною системою.
# • Після ініціалізації кластера необхідно створити overlay мережу з точним ім'ям my_overlay_network.
#   Ця мережа забезпечить можливість взаємодії між контейнерами,
#   розташованими на різних вузлах у Docker Swarm.
# • Створена overlay мережа my_overlay_network має бути налаштована для використання контейнерами,
#   які планується розгорнути у цьому кластері.

# Initializing Docker Swarm
docker swarm init

# Creating an overlay network named my_overlay_network
docker network create -d overlay my_overlay_network