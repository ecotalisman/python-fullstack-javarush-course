# Element Removal

# Write a program that creates a list with 5 elements, asks the user for an index to remove,
# and deletes the element at that index using the pop() method.
# The program should display the updated list and the removed element.
# If the index does not exist, the program should display a message about it.

### 🇺🇦 Ukrainian version:

# Видалення елемента

# Напишіть програму, яка створює список з 5 елементів, запитує у користувача індекс елемента для видалення
# і видаляє елемент за цим індексом з використанням методу pop().
# Програма повинна вивести оновлений список і видалений елемент.
# Якщо індекс не існує, програма повинна вивести повідомлення про це.

# Write your code here
l = list(n for n in range(5))
try:
    d = int(input("Enter a number to delete elements from the list: "))
    el = l.pop(d)
    print("Element has been deleted: ", el)
except IndexError:
    print("Error: index out of range")
print(l)