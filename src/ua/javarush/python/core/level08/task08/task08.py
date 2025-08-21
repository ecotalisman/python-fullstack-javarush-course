# Generator Expression

# Write a program that uses a generator expression to create
# a sequence of squares of numbers from 1 to 10. The program should:
# Create a generator expression for generating squares of numbers.
# Use this generator to output all values of the sequence.

### 🇺🇦 Ukrainian version:

# Генератор виразів.

# Напишіть програму, яка використовує генераторне вираз для створення
# послідовності квадратів чисел від 1 до 10. Програма повинна:
# Створити генераторне вираз для генерації квадратів чисел.
# Використовувати цей генератор для виведення всіх значень послідовності.

# Write your code here
squares = (x ** 2 for x in range(1, 11))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))