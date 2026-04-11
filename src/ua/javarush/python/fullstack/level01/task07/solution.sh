# Checking the Docker Daemon Status
# Check that the Docker Daemon is running on your computer. On Windows or macOS, check the icon in the system tray.
# On Linux, run the command to check the Docker Daemon status.
#
# Hint:
# Write the command to check the Docker Daemon status on Linux.
#
# Requirements:
# • The user must check for the Docker icon in the system tray to confirm that the Docker Daemon is running on Windows and macOS.
# • The user must run the `systemctl status docker` command in the terminal to check the Docker Daemon status on Linux.
#
# ## 🇺🇦 Ukrainian version:
#
# Перевірка стану Docker Daemon
# Перевірте, що Docker Daemon працює на вашому комп'ютері. На Windows або macOS перевірте значок у системному треї,
# на Linux виконайте команду для перевірки статусу Docker Daemon.
#
# Підказка:
# Напишіть команду для перевірки статусу Docker Daemon на Linux.
#
# Вимоги:
# • Користувач повинен перевірити наявність значка Docker у системному треї для підтвердження роботи Docker Daemon на Windows та macOS.
# • Користувач повинен виконати команду `systemctl status docker` у терміналі, щоб перевірити статус Docker Daemon на Linux.

# Script for checking the Docker Daemon status on Linux
sudo systemctl status docker