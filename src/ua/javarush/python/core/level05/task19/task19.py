# Simple Yet Complex

# Create 5 tuples of different lengths:
# - 0 elements
# - 1 element
# - 5 elements
# - 100 elements
# - 1000 elements
# Display them on the screen.

### 🇺🇦 Ukrainian version:

# Просто і складно водночас

# Створи 5 кортежів з різною довжиною: 0 елементів, 1 елемент, 5 елементів, 100 елементів, 1000 елементів.
# Виведи їх на екран.

# Write your code here
k = ()
l = ("a",)
m = tuple([x for x in range(5)])
n = tuple([x for x in range(100)])
o = tuple([x for x in range(1000)])
print(k, l, m, n, o, sep="\n")
