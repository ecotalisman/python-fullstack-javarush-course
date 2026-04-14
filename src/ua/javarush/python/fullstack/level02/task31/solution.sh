# Backing Up and Restoring a Volume
# Create a backup of the my_volume volume into the /backup/my_volume_backup.tar.gz file on the host
# using a busybox container. Then restore this volume from the backup.
#
# Requirements:
# • The script must create a backup of the my_volume volume into the /backup/my_volume_backup.tar.gz file on the host
# using a busybox container.
# • A busybox container must be used to perform the backup and restore tasks.
# • The backup file must be created at the path /backup/my_volume_backup.tar.gz on the host machine.
# • The script must restore the my_volume volume from the previously created backup file /backup/my_volume_backup.tar.gz.
#
# ## 🇺🇦 Ukrainian version:
#
# Резервне копіювання та відновлення тому
# Створіть резервну копію тому my_volume у файл /backup/my_volume_backup.tar.gz на хості за допомогою контейнера busybox.
# Потім відновіть цей том із резервної копії.
#
# Вимоги:
# • Скрипт повинен створити резервну копію тому my_volume у файл /backup/my_volume_backup.tar.gz на хості, використовуючи
# контейнер busybox.
# • Для виконання завдання резервного копіювання та відновлення необхідно використовувати контейнер busybox.
# • Файл резервної копії має бути створений у шляху /backup/my_volume_backup.tar.gz на хост-машині.
# • Скрипт повинен відновити том my_volume із раніше створеного файлу резервної копії /backup/my_volume_backup.tar.gz.

# Creating a directory for storing the backup if it does not exist
mkdir -p /backup

# Creating a backup of the my_volume volume using a busybox container
docker run --rm -v my_volume:/volume -v /backup:/backup busybox tar czf /backup/my_volume_backup.tar.gz /volume

# Restoring the my_volume volume from the previously created backup
docker run --rm -v my_volume:/volume -v /backup:/backup busybox tar xzf /backup/my_volume_backup.tar.gz -C /volume