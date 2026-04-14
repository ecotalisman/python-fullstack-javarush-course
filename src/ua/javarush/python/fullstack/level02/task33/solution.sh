# Downloading an Image from Docker Hub
# Download the latest official Nginx image from Docker Hub to your local machine.
# After that, check whether the image appears among those downloaded to your system
# using the docker images command.
#
# Requirements:
# • A command must be used to download the latest official Nginx image from Docker Hub to the local machine.
# • The docker images command must be used to verify the presence of the downloaded Nginx image among locally
# stored images.
# • The official Nginx image available on Docker Hub must be downloaded, which means using the nginx repository
#   without specifying a user or organization.
#
# ## 🇺🇦 Ukrainian version:
#
# Завантаження образу з Docker Hub
# Завантажте останній офіційний образ Nginx з Docker Hub на свою локальну машину.
# Після цього перевірте, чи з'явився образ серед завантажених у вашу систему,
# за допомогою команди docker images.
#
# Вимоги:
# • Необхідно використовувати команду, щоб завантажити останній офіційний образ Nginx з Docker Hub на локальну машину.
# • Потрібно використовувати команду docker images для перевірки наявності завантаженого образу Nginx серед локально
# збережених образів.
# • Потрібно завантажити саме офіційний образ Nginx, доступний на Docker Hub, що передбачає використання репозиторію nginx без зазначення користувача або організації.

# Command to download the latest official Nginx image from Docker Hub
docker pull nginx:latest

# Command to check whether the downloaded image is present
docker images