# Negative Tuples

# Write a program that creates a tuple with 7 elements entered by the user.
# Then, the program should print the third-to-last and the second-to-last elements of the tuple using negative indices.

### 🇺🇦 Ukrainian version:

# Від'ємні кортежі

# Напишіть програму, яка створює кортеж з 7 елементів, запитуваних у користувача.
# Потім програма повинна вивести третій з кінця та передостанній елемент кортежу, використовуючи від'ємні індекси.

# Write your code here
l = list(input("Enter elements: ") for l in range(7))
t = tuple(l)
print(t[-3])
print(t[-2])