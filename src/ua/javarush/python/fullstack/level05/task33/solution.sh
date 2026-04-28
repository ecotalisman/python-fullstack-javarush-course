# Creating an Isolated Network for a Web Application
# Create a custom bridge network named secure_network.
# Run a container with Nginx in this network so that it is isolated from other containers.
#
# Requirements:
# • The script must create a new custom bridge network named secure_network.
# • The script must start a container with the Nginx server installed.
# • The Nginx container must be connected to the created secure_network
#   to ensure isolation from other containers.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення ізольованої мережі для веб-застосунку
# Створіть користувацьку bridge-мережу з назвою secure_network.
# Запустіть контейнер із Nginx у цій мережі, щоб він був ізольований від інших контейнерів.
#
# Вимоги:
# • Скрипт має створити нову користувацьку bridge-мережу з іменем secure_network.
# • Скрипт має запустити контейнер із встановленим сервером Nginx.
# • Контейнер із Nginx має бути підключений до створеної мережі secure_network для забезпечення ізоляції від інших контейнерів.

# Create a custom bridge network named secure_network
docker network create secure_network

# Run a container with Nginx, connecting it to the secure_network network
# The container will be isolated from other networks and containers
docker run -d --name web --network secure_network nginx

# Check that the container is running and connected to the secure_network network
docker network inspect secure_network