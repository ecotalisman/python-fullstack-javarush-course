# Running a Container Based on the MySQL Image
# Run a container with a MySQL database. Set the password for the root user to my-secret-pw
# and forward container port 3306 to port 3306 on the host machine.
# Name the container mysql_db.
#
# Requirements:
# • The container must be started based on the official MySQL image.
# • The password my-secret-pw must be set for the root user inside the container.
# • Container port 3306 must be forwarded to port 3306 on the host machine.
# • The container must be named mysql_db.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск контейнера на основі образу MySQL
# Запустіть контейнер з базою даних MySQL. Встановіть пароль для користувача root як my-secret-pw
# та перенаправте порт 3306 контейнера на порт 3306 хост-машини.
# Назвіть контейнер mysql_db.
#
# Вимоги:
# • Контейнер має бути запущений на основі офіційного образу MySQL.
# • Необхідно встановити пароль my-secret-pw для користувача root в контейнері.
# • Порт 3306 контейнера має бути перенаправлений на порт 3306 хост-машини.
# • Контейнер має бути названий як mysql_db.

# Set the password for the root user to my-secret-pw and forward container port 3306 to port 3306 on the host machine.
docker run -d -p 3306:3306 --name mysql_db -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest