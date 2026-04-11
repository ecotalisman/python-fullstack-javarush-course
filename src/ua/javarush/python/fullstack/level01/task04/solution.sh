# Installing Docker on Ubuntu

You need to install **Docker Engine** on Ubuntu. Follow the main steps, starting with updating the package list and ending with checking the installed Docker version:

1. Update the package list.
2. Install the required packages.
3. Add the Docker GPG key.
4. Add the Docker repository.
5. Install Docker Engine.
6. Start Docker and configure it to launch automatically on system startup.
7. Display the Docker version.

# Installing Docker on Ubuntu

You need to install **Docker Engine** on Ubuntu. Follow the main steps, starting from updating the package list and ending with checking the installed Docker version:

1. Update the package list.
2. Install the required packages.
3. Add the Docker GPG key.
4. Add the Docker repository.
5. Install Docker Engine.
6. Start Docker and configure it to launch automatically.
7. Display the Docker version.

## Requirements:
- Update the package list using the appropriate command to ensure that all packages in the system are up to date.
- Install the packages required for working with HTTPS and managing repositories using the package installation command.
- Add the official Docker GPG key to ensure secure downloading of packages from the Docker repository.
- Add the Docker repository to the package sources list so that Docker can be installed from the official source.
- Install Docker Engine, start it, and configure it to start automatically when the system boots.
- Display the installed Docker version using the `docker --version` or `docker version` command.

---

# Встановлення Docker на Ubuntu

Вам необхідно встановити **Docker Engine** на Ubuntu. Виконайте основні кроки, починаючи з оновлення пакетів і закінчуючи перевіркою встановленої версії Docker:

1. Оновіть список пакетів.
2. Встановіть необхідні пакети.
3. Додайте GPG ключ Docker.
4. Додайте Docker репозиторій.
5. Встановіть Docker Engine.
6. Запустіть Docker і налаштуйте його для автозапуску.
7. Відобразіть версію Docker.

## Вимоги:
- Оновіть список пакетів з використанням команди, щоб гарантувати, що всі пакети в системі актуальні.
- Встановіть пакети, необхідні для роботи з HTTPS та управління репозиторіями, використовуючи команду встановлення пакетів.
- Додайте офіційний GPG ключ Docker, щоб забезпечити безпеку завантаження пакетів із Docker репозиторію.
- Додайте Docker репозиторій у список джерел пакетів, щоб мати можливість встановлювати Docker із офіційного джерела.
- Встановіть Docker Engine, запустіть його і налаштуйте для автоматичного старту при завантаженні системи.
- Виведіть версію встановленого Docker за допомогою команди `docker --version` або `docker version`.

# Updating the package list
sudo apt-get update

# Installing the required packages
sudo apt-get install \
   ca-certificates \
   curl \
   gnupg \
   lsb-release

# Adding the Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Adding the Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Updating the package list after adding the Docker repository
sudo apt-get update

# Installing Docker Engine
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Starting Docker and configuring it to launch automatically
sudo systemctl start docker
sudo systemctl enable docker

# Checking the Docker version
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
sudo docker --version