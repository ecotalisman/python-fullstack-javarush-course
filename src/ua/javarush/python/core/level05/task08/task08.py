# Eraser

# Write a program that creates a list with 10 elements, then replaces the elements from the third to the fifth
# with a single value entered by the user.
# The program should display the updated list.

### 🇺🇦 Ukrainian version:

# Стирач

# Напишіть програму, яка створює список із 10 елементів, потім замінює елементи з третього по п'ятий на одне значення, запитуване у користувача.
# Програма повинна вивести оновлений список.

# Write your code here
l = list(n for n in range(10))
el = input("Add element: ")
l[2:5] = [el]
print(l)