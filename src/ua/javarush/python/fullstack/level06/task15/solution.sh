# Automating Volume Backups
# Write a script that automatically creates backups of the app_data volume every day
# and removes backups that are older than 7 days.
#
# Requirements:
# • The script must create backups of the app_data volume every day,
#   ensuring that an up-to-date backup is available.
# • The script must automatically remove backups of the app_data volume
#   that are older than 7 days to save space and keep the data up to date.
#
# ## 🇺🇦 Ukrainian version:
#
# Автоматизація бекапів томів
# Напишіть скрипт, який буде автоматично створювати бекапи тому app_data кожен день
# і видаляти бекапи, яким більше 7 днів.
#
# Вимоги:
# • Скрипт повинен щодня створювати бекапи тому app_data, забезпечуючи наявність актуальної резервної копії.
# • Скрипт повинен автоматично видаляти бекапи тому app_data, яким більше 7 днів,
#   для економії місця та підтримання актуальності даних.

# Directory for storing backups
BACKUP_DIR="/path/to/backup_directory"

# Name of the volume to back up
VOLUME_NAME="app_data"

# Create the backup storage directory if it does not exist
mkdir -p $BACKUP_DIR

# Create a backup with a name matching the date, for example app_data_backup_YYYYMMDD_HHMM.tar.gz
BACKUP_FILE="$BACKUP_DIR/${VOLUME_NAME}_backup_$(date +%Y%m%d_%H%M).tar.gz"

# Create a backup of the app_data volume
docker run --rm -v ${VOLUME_NAME}:/data -v $BACKUP_DIR:/backup busybox tar czf /backup/$(basename $BACKUP_FILE) -C /data .

# Remove backups older than 7 days
find $BACKUP_DIR -type f -name "${VOLUME_NAME}_backup_*.tar.gz" -mtime +7 -exec rm -f {} \;