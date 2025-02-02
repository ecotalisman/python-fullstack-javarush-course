# Access Denied

# Write a program that asks the user for a username and password.
# If the username is "admin" and the password is "1234", the program should display "Access granted".
# Otherwise, the program should display "Access denied".

### 🇺🇦 Ukrainian version:

# Доступ заборонено

# Напишіть програму, яка запитує у користувача ім'я користувача та пароль.
# Якщо ім'я користувача дорівнює "admin" і пароль дорівнює "1234", програма повинна вивести повідомлення "Доступ дозволено".
# В іншому випадку програма повинна вивести повідомлення "Доступ заборонено".

# Write your code here
name = input("Enter your name: ")
password = int(input("Enter your password: "))

if name == "admin" and password == 1234:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")