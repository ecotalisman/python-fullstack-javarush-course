# Running in Detached Mode
# Start all services defined in the docker-compose.yml file in detached mode
# so that the containers continue running even if you close the terminal.
#
# Requirements:
# • To start all services in detached mode, the `docker compose up -d` command must be used,
#   which allows the containers to run in detached mode.
# • All services must be defined in the `docker-compose.yml` file, which must be available
#   in the current working directory when the startup command is executed.
# • The containers must continue running in detached mode even if the terminal
#   from which the command was executed is closed.
#
# ## 🇺🇦 Ukrainian version:
#
# Запуск у фоновому режимі
# Запустіть усі сервіси, визначені у файлі docker-compose.yml, у фоновому режимі,
# щоб контейнери працювали, навіть якщо ви закриєте термінал.
#
# Вимоги:
# • Для запуску всіх сервісів у фоновому режимі необхідно використовувати команду `docker compose up -d`,
#   яка дозволяє запустити контейнери у фоновому режимі (detached mode).
# • Усі сервіси повинні бути визначені у файлі `docker-compose.yml`, який повинен бути доступний
#   у поточному робочому каталозі під час виконання команди запуску.
# • Контейнери повинні продовжувати свою роботу у фоновому режимі, навіть якщо термінал,
#   із якого була виконана команда, закритий.

# Running all services in detached mode
docker compose up -d