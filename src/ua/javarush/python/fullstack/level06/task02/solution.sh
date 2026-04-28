# Using a Bind Directory for Development
# Run a container with Nginx, mounting the local directory /home/user/website
# into the /usr/share/nginx/html directory inside the container.
# This will allow you to develop the website locally,
# and changes will be immediately visible in the container.
#
# Requirements:
# • The container must mount the local directory /home/user/website
#   into the /usr/share/nginx/html directory inside the container.
# • The official Nginx image must be used to run the container.
# • Any changes made to the local directory /home/user/website
#   must be immediately reflected in the container, displaying the updated website.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання прив'язаної директорії для розробки
# Запустіть контейнер з Nginx, монтувавши локальну директорію /home/user/website
# в директорію /usr/share/nginx/html контейнера.
# Це дозволить вам розробляти вебсайт локально,
# а зміни відразу ж будуть видні в контейнері.
#
# Вимоги:
# • Контейнер повинен монтувати локальну директорію /home/user/website
#   в директорію /usr/share/nginx/html всередині контейнера.
# • Для запуску контейнера необхідно використовувати офіційний образ Nginx.
# • Будь-які зміни, внесені в локальну директорію /home/user/website,
#   повинні миттєво відображатися в контейнері, відображаючи оновлений вебсайт.

# Creating the /home/user/website directory
mkdir -p /home/user/website
echo "<h1>Hello from bind mount!</h1>" > /home/user/website/index.html

# Run a container with Nginx, mounting the local directory /home/user/website
# into the /usr/share/nginx/html directory inside the container
docker run -d --name web -v /home/user/website:/usr/share/nginx/html nginx

# Check that the container is running and the directory is mounted
docker inspect web