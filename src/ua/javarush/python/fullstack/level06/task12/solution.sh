# Creating a Volume Backup
# Create a volume named app_data.
# Run a container with Nginx that will use this volume for data storage.
# After that, create a backup of the volume data and save it on the host as an archive.
#
# Requirements:
# • A Docker volume named app_data must be created for data storage.
# • Run a container with the Nginx image that will use the created app_data volume
#   for storing data inside the container.
# • Create a backup of the data located in the app_data volume and save this backup as an archive.
# • Save the created backup archive on the host system, outside the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Створення бекапу тому
# Створіть том із назвою app_data.
# Запустіть контейнер із Nginx, який буде використовувати цей том для збереження даних.
# Після цього створіть бекап даних тому та збережіть його на хості у вигляді архіву.
#
# Вимоги:
# • Необхідно створити том Docker із назвою app_data для збереження даних.
# • Запустіть контейнер із образом Nginx, який буде використовувати створений том app_data
#   для збереження даних всередині контейнера.
# • Створіть бекап даних, які знаходяться в томі app_data, та збережіть цей бекап у вигляді архіву.
# • Збережіть створений архів бекапу на хостовій системі, поза контейнером.

# Create a volume named app_data
docker volume create app_data

# Run a container with Nginx, mounting the app_data volume for data storage
docker run -d --name web -v app_data:/data nginx

# Write a test file to the volume, for example index.html
docker run --rm -v app_data:/data busybox sh -c "echo 'configuration data' > /data/index.html"

# Create a backup of the app_data volume data and save it on the host as an archive
docker run --rm -v app_data:/data -v $(pwd):/backup busybox tar czf /backup/app_data_backup.tar.gz -C /data .

# Check that the backup was created in the current directory
ls