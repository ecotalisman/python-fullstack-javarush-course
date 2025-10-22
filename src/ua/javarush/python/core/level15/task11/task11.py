# Creating Your Own Array

# Create an array using the numpy library.
# Add 10 random numbers between 0 and 1000. Sort it and print it to the screen.
# Do not use the list class.

### 🇺🇦 Ukrainian version:

# Створюємо свій масив

# Створи масив з використанням бібліотеки numpy.
# Додай в нього 10 випадкових чисел від 0 до 1000. Відсортуй і виведи на екран.
# Клас list використовувати не можна.

# Write your code here
import numpy as np
arr = np.random.randint(0, 1001, size=10)
print(arr)
arr = np.sort(arr)
print(f"After sorting: {arr}")
