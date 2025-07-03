# Lambda squared

# Write a program that uses a lambda function to square
# each element of a list of numbers using the map() function. The program should:
# Create a list of numbers.
# Use map() and a lambda function to square each number.
# Print the result.

### 🇺🇦 Ukrainian version:

# Лямбда в квадраті.

# Напишіть програму, яка використовує лямбда-функцію для піднесення до квадрату
# кожного елемента списку чисел з використанням функції map(). Програма повинна:
# Створити список чисел.
# Використовувати map() та лямбда-функцію для піднесення кожного числа до квадрату.
# Вивести результат.

# Write your code here
squared_numbers = list(map(lambda x: x ** 2, [1, 2, 3]))
print(squared_numbers)