# Cold Keys

# Write a program that creates several frozenset objects and uses them as keys in a dictionary.
# The program should:
# Create two frozensets from lists.
# Create a dictionary where the keys are frozensets and the values are strings.
# Display the dictionary.

### 🇺🇦 Ukrainian version:

# Холодні ключі

# Напишіть програму, яка створює кілька об'єктів типу frozenset та використовує їх в якості ключів у словнику.
# Програма повинна:
# Створити два frozenset із списків.
# Створити словник, де ключами є frozenset, а значеннями рядки.
# Вивести словник.

# Write your code here
fset1 = frozenset(["a", "b", "c"])
fset2 = frozenset(["def"])
d = {fset1: "one", fset2: "second"}
print(d)