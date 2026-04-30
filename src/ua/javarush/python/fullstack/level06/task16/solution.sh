# Mounting a Directory for Web Application Development
# Create a directory on the host with a simple web page file named index.html.
# Mount this directory into a container with Nginx so that changes to files on the host
# are immediately reflected in the container.
#
# Requirements:
# • The script must create a directory on the host and place an index.html file
#   with simple web page content into it.
# • The script must mount the created host directory into a container
#   started from the Nginx image. The mount path inside the container
#   must match the standard path for serving Nginx web pages.
# • The script must ensure that any changes made to files inside the mounted directory
#   on the host are automatically reflected in the Nginx container
#   without requiring it to be restarted.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування директорії для розробки веб-додатка
# Створіть директорію на хості з простим веб-сторінковим файлом index.html.
# Змонтуйте цю директорію в контейнер з Nginx, щоб зміни у файлах на хості
# одразу відображалися в контейнері.
#
# Вимоги:
# • Скрипт має створювати директорію на хості та поміщати туди файл index.html
#   з простим веб-сторінковим вмістом.
# • Скрипт має монтувати створену на хості директорію в контейнер,
#   запущений з образом Nginx. Шлях монтування в контейнері має відповідати
#   стандартному шляху розміщення веб-сторінок Nginx.
# • Скрипт має гарантувати, що будь-які зміни, внесені у файли всередині
#   змонтованої директорії на хості, автоматично відображаються в контейнері
#   з Nginx без необхідності його перезапуску.

# Creating a directory for web content
mkdir -p ./web_content

# Create a simple web page file named index.html
echo "<html><body><h1>Hello from Docker!</h1></body></html>" > ./web_content/index.html

# Starting an Nginx container with the directory mounted
docker run -d --name web -v $(pwd)/web_content:/usr/share/nginx/html nginx