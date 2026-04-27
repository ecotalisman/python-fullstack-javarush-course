# Creating and Scaling a Service
# Create the my_web service in a Docker Swarm cluster,
# which will run Nginx with 3 replicas and publish container port 80
# to host port 8080. Then scale the service to 5 replicas.
#
# Requirements:
# • The my_web service must be created in the Docker Swarm cluster
#   and run a container with the Nginx image.
# • Container port 80 of Nginx must be published to host port 8080.
# • The service must be created with 3 replicas.
# • The my_web service must be scaled to 5 replicas after creation.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення і масштабування сервісу
# Створіть сервіс my_web у кластері Docker Swarm,
# який буде запускати Nginx з 3 репліками і публікувати порт 80 контейнера
# на порт 8080 хоста. Потім масштабуйте сервіс до 5 реплік.
#
# Вимоги:
# • Сервіс my_web повинен бути створений у кластері Docker Swarm
#   і запускати контейнер із образом Nginx.
# • Порт 80 контейнера Nginx повинен бути опублікований на порт 8080 хоста.
# • Сервіс повинен бути створений з 3 репліками.
# • Сервіс my_web повинен бути масштабований до 5 реплік після створення.

# Initializing Docker Swarm
docker swarm init

# Creating the my_web service with 3 replicas
docker service create --name my_web --replicas 3 -p 8080:80 nginx

# Scaling the my_web service to 5 replicas
docker service scale my_web=5