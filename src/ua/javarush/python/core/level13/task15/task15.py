# Reading Mail from a POP3 Server

# Write a program that connects to a POP3 server, authenticates,
# fetches the list of messages, and displays the content of the latest one.

### 🇺🇦 Ukrainian version:

# Читання пошти з POP3-сервера

# Напишіть програму, яка підключається до POP3-сервера, аутентифікується,
# отримує список листів та відображає вміст останнього листа.

# Write your code here
import poplib

HOST = "pop3.mailtrap.io"
PORT = 1100
USERNAME = "dd5e691fc1159a"
PASSWORD = "ca040510a7ffea"

mailbox = poplib.POP3(HOST, PORT, timeout=15)
mailbox.stls()
mailbox.user(USERNAME)
mailbox.pass_(PASSWORD)

num_message = len(mailbox.list()[1])
print(f"Total number of emails: {num_message}")

if num_message > 0:
    response, lines, octets = mailbox.retr(num_message)
    message = "\n".join(line.decode("utf-8", errors="replace") for line in lines)
    print(f"Content of the last email: ")
    print(message)

mailbox.quit()
