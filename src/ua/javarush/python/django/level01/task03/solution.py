# SQL Injection
#
# There is a Python program.
# You need to "break" it — write an SQL injection:
# you need to log in as admin
# without knowing the password.
#
# Hint:
# call the login() method
# with the required arguments.
#
# Program code:
#
# ```python
#
# import sqlite3
#
# # Create a database in memory
# # for this example
#
# conn = sqlite3.connect(":memory:")
#
# cursor = conn.cursor()
#
# # Create a users table
#
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
#
# # Add test data
#
# cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
#
# cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
#
# conn.commit()
#
# # Function that demonstrates the vulnerability
#
# def login(username, password):
#
#     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#
#     print("\n[SQL query]:", query) # Print the query for demonstration purposes
#
#     cursor.execute(query)
#
#     user = cursor.fetchone()
#
#     if user:
#
#         print("✅ Login successful: ", user)
#
#     else:
#
#         print("❌ Login failed")
#
# # Regular login
# # works correctly
#
# login("admin", "1234")
#
# # Close the connection
#
# conn.close()
#
# ```
#
# Requirements:
#
# 1. You need to provide a username
#    and/or password string
#    that will change the execution
#    of the query so that login as admin
#    happens without knowing the password.
# 2. The login() method must allow
#    the user to authorize as admin,
#    even if the password is unknown.
#
# 🇺🇦 Ukrainian version:
#
# SQL-інʼєкція
#
# Є програма на Python.
# Тобі потрібно "зламати" її —
# написати SQL-інʼєкцію:
# потрібно залогінитись під адміном,
# не знаючи пароль.
#
# Підказка:
# виклич метод login()
# з потрібними аргументами.
#
# Код програми:
#
# ```python
#
# import sqlite3
#
# # Створюємо базу даних у памʼяті
# # для прикладу
#
# conn = sqlite3.connect(":memory:")
#
# cursor = conn.cursor()
#
# # Створюємо таблицю користувачів
#
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
#
# # Додаємо тестові дані
#
# cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
#
# cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
#
# conn.commit()
#
# # Функція, яка показує уразливість
#
# def login(username, password):
#
#     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#
#     print("\n[SQL-запит]:", query) # Виводимо запит для наочності
#
#     cursor.execute(query)
#
#     user = cursor.fetchone()
#
#     if user:
#
#         print("✅ Вхід виконано: ", user)
#
#     else:
#
#         print("❌ Помилка входу")
#
# # Звичайний вхід
# # працює коректно
#
# login("admin", "1234")
#
# # Закриваємо зʼєднання
#
# conn.close()
#
# ```
#
# Вимоги:
#
# 1. Потрібно надати рядок username
#    і/або password,
#    яка змінить виконання запиту так,
#    щоб відбувся вхід під адміном
#    без знання пароля.
# 2. Метод login() має дозволити
#    користувачу авторизуватися під адміном,
#    навіть якщо пароль невідомий.

import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")  # Create a database in memory
        self.cursor = self.conn.cursor()
        self._create_table()
        self._insert_test_data()

    def _create_table(self):
        """Creates a users table."""
        self.cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY, 
                username TEXT, 
                password TEXT
            )
        """)

    def _insert_test_data(self):
        """Adds test data to the users table."""
        users = [
            ("admin", "1234"),
            ("user", "password")
        ]
        self.cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
        self.conn.commit()

    def login(self, username: str, password: str):
        """Demonstrates a vulnerability by executing an unsafe SQL query."""
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("\n[SQL query]:", query)  # Prints the query for demonstration purposes

        self.cursor.execute(query)
        user = self.cursor.fetchone()

        if user:
            print("✅ Login successful: ", user)
        else:
            print("❌ Login failed")

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()


# Using the class
if __name__ == "__main__":
    db = DatabaseManager()
    # db.login("admin", "unknown") # Log in as admin

    db.login("admin'--", "unknown") # Log in as admin
    db.close_connection()