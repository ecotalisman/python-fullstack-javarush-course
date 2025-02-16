# Tuple Grouping

# Write a program that creates a tuple with 6 elements entered by the user.
# Then, the program should group them into 3 tuples with 2 elements each.
# Finally, merge the 1st and 3rd tuples and print the updated tuple.

### 🇺🇦 Ukrainian version:

# Групування кортежів

# Напишіть програму, яка створює кортеж із 6 елементів, запитуваних у користувача.
# Потім програма повинна згрупувати їх у 3 кортежі по 2 елементи.
# Потім об'єднати 1 і 3 кортежі та вивести оновлений кортеж на екран.

# Write your code here
t = tuple([input("Enter elements: ") for _ in range(6)])
l = list(t)
l = [(l[i], l[i + 1]) for i in range(0, len(l) - 1, 2)]
a, _, b = l
n = [a, b]
n = tuple(n)
print(n)
