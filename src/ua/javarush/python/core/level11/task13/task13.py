# Default Parameters

# Write 2 functions: def foo(bar=[]) and foo_correct(bar=None).
# Each function takes a list and adds the element "baz" to it.
# If the list is not passed, the function should use a new empty list.
# Show how using a mutable object as a default value can lead to unexpected behavior,
# and fix this in the second function.

### 🇺🇦 Ukrainian version:

# Параметри за замовчуванням.

# Напишіть 2 функції: def foo(bar=[]) і foo_correct(bar=None).
# Кожна функція приймає список і додає до нього елемент "baz".
# Якщо список не переданий, функція повинна використовувати новий порожній список.
# Покажіть, як використання змінюваного об'єкта як значення за замовчуванням може призвести до несподіваної поведінки,
# і виправте це (у другій функції).

# Write your code here
def foo(bar=[]):
    bar.append("baz")
    return bar

def foo_correct(bar=None):
    if bar is None:
        bar = []
    bar.append("baz")
    return bar

print(foo())
print(foo())
print(foo())

# Checking the corrected function
print(foo_correct())  # Виводить: ['baz']
print(foo_correct())  # Виводить: ['baz']
print(foo_correct())  # Виводить: ['baz']

# Checking with passing a list
lst = [1, 2, 3]
print(foo_correct(lst))  # Виводить: [1, 2, 3, "baz"]
print(foo_correct(lst))  # Виводить: [1, 2, 3, "baz", "baz"]