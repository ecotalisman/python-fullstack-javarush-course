# File existence check

# Write a program that checks whether the file example.txt exists,
# and if it does, deletes it.

### 🇺🇦 Ukrainian version:

# Перевірка існування файлу

# Напишіть програму, яка перевіряє, чи існує файл example.txt,
# і якщо існує, видаляє його.

# Write your code here
import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print("File exists and delete")
else:
    print("File does not exist")
