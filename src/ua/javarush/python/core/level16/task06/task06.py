# The Best Search

# Write a program to determine which method is faster on an array of 1000 elements:
# Method 1: perform linear search 10 times.
# Method 2: sort the array + perform binary search 10 times.

### 🇺🇦 Ukrainian version:

# Найкращий пошук

# Напиши програму, яка з'ясує, який спосіб пошуку в масиві з 1000 елементів швидший:
# Спосіб 1: 10 разів скористатися лінійним пошуком.
# Спосіб 2: відсортувати масив + 10 разів скористатися бінарним пошуком.

# Write your code here

import random
from time import perf_counter
from numpy.ma.extras import median


def linear_search(arr, target):
    for i, el in enumerate(arr):
        if el == target:
            return i
    return -1

def bin_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = random.sample(range(1, 1001), k=1000)
print(len(arr) == len(set(arr)))

targets = random.sample(arr, k=10)
print("Targets: ", targets)

tl = perf_counter()
for t in targets:
    linear_search(arr, t)
time_linear_total = perf_counter() - tl

tb = perf_counter()
arr_sorted = sorted(arr)
for t in targets:
    bin_search(arr_sorted, t)
time_binary_total = perf_counter() - tb

print(f"\nMethod Linear (10x linear):           {time_linear_total:.6f} sec")
print(f"\nMethod Binary (sort + 10x binary):    {time_binary_total:.6f} sec")

if time_binary_total < time_linear_total:
    speedup = time_linear_total / time_binary_total
    print(f"Conclusion: Binary is faster (including sort). ~{speedup:.2f}x faster")
elif time_binary_total > time_linear_total:
    slowdown = time_binary_total / time_linear_total
    print(f"Conclusion: Linear is faster (or roughly same). Binary is ~{slowdown:.2f}x slower")
else:
    print("Conclusion: Tie — both took the same time")
