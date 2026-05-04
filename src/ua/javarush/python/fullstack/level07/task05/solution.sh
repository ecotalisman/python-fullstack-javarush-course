# Analyzing Container Disk Operations
# Start a container with an application that actively uses the disk
# for reading and writing data. Use the docker stats or docker inspect command
# to monitor the number of input/output (I/O) operations.
# Visually evaluate how this affects container performance.
#
# Requirements:
# • The container must be started with an application that intensively uses the disk
#   for read and write operations.
# • The docker stats or docker inspect commands must be used
#   to monitor the number of input/output (I/O) operations in the container.
# • It is necessary to visually evaluate how the number of I/O operations
#   affects the overall performance of the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Аналіз дискових операцій контейнера
# Запустіть контейнер із застосунком, який активно використовує диск
# для читання та запису даних. Використовуйте команду docker stats або docker inspect
# для моніторингу кількості операцій введення/виведення (I/O).
# Візуально оцініть, як це впливає на продуктивність контейнера.
#
# Вимоги:
# • Контейнер повинен бути запущений із застосунком, який інтенсивно використовує диск
#   для операцій читання та запису даних.
# • Необхідно використовувати команди docker stats або docker inspect
#   для моніторингу кількості операцій введення/виведення (I/O) у контейнері.
# • Потрібно візуально оцінити, як кількість операцій I/O впливає
#   на загальну продуктивність контейнера.

# Building the Docker image
docker build -t disk_io_app .

# Running the Docker container
docker run -d --name disk_io_container disk_io_app

# Monitoring input/output operations
docker inspect disk_io_container