# Common Subarray Elements

# Given two arrays of numbers, find the elements from the first array
# that also exist in the second array.

### 🇺🇦 Ukrainian version:

# Загальний підмасив

# Дано два масиви чисел. Необхідно знайти елементи першого масиву,
# які існують у другому масиві.

def common_subarray(arr1, arr2):
# Write your code here
    hash_tab = set(arr2)
    common_el = []
    for el in arr1:
        if el in hash_tab:
            common_el.append(el)
    return common_el

# Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

result = common_subarray(arr1, arr2)
print(result)
