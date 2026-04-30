# Checking the Contents of Mounted Directories
# Start a container with a directory mounted from the host.
# Use the docker exec command to check the contents
# of the mounted directory inside the container.
#
# Requirements:
# • The container must be started using Docker with the option
#   for mounting a directory from the host into the container.
# • The docker exec command must be used to access the container
#   in order to check the contents of the mounted directory.
# • When mounting, the path to the directory on the host
#   and the path where it will be available inside the container
#   must be specified correctly.
# • Access permissions must be respected so that the container
#   and the user can perform actions in the mounted directory.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка вмісту змонтованих директорій
# Запустіть контейнер зі змонтованою директорією з хоста.
# Використовуйте команду docker exec, щоб перевірити вміст
# змонтованої директорії всередині контейнера.
#
# Вимоги:
# • Контейнер має бути запущений із використанням Docker із зазначенням опції
#   для монтування директорії з хоста всередину контейнера.
# • Необхідно використовувати команду docker exec для доступу до контейнера
#   з метою перевірки вмісту змонтованої директорії.
# • Під час монтування потрібно правильно вказати шлях до директорії на хості
#   та шлях, за яким вона буде доступна всередині контейнера.
# • Мають бути дотримані права доступу, що дозволяють контейнеру
#   та користувачеві виконувати дії у змонтованій директорії.

# Creating a directory on the host for mounting if it does not exist
mkdir -p ~/myapp

# Writing a test file to the directory on the host
echo "Hello world!" > ~/myapp/index.html

# Starting a container with the mounted directory
docker run -d --name web -v ~/myapp:/usr/share/nginx/html nginx

# Checking the contents of the mounted directory inside the container
docker exec -it web ls /usr/share/nginx/html

# Displaying the contents of the test file inside the container
docker exec -it web cat /usr/share/nginx/html/index.html