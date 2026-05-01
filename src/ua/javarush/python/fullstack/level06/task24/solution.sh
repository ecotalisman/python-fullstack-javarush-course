# Backing Up and Restoring Docker Volumes
# Using the docker-volume-backup utility, create a backup of the my_volume volume
# and save it to the my_backup.tar.gz file. Then restore this volume from the backup.
#
# Requirements:
# • The script must use the docker-volume-backup utility to create a backup of the my_volume volume.
# • The backup must be saved to a file named my_backup.tar.gz.
# • The script must provide the ability to restore the my_volume volume from the my_backup.tar.gz file.
# • The backup creation and restore process must be performed using Docker commands and the appropriate utilities.
#
# ## 🇺🇦 Ukrainian version:
#
# Резервне копіювання та відновлення томів Docker
# За допомогою утиліти docker-volume-backup створіть резервну копію тому my_volume
# та збережіть її у файл my_backup.tar.gz.
# Потім відновіть цей том із бекапу.
#
# Вимоги:
# • Скрипт повинен використовувати утиліту docker-volume-backup для створення резервної копії тому my_volume.
# • Резервна копія повинна бути збережена у файл з іменем my_backup.tar.gz.
# • Скрипт повинен передбачати можливість відновлення тому my_volume із файлу my_backup.tar.gz.
# • Процес створення та відновлення резервної копії повинен бути виконаний з використанням команд Docker та відповідних утиліт.

# Create a backup of the my_volume volume and save it to the my_backup.tar.gz file
docker-volume-backup backup my_volume my_backup.tar.gz

# Check that the backup was created
ls -lh my_backup.tar.gz

# Restore the my_volume volume from the my_backup.tar.gz backup
docker-volume-backup restore my_backup.tar.gz my_volume

# Check that the volume has been restored
docker volume ls