# Finding Duplicates

# Given an array of numbers, you must find and return all duplicates in the array.

### 🇺🇦 Ukrainian version:

# Пошук дублікатів

# Дано масив чисел. Необхідно знайти та повернути всі дублікати в масиві.


def find_duplicates(nums):
    # Write your code here
    s = set()
    duplicates = []
    for n in nums:
        if n in s:
            duplicates.append(n)
        s.add(n)
    return duplicates

# Example usage:
nums = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 1]
print(find_duplicates(nums))  # Output: [2, 3, 1]
