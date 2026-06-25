from library.models import Book

# Create a Book object with the specified parameters
new_book = Book(title="Learning Django", author="John Doe", published_date="2023-10-15")

# Save the created object to the database
new_book.save()

# Display the object on the screen (the __str__ method will be used)
print(new_book)