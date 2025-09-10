# Reading the Entire File

# Write a program that reads and prints the full contents of the file example.txt.

### 🇺🇦 Ukrainian version:

# Читання всього файлу

# Напишіть програму, яка читає і виводить на екран вміст файлу example.txt повністю.

# Write your code here
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()