# Using the with Statement for File Handling

# Write a program that opens the file example.txt in append mode
# and writes the line "New line." into it.
# The program should properly handle the FileNotFoundError exception,
# ensuring the file is closed in any case.
# Use the with statement for automatic file closing.

### 🇺🇦 Ukrainian version:

# Використання оператора with для роботи з файлами

# Напишіть програму, яка відкриває файл example.txt в режимі додавання, записує в нього рядок "Нова лінія.".
# Потрібно коректно обробляти виняток FileNotFoundError, закриваючи файл у будь-якому випадку.
# Потрібно використовувати оператор with для автоматичного закриття файлу.

# Write your code here
try:
    with open('example.txt', 'a', encoding='utf-8') as file:
        file.write("Нова лінія.")
except FileNotFoundError as e:
    print(f"File not found: {e}")