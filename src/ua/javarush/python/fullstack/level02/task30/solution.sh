# Sharing a Volume Between Containers
# Create a volume named shared_volume and run two containers based on the nginx image,
# mounting this volume into the /shared directory inside each container.
# Name the containers container_one and container_two.
#
# Requirements:
# • A Docker volume named shared_volume must be created.
# • A container named container_one must be started using the nginx image, with the shared_volume
#   volume mounted into the /shared directory inside the container.
# • A container named container_two must be started using the nginx image, with the shared_volume
#   volume mounted into the /shared directory inside the container.
# • The created shared_volume volume must be shared by both containers, container_one and container_two.
#
# ## 🇺🇦 Ukrainian version:
#
# Спільне використання тому між контейнерами
# Створіть том shared_volume і запустіть два контейнери з образами nginx,
# змонтувавши цей том у директорію /shared всередині кожного контейнера.
# Назвіть контейнери container_one і container_two.
#
# Вимоги:
# • Необхідно створити Docker том з іменем shared_volume.
# • Необхідно запустити контейнер з іменем container_one, використовуючи образ nginx,
#   і змонтувати том shared_volume у директорію /shared всередині контейнера.
# • Необхідно запустити контейнер з іменем container_two, використовуючи образ nginx,
#   і змонтувати том shared_volume у директорію /shared всередині контейнера.
# • Створений том shared_volume має використовуватися спільно обома контейнерами
#   container_one і container_two.

# Create a named volume:
docker volume create shared_volume

# Run the first container:
docker run -d -v shared_volume:/shared --name container_one nginx

# Run the second container:
docker run -d -v shared_volume:/shared --name container_two nginx