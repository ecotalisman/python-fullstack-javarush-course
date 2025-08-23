# Creating Classes

# Create a class Library with an attribute books, which is a list of books.
# Add methods add_book(book) to add a book to the library
# and display_books() to print the list of all books.
# Create an object of the Library class, add several books, and display the list of books using the object methods.

### 🇺🇦 Ukrainian version:

# Створюємо класи.

# Створіть клас Library з атрибутом books, який є списком книг.
# Додайте методи add_book(book) для додавання книги до бібліотеки
# та display_books() для виводу списку всіх книг.
# Створіть об'єкт класу Library, додайте кілька книг і виведіть список книг, використовуючи методи об'єкта.

# Write your code here
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)

    def display_books(self):
        print(self.books)

book = Library()
book.add_book("Harry Potter")
book.add_book("Sherlock Holmes")
book.display_books()
