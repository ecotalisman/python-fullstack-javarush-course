# Editor

# Write a program that creates a dictionary with information about a book (title, author, year of publication).
# The program should:
# - Modify the value of the "year of publication" key.
# - Use the setdefault() method to add a new key "publisher" if it is missing.
# - Update the values of several elements using the update() method.
# - Print the updated dictionary after each change.

### 🇺🇦 Ukrainian version:

# Редактор.

# Напишіть програму, яка створює словник з інформацією про книгу (назва, автор, рік видання).
# Програма повинна:
# Змінити значення ключа "рік видання".
# Використати метод setdefault() для додавання нового ключа "видавництво", якщо він відсутній.
# Оновити значення декількох елементів з використанням методу update().
# Вивести оновлений словник після кожної зміни.

# Write your code here
book_dict = {"title" : "Sherlock Holmes", "author" : "Arthur K.Doyle", "year" : 1982}

book_dict["year"] = 1985
print(book_dict)

book_dict.setdefault("publisher", "Vivat")
print(book_dict)

updates = {"author": "Arthur Konan Doyle", "year": 1982}
book_dict.update(updates)
print(book_dict)
