# Collecting

# Write a program that uses the functions zip(), min(), max(), and sum() to work with data collections:
# Combine two lists into a list of tuples using zip().
# Find the smallest and largest element in a list of numbers using min() and max().
# Calculate the sum of all elements in a list of numbers using sum().

### 🇺🇦 Ukrainian version:

# Колекціонування

# Напишіть програму, яка використовує функції zip(), min(), max(), і sum() для роботи з колекціями даних:
# Об'єднати два списки в список кортежів за допомогою zip().
# Знайти найменший і найбільший елемент у списку чисел за допомогою min() та max().
# Підрахувати суму всіх елементів у списку чисел за допомогою sum().

# Write your code here
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))

print(c)
print(min(a))
print(max(b))
print(sum(a) + sum(b))
