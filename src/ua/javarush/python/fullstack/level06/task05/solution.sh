# Viewing Volume Information
# Create a volume named db_backup and run a container to use this volume.
# Then get information about the volume using the docker volume inspect command.
#
# Requirements:
# • A volume named db_backup must be created using the docker volume create command.
# • A container must be started with the db_backup volume specified,
#   so that the container uses this volume for data storage.
# • The docker volume inspect command must be used to get and display
#   information about the created db_backup volume.
#
# ## 🇺🇦 Ukrainian version:
#
# Перегляд інформації про том
# Створіть том з іменем db_backup і запустіть контейнер для використання цього тому.
# Потім отримайте інформацію про том за допомогою команди docker volume inspect.
#
# Вимоги:
# • Потрібно створити том з іменем db_backup за допомогою команди docker volume create.
# • Необхідно запустити контейнер, вказавши том db_backup, щоб контейнер використовував цей том для збереження даних.
# • Повинна бути використана команда docker volume inspect для отримання та відображення інформації про створений том db_backup.

# Create a volume named db_backup
docker volume create db_backup

# Running a temporary container using the db_backup volume
docker run -d --name app -e POSTGRES_PASSWORD=mysecretpassword -v db_backup:/var/lib/postgresql/data postgres

# Getting information about the db_backup volume
docker volume inspect db_backup