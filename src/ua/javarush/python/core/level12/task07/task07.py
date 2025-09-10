# Handling File Errors

# Write a program that opens the file example.txt in append mode
# and writes the line "New line." into it.
# Handle the FileNotFoundError exception properly, making sure the file is closed in any case.

### 🇺🇦 Ukrainian version:

# Обробка помилок при роботі з файлами

# Напишіть програму, яка відкриває файл example.txt в режимі додавання, записує в нього рядок "Нова лінія.".
# Потрібно коректно обробляти виключення FileNotFoundError, закриваючи файл у будь-якому випадку.

# Write your code here
file = None
try:
    file = open('example.txt', 'a', encoding="utf-8")
    file.write("Нова лінія.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    if file:
        file.close()
