# File Access Modes

# Write a program that creates or opens the file example.txt in write mode
# and writes the string "Hello, World!" into it.
# Then open the file in append mode and add the string "Appended text.".

### 🇺🇦 Ukrainian version:

# Режими доступу

# Напишіть програму, яка створює або відкриває файл example.txt у режимі запису та
# записує в нього рядок "Hello, World!".
# Потім відкрийте файл у режимі додавання та додайте рядок "Appended text.".

# Write your code here
file = open('example.txt', 'w')
file.write("Hello, World!")
file = open('example.txt', 'a')
file.write("\nAppended text.")
file.close()
