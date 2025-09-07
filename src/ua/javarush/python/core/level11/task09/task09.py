# Creating a Simple Iterator

# Write a class SimpleIterator that will iterate over a sequence of numbers from start to end.
# Implement the __iter__ and __next__ methods.

### 🇺🇦 Ukrainian version:

# Створення простого ітератора

# Напишіть клас SimpleIterator, який буде ітеруватися по послідовності чисел від start до end.
# Реалізуйте методи __iter__ і __next__.

# Write your code here
class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current
