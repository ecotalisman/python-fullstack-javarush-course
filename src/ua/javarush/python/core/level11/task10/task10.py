# Iterator for a Collection

# Write a class CollectionIterator that will iterate over any collection (list, string, etc.).
# Implement the __iter__ and __next__ methods.

### 🇺🇦 Ukrainian version:

# Ітератор для колекції

# Напишіть клас CollectionIterator, який буде ітеруватися по довільній колекції (список, рядок і т.д.).
# Реалізуйте методи __iter__ та __next__.

# Write your code here
class CollectionIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        item = self.collection[self.index]
        self.index += 1
        return item