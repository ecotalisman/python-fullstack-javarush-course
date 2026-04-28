# Restricting Port Access
# Run a container with Nginx and restrict access to it only from the local host
# (IP 127.0.0.1) on port 8080. External connections must not have access to this container.
#
# Requirements:
# • The container must be started with the Nginx server installed and configured.
# • Access to the container must be restricted only to the IP address 127.0.0.1.
# • Nginx inside the container must be available on port 8080.
# • All external connections that do not come from the local host must be blocked
#   and must not have access to the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Обмеження доступу до порту
# Запустіть контейнер з Nginx та обмежте доступ до нього лише з локального хоста
# (IP 127.0.0.1) на порту 8080. Зовнішні підключення не повинні мати доступу до цього контейнера.
#
# Вимоги:
# • Контейнер повинен бути запущений з встановленим та налаштованим сервером Nginx.
# • Доступ до контейнера повинен бути обмежений лише з IP-адреси 127.0.0.1.
# • Nginx у контейнері повинен бути доступний на порту 8080.
# • Усі зовнішні підключення, що не надходять з локального хоста, повинні бути заблоковані
#   та не мати доступу до контейнера.

# Run a container with Nginx, forwarding container port 80 to host port 8080,
# but restrict access only to the local IP 127.0.0.1
docker run -d -p 127.0.0.1:8080:80 --name web nginx

# Check that the container is running and accessible only from the local host
docker ps

# You can check access by sending an HTTP request to the local host
# For example, using the curl command
curl http://127.0.0.1:8080