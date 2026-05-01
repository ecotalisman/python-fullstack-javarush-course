# Synchronizing Data with Cloud Storage
# Use the rclone utility to synchronize data from the local directory /path/to/local/dir
# with the cloud storage remote:bucket.
#
# Requirements:
# • The script must install the rclone utility and configure it to interact with cloud storage.
# • The script must use the local directory /path/to/local/dir as the data source for synchronization.
# • The script must synchronize data with the remote cloud storage using the path remote:bucket.
#
# ## 🇺🇦 Ukrainian version:
#
# Синхронізація даних з хмарним сховищем
# Використовуйте утиліту rclone для синхронізації даних із локальної директорії /path/to/local/dir
# з хмарним сховищем remote:bucket.
#
# Вимоги:
# • Скрипт має встановлювати утиліту rclone та налаштовувати її для взаємодії з хмарним сховищем.
# • Скрипт має використовувати локальну директорію /path/to/local/dir як джерело даних для синхронізації.
# • Скрипт має синхронізувати дані з віддаленим хмарним сховищем, використовуючи шлях remote:bucket.

# Updating packages and installing rclone
sudo apt-get update
sudo apt-get install -y rclone

# Synchronizing data from the local directory with cloud storage
rclone config create remote s3 \
  provider AWS \
  env_auth false \
  access_key_id AKIAXXXXXXX \
  secret_access_key WJZXXXXXX \
  region us-west-2 \
  acl private

# Perform synchronization of the local directory with the remote:bucket cloud storage
rclone sync /path/to/local/dir remote:bucket

# Check that synchronization was successful by viewing the contents of the cloud storage
rclone check /path/to/local/dir remote:bucket