# Union and Intersection

# Write a program that creates two sets with elements entered by the user.
# The program should combine these sets using the union() method and find their intersection using the intersection() method.
# The program should display both results.

### 🇺🇦 Ukrainian version:

# Об'єднання та перетин

# Напишіть програму, яка створює два множини з елементів, запитуваних у користувача.
# Програма повинна об'єднати ці множини з використанням методу union() і знайти їх перетин з використанням методу intersection().
# Програма повинна вивести обидва результати

# Write your code here
l1 = [input("Add elements to set 1: ") for _ in range(3)]
l2 = [input("Add elements to set 2: ") for _ in range(3)]
s1 = set(l1)
s2 = set(l2)

union_set = s1.union(s2)
intersection_set = s1.intersection(s2)

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
