# Substring Search

# Write a program that takes a string and a substring from the user.
# The program should:
# - Check if the substring is in the string using the 'in' operator,
# - Find the first occurrence of the substring using the find() method,
# - Count the number of occurrences using the count() method.
# The program should display all the results.

### 🇺🇦 Ukrainian version:

# Пошук підрядка.

# Напишіть програму, яка приймає рядок і підрядок від користувача.
# Програма повинна перевірити, чи входить підрядок до рядка з використанням оператора in,
# знайти перше входження підрядка з використанням методу find() і
# підрахувати кількість входжень підрядка з використанням методу count().
# Програма повинна вивести всі результати.

# Write your code here
text = input("Enter the main string: ")
subString = input("Enter the substring: ")

contains = subString in text
first_index = text.find(subString)
count = text.count(subString)

print(f"Is the substring present? {contains}")
if  first_index != -1:
    print(f"First occurrence at position: {first_index}")
else: print("Substring not found")
print(f"Number of occurrence: {count}")