# Diagnosing Network Issues Using nslookup
# The web container has problems resolving hostnames.
# Use the nslookup command to check whether DNS is correctly configured
# for the db container in the webnet network.
#
# Requirements:
# • The nslookup command must be used to check hostname resolution inside the container.
# • It is necessary to check whether DNS is correctly configured for the db container running in the webnet network.
# • The nslookup command must be executed inside the web container to diagnose network issues.
# • The check must be performed in the context of the webnet network, where the containers communicate.
#
# ## 🇺🇦 Ukrainian version:
#
# Діагностика мережевих проблем із використанням nslookup
# У контейнері web виникають проблеми з розв'язанням імен хостів.
# Використайте команду nslookup, щоб перевірити, чи правильно налаштовується DNS
# для контейнера db у мережі webnet.
#
# Вимоги:
# • Потрібно використовувати команду nslookup для перевірки розв'язання імен хостів усередині контейнера.
# • Необхідно перевірити, чи правильно налаштований DNS для контейнера db, що працює в мережі webnet.
# • Команда nslookup має бути виконана усередині контейнера web для діагностики мережевих проблем.
# • Перевірка має відбуватися в контексті мережі webnet, у якій взаємодіють контейнери.

# Make sure that the webnet network is created
docker network create webnet

# Running the web container with Nginx, connected to the webnet network
docker run -d --name web --network webnet nginx

# Running the db container with PostgreSQL, connected to the webnet network
docker run -d --name db -e POSTGRES_PASSWORD=mypassword --network webnet postgres

# Installing the nslookup utility inside the web container
docker exec web apt-get update
docker exec web apt-get install -y dnsutils

# Checking DNS using nslookup
docker exec web nslookup db

# Make sure that both containers are connected to the same network
docker network inspect webnet