# Opening an Interactive Bash Session
# Open an interactive session inside the web_server container so that commands can be executed
# in the container terminal in real time. Use the docker exec command with the required parameters.
#
# Requirements:
# • The docker exec command must be used to open an interactive Bash session inside the web_server container.
# • The docker exec command must be applied to the container named web_server.
# • The opened session must allow commands to be executed in the container terminal in interactive mode,
#   meaning it must provide the ability to enter commands and receive their output in real time.
# • The interactive session must be opened using the Bash shell to ensure compatibility with the commands
#   that will be executed inside the container.
#
# ## 🇺🇦 Ukrainian version:
#
# Відкриття інтерактивної сесії Bash
# Відкрийте інтерактивну сесію всередині контейнера web_server, щоб можна було виконувати команди
# в терміналі контейнера в режимі реального часу. Використовуйте команду docker exec з необхідними параметрами.
#
# Вимоги:
# • Для відкриття інтерактивної сесії Bash всередині контейнера web_server необхідно використовувати команду docker exec.
# • Команда docker exec повинна бути застосована до контейнера з іменем web_server.
# • Відкрита сесія повинна дозволяти виконувати команди в терміналі контейнера в інтерактивному режимі,
#   тобто забезпечувати можливість вводу і отримання виводу команд в режимі реального часу.
# • Інтерактивна сесія повинна бути відкрита з використанням командної оболонки Bash, щоб забезпечити
#   сумісність із командами, які будуть виконуватися всередині контейнера.

# Opening an interactive Bash session inside the web_server container
docker exec -it web_server /bin/bash