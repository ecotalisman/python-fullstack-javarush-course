# Working with Docker Volumes
# Perform the following actions:
#
# 1. Create a new volume named data_volume.
# 2. View information about the created volume.
# 3. Mount this volume in a container named my_container at the path /data.
# 4. Remove the volume after you finish using it.
#
# Requirements:
# • Create a new Docker volume named `data_volume`.
# • View information about the created `data_volume` volume.
# • Mount the `data_volume` volume in a container named `my_container` at the path `/data`.
# • Remove the volume after use is complete.
#
# ## 🇺🇦 Ukrainian version:
#
# Робота з томами Docker
# Виконайте наступні дії:
#
# 1. Створіть новий том з іменем data_volume.
# 2. Перегляньте інформацію про створений том.
# 3. Змонтуйте цей том у контейнері з іменем my_container за шляхом /data.
# 4. Видаліть том після завершення використання.
#
# Вимоги:
# • Створіть новий Docker том з іменем `data_volume`.
# • Перегляньте інформацію про створений том `data_volume`.
# • Змонтуйте том `data_volume` у контейнері з іменем `my_container` за шляхом `/data`.
# • Видаліть том після завершення використання.

# Creating a new Docker volume named data_volume
docker volume create data_volume

# Viewing information about the created data_volume volume
docker volume inspect data_volume

# Running a container and mounting the data_volume volume at the path /data
docker run -d --name my_container -v data_volume:/data alpine

# Removing the my_container container and the data_volume volume
docker rm -f my_container
docker volume rm data_volume