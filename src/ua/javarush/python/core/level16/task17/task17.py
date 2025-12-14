# Password Hashing

# Write a program for hashing passwords.
# Your task is to create a function that takes a password string
# and returns its hash value.

### 🇺🇦 Ukrainian version:

# Хешування паролів

# Напишіть програму для хешування паролів.
# Ваше завдання — створити функцію, яка приймає рядок пароля
# і повертає його хеш-значення.

import hashlib

def hash_password(password: str) -> str:
# Write your code here
    return hashlib.sha256(password.encode()).hexdigest()


# Example usage:
password = "my_secure_password"
hashed_password = hash_password(password)
print(hashed_password)
