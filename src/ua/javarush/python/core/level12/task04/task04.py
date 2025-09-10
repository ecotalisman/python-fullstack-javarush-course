# Iterating Over File Lines

# Write a program that reads the file example.txt line by line using an iterator
# and prints each line to the screen.

### 🇺🇦 Ukrainian version:

# Ітерація по рядках файлу

# Напиши програму, яка читає файл example.txt построчно, використовуючи ітератор, і виводить кожен рядок на екран.

# Write your code here
file = open('example.txt', 'r')
for line in file:
    print(line.strip())
file.close()
