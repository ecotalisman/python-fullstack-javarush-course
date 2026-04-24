# Creating an overlay Network
# Initialize Docker Swarm on your host.
# Create an overlay network named my_overlay_network
# and deploy a service with an Nginx container in it.
#
# Requirements:
# • The host machine must be initialized as a Docker Swarm using the docker swarm init command.
# • It is necessary to create an overlay network named my_overlay_network using the docker network create command with
# the appropriate parameters.
# • The service must be deployed in the my_overlay_network network and use the Nginx image.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення overlay-мережі
# Ініціалізуйте Docker Swarm на вашому хості.
# Створіть overlay-мережу з ім'ям my_overlay_network та розгорніть у ній сервіс із контейнером Nginx.
#
# Вимоги:
# • Хостова машина має бути ініціалізована як Docker Swarm, використовуючи команду docker swarm init.
# • Необхідно створити overlay-мережу з ім'ям my_overlay_network, використовуючи команду docker network create з
# відповідними параметрами.
# • Сервіс має бути розгорнутий у мережі my_overlay_network і використовувати образ Nginx.

# Initializing Docker Swarm
docker swarm init

# Creating the overlay network
docker network create --driver overlay my_overlay_network

# Deploying a service with an Nginx container in the overlay network
docker service create --name my_web_overlay --network my_overlay_network nginx

# Checking that the service is working
docker network ls