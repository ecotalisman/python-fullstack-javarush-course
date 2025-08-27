# Library

# Create a class Library that represents a library of books.
# Add a __str__ method that returns a string with information about the library and the list of books,
# and a __len__ method that returns the number of books in the library.
# Create an object of the Library class, add several books to it,
# and print the library information and the number of books.

### 🇺🇦 Ukrainian version:

# Бібліотека.

# Створіть клас Library, який буде представляти бібліотеку книг.
# Додайте метод __str__, який буде повертати рядок з інформацією про бібліотеку з переліком книг, та метод __len__,
# який буде повертати кількість книг у бібліотеці.
# Створіть об'єкт класу Library, додайте в нього декілька книг і
# виведіть інформацію про бібліотеку та кількість книг.

# Write your code here


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
# Write your code here
        self.books.append(book)

    def __str__(self):
# Write your code here
        return f"{self.books}"

    def __len__(self):
# Write your code here
        return len(self.books)

# Creating a Library Object
library = Library()

# Add books to the library
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Display information about the library with a list of books and the total number of books
print(library)
print(f"Number of books in library: {len(library)}")