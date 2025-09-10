# Reading a File

# Write a program that opens the file example.txt for reading,
# reads its contents, and prints them to the screen.
# After that, close the file.

### 🇺🇦 Ukrainian version:

# Читання файлу.

# Напиши програму, яка відкриває файл example.txt для читання, читає його вміст і виводить його на екран.
# Після цього закрий файл.

# Write your code here
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()