# Sum of Numbers (Pairs)

# Given an array of numbers and a target sum,
# find all pairs of numbers whose sum equals the target value.

### 🇺🇦 Ukrainian version:

# Сума чисел

# Дано масив чисел і цільове значення суми. Необхідно знайти всі пари чисел,
# які у сумі дають цільове значення.

def find_pairs(nums, target):
# Write your code here
    seen = set()
    result_set = set()
    for x in nums:
        y = target - x
        if y in seen:
            pair = (min(x, y), max(x, y),)
            result_set.add(pair)
        seen.add(x)
    return list(result_set)

# Example usage:
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
print(find_pairs(nums, target))
