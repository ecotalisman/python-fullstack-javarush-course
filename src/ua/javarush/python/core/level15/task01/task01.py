# Real Array

# Create an array using the array module.
# Add 10 random numbers between 0 and 1000. Sort it and print it to the screen.
# Do not use the list class.

### 🇺🇦 Ukrainian version:

# Справжній масив.

# Створи масив з використанням бібліотеки array.
# Додай у нього 10 випадкових чисел від 0 до 1000. Відсортуй і виведи на екран.
# Клас list використовувати не можна.

# Write your code here
import array as arr
import random

my_arr = arr.array("i", [])
for i in range(10):
    my_arr.append(random.randint(0, 1000))

sorted_arr = arr.array("i", sorted(my_arr))
print(sorted_arr)
