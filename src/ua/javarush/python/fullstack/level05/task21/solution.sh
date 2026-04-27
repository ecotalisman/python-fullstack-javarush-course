# Initializing a Swarm Cluster
# Initialize a new Docker Swarm cluster on your host with the IP address 192.168.1.10
# so that this node becomes the cluster manager.
# After initialization, get the command for joining worker nodes.
#
# Requirements:
# • The Docker Swarm cluster must be initialized on the host with the IP address 192.168.1.10
#   to assign this node as the cluster manager.
# • After initializing the cluster, it is necessary to get the command
#   that other nodes can use to join as worker nodes.
# • Make sure that the node with the IP address 192.168.1.10 is configured
#   as the cluster manager to manage Docker Swarm effectively.
#
# ## 🇺🇦 Ukrainian version:
#
# Ініціалізація кластера Swarm
# Ініціалізуйте новий кластер Docker Swarm на вашому хості з IP-адресою 192.168.1.10,
# щоб цей вузол став менеджером кластера.
# Після ініціалізації отримайте команду для приєднання робочих вузлів.
#
# Вимоги:
# • Кластер Docker Swarm має бути ініціалізований на хості з IP-адресою 192.168.1.10,
#   щоб призначити цей вузол як менеджера кластера.
# • Після ініціалізації кластера необхідно отримати команду,
#   яку інші вузли зможуть використовувати для приєднання як робочі вузли.
# • Переконайтеся, що вузол з IP-адресою 192.168.1.10 налаштований як менеджер кластера,
#   щоб ефективно керувати Docker Swarm.

# Initializing Docker Swarm on the host with the IP address 192.168.1.10
docker swarm init --advertise-addr 192.168.1.10

# Getting the command for joining worker nodes
docker swarm join-token worker