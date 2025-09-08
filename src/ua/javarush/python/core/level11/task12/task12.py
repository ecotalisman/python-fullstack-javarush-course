# Operator Overloading for Indexing

# Write a class Matrix that represents a two-dimensional matrix
# and supports operator overloading for indexing ([]).
# Implement the __getitem__ and __setitem__ methods.

### 🇺🇦 Ukrainian version:

# Перевантаження операторів індексації

# Напишіть клас Matrix, який буде представляти двовимірну матрицю та підтримувати перевантаження операторів індексації ([]).
# Реалізуйте методи __getitem__ та __setitem__.


class Matrix:

# Write your code here
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, key):
        row, col = key
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of range")
        return self.data[row][col]

    def __setitem__(self, key, value):
        row, col = key
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Index out of range")
        self.data[row][col] = value

# Example usage:
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вивід: 1
