# Competition: Linear vs Binary Search

# Write a program that measures the time taken by linear search and binary search.
# Provide input arrays of lengths 1, 2, 4, 8, ... 2^n elements.
# Determine from which array size the binary search becomes more efficient.
# Do not include the time to sort the array for the binary search.

### 🇺🇦 Ukrainian version:

# Змагання

# Напишіть програму, яка вимірює час, який витрачають на пошук лінійний та бінарний пошуки.
# Передайте їй на вхід масиви довжиною 1, 2, 4, 8, ... 2^n елементів.
# Визначте кількість елементів, починаючи з якої бінарний пошук ефективніший.
# Час на сортування масиву для бінарного пошуку не враховувати.
import random
from time import perf_counter

from numpy.ma.extras import median


# Write your code here
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

n = 10
length = [2**k for k in range(n + 1)]
square_arrays = [[x*x for x in range(L)] for L in length]
reps = 50

def time_call(fn, arr, target, reps):
    times = []
    for _ in range(reps):
        t0 = perf_counter()
        fn(arr, target)
        t1 = perf_counter()
        times.append(t1 - t0)
    return median(times)

results = []
for L, arr in zip(length, square_arrays):
    if not arr:
        continue

    target = random.choice(arr)

    tl = time_call(linear_search, arr, target, reps)
    tb = time_call(bin_search, arr, target, reps)

    results.append((L, tl, tb))

for L, tl, tb in results:
    print(f"L={L:6d} | linear={tl:.6e} sec | binary={tb:.6e} sec | faster={'bin' if tb < tl else 'lin'}")

threshold = next((L for L, tl, tb in results if tb < tl), None)
print("\nApproximate threshold length from which binary becomes faster:", threshold)

