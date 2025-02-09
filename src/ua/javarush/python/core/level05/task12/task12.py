# Clear List

# Write a program that creates a list of 10 integers.
# Using a for loop, replace all even elements in the list with the string "even".
# The program should display the updated list.

### 🇺🇦 Ukrainian version:

# Чіткий список

# Напишіть програму, яка створює список з 10 цілих чисел.
# За допомогою циклу for замініть усі парні елементи списку на рядок "парне".
# Програма повинна вивести оновлений список.

# Write your code here
l = [n for n in range(1, 11)]

print([x if x % 2 != 0 else "парне" for x in l])