# Updating a Service in Swarm
# Update the existing my_web service to the latest version of Nginx using Docker Swarm.
# The service must be updated using the new image version.
#
# Requirements:
# • The my_web service must be updated in the Docker Swarm environment,
#   ensuring that the update happens at the cluster level.
# • When updating the my_web service, the latest available version of the Nginx image must be used.
# • The service name my_web must remain unchanged after updating to the new Nginx version.
# • During the update, zero downtime and uninterrupted operation of the my_web service must be ensured.
#
# ## 🇺🇦 Ukrainian version:
#
# Оновлення сервісу в Swarm
# Оновіть вже існуючий сервіс my_web до останньої версії Nginx,
# використовуючи Docker Swarm. Сервіс повинен оновлюватися з використанням нової версії образу.
#
# Вимоги:
# • Сервіс my_web повинен бути оновлений у середовищі Docker Swarm,
#   гарантуючи, що оновлення відбувається на рівні кластера.
# • При оновленні сервісу my_web необхідно використовувати останню доступну версію образу Nginx.
# • Ім'я сервісу my_web повинно залишитися незмінним після оновлення до нової версії Nginx.
# • Під час оновлення необхідно забезпечити відсутність простою і безперебійну роботу сервісу my_web.

# Initializing Docker Swarm
docker swarm init

# Pulling the latest Nginx image
docker service update --image nginx:latest my_web

# Updating the my_web service so that it uses the latest version of the Nginx image
docker service update \
  --image nginx:latest \
  --update-parallelism 1 \
  --update-delay 10s \
  --update-failure-action rollback \
  my_web
