# Using Docker Compose for Communication Between Containers
# Create a docker-compose.yml file that describes a web server
# and a PostgreSQL database connected to the same bridge network.
# Start the containers using Docker Compose — there must be communication
# between the web server and the database.
#
# Requirements:
# • A docker-compose.yml file must be created that contains definitions
#   for both the web server and the PostgreSQL database as services.
# • The docker-compose.yml file must include the definition of a bridge network
#   to which both containers are connected to ensure communication between them.
# • The web server and the PostgreSQL database must be configured
#   so that they can exchange data through the specified bridge network.
# • The containers for the web server and the database must be started
#   using the Docker Compose command to ensure their automatic orchestration and communication.
#
# ## 🇺🇦 Ukrainian version:
#
# Використання Docker Compose для зв'язку між контейнерами
# Створіть файл docker-compose.yml, який описує веб-сервер та базу даних PostgreSQL,
# підключені до однієї bridge мережі.
# Запустіть контейнери за допомогою Docker Compose - між веб-сервером і базою даних має бути зв'язок.
#
# Вимоги:
# • Необхідно створити файл docker-compose.yml, який містить опис як веб-сервера,
#   так і бази даних PostgreSQL, визначаючи їх як сервіси.
# • Файл docker-compose.yml повинен включати визначення bridge мережі,
#   до якої підключені обидва контейнери для забезпечення їх зв'язку.
# • Веб-сервер та база даних PostgreSQL повинні бути сконфігуровані так,
#   щоб мати можливість обмінюватися даними через вказану bridge мережу.
# • Контейнери для веб-сервера та бази даних повинні бути запущені
#   за допомогою команди Docker Compose, щоб забезпечити їх автоматичну оркестрацію та зв'язок.

# Starting containers using Docker Compose
docker compose up -d

# Checking connectivity between the web server and the database
docker compose exec web ping -c 4 db