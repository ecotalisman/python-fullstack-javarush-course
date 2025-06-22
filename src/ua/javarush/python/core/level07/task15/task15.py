# Freezing

# Write a program that creates several frozenset objects from different iterable objects (a list, a string).
# The program should:
# Create a frozenset from a list.
# Create a frozenset from a string.
# Perform union, intersection, difference, and symmetric difference of the two frozensets.
# Display the results of each operation.

### 🇺🇦 Ukrainian version:

# Замороження

# Напишіть програму, яка створює декілька об'єктів типу frozenset із різних ітерованих об'єктів (список, рядок).
# Програма повинна:
# Створити frozenset із списку.
# Створити frozenset із рядка.
# Виконати об'єднання, перетин, різницю та симетричну різницю двох frozenset множин.
# Вивести результати кожної операції.

# Write your code here
fset1 = frozenset(["a", "b", "c", "d", "e"])
fset2 = frozenset("abczx")
print(fset1.union(fset2))
print(fset1.intersection(fset2))
print(fset1.difference(fset2))
print(fset1.symmetric_difference(fset2))
