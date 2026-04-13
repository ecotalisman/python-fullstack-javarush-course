# Mounting a Directory into a Container
# Run a container based on the Ubuntu image with a mounted directory.
# Mount the local directory /host/data to the container directory /container/data
# to provide access to the data inside the container.
#
# Requirements:
# • The container must be created and started based on the official Ubuntu image from Docker Hub.
# • The local directory /host/data must be mounted into the container at /container/data to provide access to the data.
# • Inside the container, there must be full access (read and write) to the files and directories located in
# the mounted /container/data directory.
#
# ## 🇺🇦 Ukrainian version:
#
# Монтування директорії в контейнер
# Запустіть контейнер на основі образу ubuntu з примонтованою директорією.
# Змонуйте локальну директорію /host/data у контейнерну директорію /container/data,
# щоб забезпечити доступ до даних всередині контейнера.
#
# Вимоги:
# • Контейнер має бути створений і запущений на основі офіційного образу Ubuntu з Docker Hub.
# • Локальна директорія /host/data має бути змонтована в контейнер за шляхом /container/data для забезпечення доступу
# до даних.
# • Всередині контейнера має бути повний доступ (читання і запис) до файлів і директорій, що знаходяться в змонтованій
# директорії /container/data.

# Create the directory on the host if it does not exist
mkdir -p /host/data

# Run the Ubuntu container with the mounted directory
docker run --name my_data_container -v /host/data:/container/data ubuntu