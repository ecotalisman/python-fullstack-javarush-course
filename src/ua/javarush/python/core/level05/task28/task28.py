# The Most Important Tuple

# Write a program that creates a tuple containing several nested tuples with integers.
# The program should use a for loop to find the maximum element in the nested tuples and display the result.

### 🇺🇦 Ukrainian version:

# Найголовніший кортеж

# Напишіть програму, яка створює кортеж, що містить декілька вкладених кортежів із цілих чисел.
# Програма повинна використовувати цикл for для пошуку максимального елемента у вкладених кортежах і вивести результат.

# Write your code here
l = list(range(10))
t = tuple([(l[i], l[i + 1], l[i + 2]) for i in range(1, 10, 3)])
print(t)
x = list([i for sub in t for i in sub])
print(max(x))
