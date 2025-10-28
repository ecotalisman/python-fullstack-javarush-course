# Linear Search

# Write a function that performs a linear search for a given element in an array of numbers.
# The function should return the index of the first found element or -1 if the element is not found.
# You may use the list class, but do not call its built-in methods.

### 🇺🇦 Ukrainian version:

# Лінійний пошук

# Напишіть функцію, яка виконує лінійний пошук заданого елемента в масиві чисел.
# Функція повинна повертати індекс першого знайденого елемента або -1, якщо елемент не знайдений.
# Класом list користуватися можна, викликати його функції - ні.

# Write your code here
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage:

arr = [10, 20, 30, 40, 50]
target = 30
print(linear_search(arr, target))  # Вивід: 2

