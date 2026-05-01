# Managing Logs with Logrotate
# Configure the Logrotate utility to automatically rotate application logs
# stored in the /var/log/myapp/ directory.
# Logs must be compressed and kept for the last 7 days.
#
# Requirements:
# • Logrotate must be configured to process logs located in the /var/log/myapp/ directory.
# • Logs must be automatically compressed after rotation to save space.
# • Compressed logs must be kept for the last 7 days.
# • Logrotate must be configured for automatic log rotation without manual intervention.
#
# ## 🇺🇦 Ukrainian version:
#
# Управління логами за допомогою Logrotate
# Налаштуйте утиліту Logrotate для автоматичної ротації логів додатку,
# які зберігаються в директорії /var/log/myapp/.
# Логи мають стискатися і зберігатися за останні 7 днів.
#
# Вимоги:
# • Logrotate має бути налаштований для обробки логів, які знаходяться в директорії /var/log/myapp/.
# • Логи повинні автоматично стискатися після ротації для економії місця.
# • Зберігати стиснені логи необхідно протягом останніх 7 днів.
# • Logrotate має бути налаштований на автоматичну ротацію логів без ручного втручання.

# Check the Logrotate configuration
sudo logrotate -d /etc/logrotate.d/myapp

# Manually run log rotation for testing
sudo logrotate -f /etc/logrotate.d/myapp