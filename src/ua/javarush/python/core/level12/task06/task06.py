# Appending Data to a File

# Write a program that opens the file example.txt in append mode
# and adds the lines "We added this line." and "And this one too."

### 🇺🇦 Ukrainian version:

# Додавання даних у файл

# Напишіть програму, яка відкриває файл example.txt у режимі додавання і
# додає в нього рядки "Ми додали цю лінію." і "І цю теж."

# Write your code here
file = open('example.txt', 'a')
file.write("Ми додали цю лінію.\n")
file.write("І цю теж.\n")
file.close()
