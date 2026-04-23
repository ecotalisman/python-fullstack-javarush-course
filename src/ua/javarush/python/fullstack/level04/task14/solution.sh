# Rebuilding Images and Starting Containers
# Start all services, rebuilding the images before starting the containers.
# This is necessary if changes were made to the Dockerfile or source code and need to be applied.
#
# Requirements:
# • Before starting the containers, all images must be rebuilt to include changes in the Dockerfile or source code.
# • After successfully rebuilding the images, all services must be started in containers.
# • The rebuild must apply all changes made in the Dockerfile or source code to the new images used in the containers.
#
# ## 🇺🇦 Ukrainian version:
#
# Перезбірка образів та запуск
# Запустіть всі сервіси, перезібравши образи перед запуском контейнерів.
# Це необхідно, якщо в Dockerfile або вихідному коді було внесено зміни, і їх потрібно застосувати.
#
# Вимоги:
# • Перед запуском контейнерів має бути виконана перезбірка всіх образів з урахуванням змін у Dockerfile або вихідному коді.
# • Після успішної перезбірки образів необхідно запустити всі сервіси у контейнерах.
# • Перезбірка має застосувати всі внесені зміни у Dockerfile або вихідний код до нових образів, що використовуються у контейнерах.

# Rebuilding the images and starting the containers
docker compose up --build
