# Sending Email via SMTP

# Write a program that connects to an SMTP server,
# authenticates, and sends an email.

### 🇺🇦 Ukrainian version:

# Відправка пошти за допомогою SMTP

# Напишіть програму, яка підключається до SMTP-сервера,
# аутентифікується і відправляє листа.

# Write your code here
import smtplib

HOST = "smtp.mailtrap.io"
PORT = 2525
USERNAME = "dd5e691fc1159a"
PASSWORD = "ca040510a7ffea"

from_addr = "test@example.com"
to_addr = "anyone@example.com"
subject = "Test email"
body = "Hello from Python via Mailtrap!"

message = f"From: {from_addr}\nTo: {to_addr}\nSubject: {subject}\n\n{body}"

try:
    server = smtplib.SMTP(HOST, PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(from_addr, to_addr, message)
    print("Email sent successfully!")
except Exception as err:
    print(f"Error while sending email: {err}")
finally:
    server.quit()
