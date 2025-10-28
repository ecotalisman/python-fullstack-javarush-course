# Searching is Easy

# Write a function that performs a linear search to check whether
# a given element exists in a list of strings.
# The function should return True if the element is found,
# and False if the element is not present.
# You may use the list class, but do not call its built-in methods.

### 🇺🇦 Ukrainian version:

# Пошук - це легко

# Напишіть функцію, яка виконує лінійний пошук для перевірки наявності заданого елемента в списку рядків.
# Функція повинна повертати True, якщо елемент знайдено, і False, якщо елемент відсутній.
# Користуватися класом list можна, викликати його функції - ні.

# Write your code here

def linear_search(arr, target):
    for ind, el in enumerate(arr):
        if el == target:
            return True
    return False

products = ["milk", "water", "bread"]
target = "water"
found = linear_search(products, target)
print(f"Element {target} {'found' if found else 'not found'}")
