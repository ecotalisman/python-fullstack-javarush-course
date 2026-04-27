# Joining Worker Nodes to Swarm
# Join a worker node with the IP address 192.168.1.20
# to an already initialized Swarm cluster with the manager at 192.168.1.10.
# Use the following join token: SWMTKN-1-0defghi1234jklmnop-5678qrstuvwx90yz.
#
# Requirements:
# • The worker node must have the IP address 192.168.1.20.
# • The Swarm cluster manager must be available at the IP address 192.168.1.10.
# • The token SWMTKN-1-0defghi1234jklmnop-5678qrstuvwx90yz must be used to join the node.
# • The Swarm cluster must already be initialized before joining the worker node.
#
# ## 🇺🇦 Ukrainian version:
#
# Приєднання робочих вузлів до Swarm
# Приєднайте робочий вузол з IP-адресою 192.168.1.20
# до вже ініціалізованого кластера Swarm з менеджером за адресою 192.168.1.10.
# Використовуйте наступний токен для приєднання: SWMTKN-1-0defghi1234jklmnop-5678qrstuvwx90yz.
#
# Вимоги:
# • Робочий вузол повинен мати IP-адресу 192.168.1.20.
# • Менеджер кластера Swarm повинен бути доступний за IP-адресою 192.168.1.10.
# • Для приєднання вузла має бути використаний токен SWMTKN-1-0defghi1234jklmnop-5678qrstuvwx90yz.
# • Кластер Swarm повинен бути вже ініціалізований перед приєднанням робочого вузла.

# Joining the worker node with the IP address 192.168.1.20 to the already initialized Swarm cluster
docker swarm join --token SWMTKN-1-0defghi1234jklmnop-5678qrstuvwx90yz 192.168.1.10:2377