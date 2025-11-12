# Hash Table

# Write a class that implements a hash table.
# Your class should include methods for inserting and retrieving elements.
# You may ignore the possibility of hash function collisions.

### 🇺🇦 Ukrainian version:

# Хеш-таблиця

# Напишіть клас для реалізації хеш-таблиці.
# Ваш клас повинен включати методи для вставки та отримання елементів.
# Можливість колізії хеш-функції можна не враховувати.

# Write your code here

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
    # Write your code here
        return hash(key) % self.size

    def insert(self, key, value):
    # Write your code here
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
    # Write your code here
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

# Example usage:
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
print(ht.get("apple"))  # Output: 1
print(ht.get("banana"))  # Output: 2
print(ht.get("cherry"))  # Output: None
