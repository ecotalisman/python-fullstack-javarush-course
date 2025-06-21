# Three Checks

# Write a program that creates a dictionary with information about a book (e.g., title, author, year of publication).
# The program should:
# - Check for the presence of the "author" key using the in operator.
# - Check for the presence of the "publisher" key using the get() method.
# - Check for the presence of the "title" key using the keys() method.

### 🇺🇦 Ukrainian version:

# Три перевірки.

# Напишіть програму, яка створює словник з інформацією про книгу (наприклад, назва, автор, рік видання).
# Програма повинна:
# Перевірити наявність ключа "author" з використанням оператора in.
# Перевірити наявність ключа "publisher" з використанням методу get().
# Перевірити наявність ключа "title" з використанням методу keys().

# Write your code here
book_dict = {"title" : "Sherlock Holmes", "author" : "Arthur K.Doyle", "publisher" : 1982}

if "author" in book_dict:
    print("Key 'author' is have in Dictionary")
else:
    print("Key isn't found")

if book_dict.get("publisher") is not None:
    print("Key 'publisher' is have in Dictionary")
else:
    print("Key isn't found")

if "title" in book_dict.keys():
    print("Key 'title' is have in Dictionary")
else:
    print("Key isn't found")
