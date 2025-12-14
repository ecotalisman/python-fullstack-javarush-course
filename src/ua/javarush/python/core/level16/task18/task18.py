# Authorization (Login Simulation)

# Write a program that simulates user login.
# The program must include functions login(email, password) and register(email, password).
# When registering a user, call register and add the user to the users list.
# Store a hash instead of the plain password.
# When logging in, call login and verify that the password hash matches one of the stored hashes.

### 🇺🇦 Ukrainian version:

# Авторизація

# Напиши програму імітації логіну користувачів.
# Програма повинна містити функцію login(email, password) і register(email, password).
# При реєстрації користувача потрібно викликати функцію register і додати користувача в список користувачів.
# Замість пароля потрібно зберігати його hash.
# При логіні користувача потрібно викликати функцію login, де перевірити, що hash пароля співпадає з одним із збережених хешів.

import hashlib

users = {}

def hash_password(password):
    # Write your code here
    return hashlib.sha256(password.encode()).hexdigest()

def register(email, password):
    # Write your code here
    if email in users:
        print("User already exists")
        return
    users[email] = hash_password(password)
    print("Create User")

def login(email, password):
    # Write your code here
    if email not in users:
        print("User not found")
        return
    if hash_password(password) == users[email]:
        print("Password is correct")
    else:
        print("Password is wrong")


# Example usage
register("user@example.com", "securepassword123")
login("user@example.com", "securepassword123")
login("user@example.com", "wrongpassword")
