# Square List

# Write a program that creates a list of squares of numbers from -100 to 100. Use the list() function to create the list.
# Finally, print the resulting list to the screen.

### 🇺🇦 Ukrainian version:

# Квадратний список

# Напиши програму, яка створює список квадратів чисел від -100 до 100. Для створення списку використовуй функцію list().
# Наприкінці виведи отриманий список на екран.

# Write your code here
my_list = list(num ** 2 for num in range(-100, 101))
print(my_list)