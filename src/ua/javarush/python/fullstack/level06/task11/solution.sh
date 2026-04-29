# Checking Volume Contents
# Create a volume named config_volume and write a configuration file into it
# using a temporary container. Then check the volume contents using the ls command.
#
# Requirements:
# • A volume named config_volume must be created to store the configuration file.
# • A temporary container must be used to write the configuration file into the config_volume volume.
# • The ls command must be used to check the contents of the config_volume volume
#   and confirm that the configuration file exists.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка вмісту тому
# Створіть том config_volume та запишіть у нього файл конфігурації за допомогою тимчасового контейнера.
# Потім перевірте вміст тому за допомогою команди ls.
#
# Вимоги:
# • Повинен бути створений том із назвою config_volume для збереження конфігураційного файлу.
# • Тимчасовий контейнер повинен бути використаний для запису конфігураційного файлу в том config_volume.
# • Команда ls повинна бути використана для перевірки вмісту тому config_volume
#   та підтвердження наявності конфігураційного файлу.

# Create a volume named config_volume
docker volume create config_volume

# Run a temporary container and write a configuration file into the volume
docker run --rm -v config_volume:/app busybox sh -c "echo 'configuration data' > /app/config.txt"

# Run another temporary container to check the volume contents using the ls command
docker run --rm -v config_volume:/app busybox ls /app

# Displaying the contents of the configuration file
docker run --rm -v config_volume:/app busybox cat /app/config.txt