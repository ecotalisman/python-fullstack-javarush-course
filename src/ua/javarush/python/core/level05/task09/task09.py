# First Out

# Write a program that creates a list with 5 elements, asks the user for an element to remove,
# and removes the first occurrence of that element from the list using the remove() method.
# The program should display the updated list.

### 🇺🇦 Ukrainian version:

# Перший на вихід

# Напишіть програму, яка створює список з 5 елементів, запитує у користувача елемент для видалення
# і видаляє перший знайдений елемент зі списку з використанням методу remove().
# Програма повинна вивести оновлений список.

# Write your code here
l = list(n for n in range(5))
d = int(input("Enter a number to delete elements from the list: "))
if d in l:
    l.remove(d)
else:
    print("Number not found in the list")
print(l)