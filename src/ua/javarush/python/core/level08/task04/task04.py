# Sorting

# Write a program that uses a lambda function to sort a list of strings by their length
# using the sorted() function. The program should:
# Create a list of strings.
# Use sorted() and a lambda function to sort the strings by length.
# Print the result.

### 🇺🇦 Ukrainian version:

# Сортування.

# Напишіть програму, яка використовує лямбда-функцію для сортування списку рядків за їхньою довжиною
# з використанням функції sorted(). Програма повинна:
# Створити список рядків.
# Використати sorted() і лямбда-функцію для сортування рядків за довжиною.
# Вивести результат.

# Write your code here
sort = sorted(["Hello", "Chao", "Bonjour"], key=lambda x: len(x))
print(sort)