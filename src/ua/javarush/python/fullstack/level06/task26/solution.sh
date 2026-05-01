# Backing Up and Restoring with Restic
# Using the Restic utility, create a backup of data from the /path/to/data directory,
# and then restore it to the /path/to/restore directory.
#
# Requirements:
# • The Restic utility must be installed on the server
#   to perform backup and restore operations.
# • The Restic command must be used to create a backup
#   of data from the /path/to/data directory.
# • During data restoration using Restic, the /path/to/restore directory
#   must be specified as the target directory for restoration.
#
# ## 🇺🇦 Ukrainian version:
#
# Резервне копіювання та відновлення за допомогою Restic
# За допомогою утиліти Restic створіть резервну копію даних з директорії /path/to/data,
# а потім відновіть їх у директорію /path/to/restore.
#
# Вимоги:
# • На сервері має бути встановлена утиліта Restic для виконання операцій резервного копіювання та відновлення.
# • Необхідно використовувати команду Restic для створення резервної копії даних з директорії /path/to/data.
# • У процесі відновлення даних за допомогою Restic слід вказати директорію /path/to/restore як цільову директорію для відновлення.

# Initializing the Restic repository for backup, if it has not been initialized yet
restic init --repo /path/to/data

# Perform a backup of data from the /path/to/data directory
restic -r /path/to/data backup /path/to/data

# Check that the backup was successful
restic -r /path/to/data snapshots

# Restore data from the latest backup to the /path/to/restore directory
restic -r /path/to/data restore latest --target /path/to/restore

# Check that the data has been restored to the /path/to/restore directory
ls -lh /path/to/restore