# Boundary Values Search

# Write a function that performs the fastest search to find the minimum
# and maximum values in a sorted array of numbers.
# The function should return a tuple with the indices of the minimum
# and maximum elements.

### 🇺🇦 Ukrainian version:

# Пошук граничних значень

# Напишіть функцію, яка виконує найшвидший пошук для знаходження мінімального
# і максимального значення в відсортованому масиві чисел.
# Функція повинна повертати кортеж з індексів мінімального і максимального елемента.

# Write your code here
def find_boundaries(arr):
    n = len(arr)
    if n == 0:
        return (None, None)
    elif arr[0] <= arr[-1]:
        return (0, n - 1)
    return (n - 1, 0)


# Example usage:
arr = [1, 2, 3, 4, 5]
print(find_boundaries(arr))  # Вивід: (0, 4)
