# Binary Search
from ua.javarush.python.core.level05.task02.task02 import element


# Write a function that performs a binary search for a given element
# in a sorted array of numbers.
# The function should return the index of the found element,
# or -1 if the element is not found.

### 🇺🇦 Ukrainian version:

# Бінарний пошук

# Напишіть функцію, яка виконує бінарний пошук заданого елемента
# в відсортованому масиві чисел.
# Функція повинна повертати індекс знайденого елемента або -1, якщо елемент не знайдено.

# Write your code here
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sort_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
found = binary_search(sort_arr, target)
print(f"Element {element} was found at index: {found}")
