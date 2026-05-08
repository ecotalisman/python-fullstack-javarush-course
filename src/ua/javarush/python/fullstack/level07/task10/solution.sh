# Installing Prometheus
# Configure container monitoring using Prometheus.
# Start by installing Prometheus on your local server.
# Download and extract the archive, then move the binary files
# to the /usr/local/bin/ directory.
#
# Requirements:
# • Prometheus must be installed on the local server,
#   starting with downloading the appropriate archive.
# • The downloaded Prometheus archive must be extracted
#   for further use of its contents.
# • The extracted Prometheus binary files must be moved
#   to the /usr/local/bin/ directory on the local server
#   to ensure that they are available from the command line.
#
# ## 🇺🇦 Ukrainian version:
#
# Встановлення Prometheus
# Налаштуйте моніторинг контейнерів за допомогою Prometheus.
# Почніть із встановлення Prometheus на ваш локальний сервер.
# Завантажте та розпакуйте архів,
# а потім перемістіть бінарні файли в директорію /usr/local/bin/.
#
# Вимоги:
# • Prometheus має бути встановлений на локальний сервер,
#   починаючи із завантаження відповідного архіву.
# • Завантажений архів Prometheus необхідно розпакувати
#   для подальшого використання його вмісту.
# • Розпаковані бінарні файли Prometheus мають бути переміщені
#   до директорії /usr/local/bin/ на локальному сервері
#   для забезпечення їх доступності з командного рядка.

# First, download the latest version of Prometheus from the official website
wget https://github.com/prometheus/prometheus/releases/download/v2.30.3/prometheus-2.30.3.linux-amd64.tar.gz

# Extract the archive:
tar xvfz prometheus-*.tar.gz

# Move the binary files to /usr/local/bin:
sudo mv prometheus-2.30.3.linux-amd64/prometheus /usr/local/bin/
sudo mv prometheus-2.30.3.linux-amd64/promtool /usr/local/bin/