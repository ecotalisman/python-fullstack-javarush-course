# Running a Container in Detached Mode
# Run a container with the Nginx web server in detached mode.
# Assign the container the name my_nginx so that it can be easily identified during further operations.
#
# Requirements:
# • The container with the Nginx web server must be started in detached mode, allowing you to continue working in
# the terminal after it starts.
# • The container must be assigned the name my_nginx to simplify identification during further operations.
# • The container must contain the Nginx web server, ensuring that it can be started and run inside the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск контейнера у фоновому режимі
# Запустіть контейнер із веб-сервером Nginx у фоновому режимі.
# Присвойте контейнеру ім'я my_nginx, щоб його було легко ідентифікувати при подальших операціях.
#
# Вимоги:
# • Контейнер із веб-сервером Nginx має бути запущений у фоновому режимі, що дозволяє продовжувати роботу в терміналі
# після його запуску.
# • Контейнеру необхідно присвоїти ім'я my_nginx для спрощення ідентифікації при виконанні подальших операцій.
# • Контейнер повинен містити веб-сервер Nginx, що забезпечує можливість його запуску і роботи в контейнері.

# Running a container in detached mode
docker run -d --name my_nginx nginx
