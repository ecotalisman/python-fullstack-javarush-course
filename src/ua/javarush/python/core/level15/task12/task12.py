# Creating a Two-Dimensional Array

# Create a 10x10 square array using the numpy library.
# Fill it as a multiplication table x*y. Print it to the screen.
# Do not use the list class.

### 🇺🇦 Ukrainian version:

# Створюємо двовимірний масив.

# Створи квадратний масив 10х10 з використанням бібліотеки numpy.
# Заповни його як таблицю множення x*y. Виведи на екран.
# Клас list використовувати не можна.

# Write your code here
import numpy as np

x = np.arange(10)
y = np.arange(10)
result_2d = np.outer(x, y)

print(result_2d)
