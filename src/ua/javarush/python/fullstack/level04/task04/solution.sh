# Restarting the Database Service
# After starting the application, restart only the MySQL database service
# without stopping the web service.
#
# Requirements:
# • The application must include in its logic the ability to restart only the MySQL database service without the need to stop or restart the web service.
# • Docker commands must be used to manage services in order to ensure an isolated restart of only MySQL.
# • During the MySQL restart, the web service must remain available and continue functioning without failures or performance loss.
#
# ## 🇺🇦 Ukrainian version:
# Перезапуск сервісу бази даних
# Після запуску додатку перезапустіть лише сервіс бази даних MySQL, не зупиняючи веб-сервіс.
#
# Вимоги:
# • Додаток повинен включати в свою логіку можливість перезапуску тільки сервісу бази даних MySQL без необхідності зупинки або перезапуску веб-сервісу.
# • Необхідно використовувати команди Docker для керування сервісами, щоб забезпечити ізольований перезапуск тільки MySQL.
# • Під час перезапуску MySQL веб-сервіс повинен залишатися доступним і функціонувати без збоїв або втрати продуктивності.
#
# Restarting the MySQL database service
docker compose restart db