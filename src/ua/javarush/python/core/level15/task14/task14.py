# I Love Lists Even More

# Write a program that creates a dynamic array (list-like structure)
# and demonstrates its core operations: append, remove, index access, and element update.
# Do not use the built-in list class.

### 🇺🇦 Ukrainian version:

# Люблю список ще більше

# Напишіть програму, яка створює динамічний масив (структуру на кшталт списку)
# і демонструє його основні операції: додавання, видалення, доступ за індексом та зміну елемента.
# Клас list використовувати не можна.


class DynamicArray:
    def __init__(self):
        self.array = []

    def add(self, element):
        # Write your code here
        self.array.append(element)

    def remove(self, index):
        # Write your code here
        if len(self.array) == 0:
            raise IndexError("List is empty")
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        self.array.pop(index)

    def get(self, index):
        # Write your code here
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, element):
        # Write your code here
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        self.array[index] = element

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)


# Приклади використання:
arr = DynamicArray()
arr.add(1)
arr.add(2)
arr.add(3)
print(arr)  # [1, 2, 3]

arr.remove(2)
print(arr)  # [1, 2]

print(arr.get(1))  # 2

arr.set(1, 5)
print(arr)  # [1, 5]

print(len(arr))  # 2