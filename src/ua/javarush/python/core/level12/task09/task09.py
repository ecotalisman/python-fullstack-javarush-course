# Reading a Binary File

# Write a program that reads the binary file example.bin
# and prints its contents to the console as bytes.

### 🇺🇦 Ukrainian version:

# Читання бінарного файлу

# Напишіть програму, яка читає бінарний файл example.bin і виводить його вміст у консоль у вигляді байтів.

# Write your code here
file = open('example.bin', 'rb')
print(file.read())
file.close()