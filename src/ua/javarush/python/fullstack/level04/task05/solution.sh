# Installing Docker and Docker Compose on Linux
# You need to install Docker and Docker Compose on the Ubuntu operating system.
# Complete all the required steps to install Docker and Docker Compose,
# and then verify that the installation was completed correctly.
#
# Steps:
#
# 1. Install Docker on your system.
#
# 2. Docker must work without requiring the sudo command.
#
# 3. Install the Docker Compose plugin.
#
# 4. Display the Docker Compose version.
#
# Requirements:
# • The script must contain the steps to install Docker on the Ubuntu operating system.
# • Docker must be configured in such a way that it can run without requiring the sudo command.
# • The script must include the steps to install the Docker Compose plugin on the system.
# • After installation, the script must display the Docker Compose version to verify that the installation is correct.
#
# ## 🇺🇦 Ukrainian version:
# Встановлення Docker і Docker Compose на Linux
# Вам потрібно встановити Docker і Docker Compose на операційну систему Ubuntu.
# Виконайте всі необхідні кроки для встановлення Docker і Docker Compose,
# а потім перевірте, що встановлення виконане коректно.
#
# Кроки:
#
# 1. Встановіть Docker на вашу систему.
#
# 2. Docker повинен працювати без необхідності використання команди sudo.
#
# 3. Встановіть плагін Docker Compose.
#
# 4. Відобразіть версію Docker Compose.
#
# Вимоги:
# • Скрипт повинен містити кроки для встановлення Docker на операційну систему Ubuntu.
# • Docker має бути налаштований таким чином, щоб він міг працювати без необхідності використання команди sudo.
# • Скрипт повинен включати кроки для встановлення плагіна Docker Compose на систему.
# • Після встановлення скрипт повинен відобразити версію Docker Compose для перевірки коректності встановлення.

# Updating the package list and installing the required dependencies
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Adding the official Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Adding the Docker repository to the APT sources list
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Installing Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Adding the current user to the docker group to use Docker without sudo
sudo usermod -aG docker $USER

# Applying the user group changes (you will need to log out and log back in)
newgrp docker

# Installing Docker Compose as a plugin
sudo apt-get install docker-compose-plugin

# Verifying the Docker Compose installation by displaying its version
docker compose --version