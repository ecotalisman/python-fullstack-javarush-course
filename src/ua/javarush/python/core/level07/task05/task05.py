# Looking for Keys

# Write a program that creates a dictionary with information about a book (e.g., title, author, year of publication). The program should:
# - Print all the keys of the dictionary using the keys() method.
# - Iterate over all keys and display them on the screen.

### 🇺🇦 Ukrainian version:

# Шукаємо ключі.

# Напишіть програму, яка створює словник з інформацією про книгу (наприклад, назва, автор, рік видання). Програма повинна:
# Вивести всі ключі словника з використанням методу keys().
# Ітерувати по всіх ключах і вивести їх на екран.

# Write your code here
book_dict = {"title" : "Sherlock Holmes", "author" : "Arthur K.Doyle", "year" : 1982}

print(book_dict.keys())

for key in book_dict.keys():
    print(key)