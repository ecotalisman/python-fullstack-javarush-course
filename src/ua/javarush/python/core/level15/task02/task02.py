# Two-Dimensional Array

# Create a 10x10 square array using the array module.
# Fill it as a multiplication table x*y. Print it to the screen.
# Note: x from 1 to 10 and y from 1 to 10.
# Do not use the list class.

### 🇺🇦 Ukrainian version:

# Двовимірний масив.

# Створи квадратний масив 10х10 з використанням бібліотеки array.
# Заповни його як таблицю множення x*y. Виведи на екран.
# Примітка: х від 1 до 10 та y від 1 до 10.
# Клас list використовувати не можна.

# Write your code here
import array

x = 10
y = 10

matrix = array.array("I", (0 for _ in range(x * y)))

for i in range(x):
    for j in range(y):
        matrix[i * y + j] = (i + 1) * (j + 1)

for i in range(x):
    base = i * y
    for j in range(y):
        print(matrix[base + j], end=' ')
    print()
