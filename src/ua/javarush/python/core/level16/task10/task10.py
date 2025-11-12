# Real Hash Table

# Write a class that implements a hash table.
# Your class should include methods for inserting, retrieving, searching, and deleting elements.
# You may ignore the possibility of hash function collisions.

### 🇺🇦 Ukrainian version:

# Реальна хеш-таблиця

# Напишіть клас для реалізації хеш-таблиці.
# Ваш клас повинен включати методи для вставки, отримання, пошуку та видалення елементів.
# Можливість колізії хеш-функції можна не враховувати.

# Write your code here


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
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
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
    # Write your code here
        index = self._hash(key)
        if self.table[index] is None:
            return
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return


    def search(self, key):
    # Write your code here
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for k, v in self.table[index]:
            if k == key:
                return True
        return False



# Example usage:
hash_table = HashTable()
hash_table.insert("key1", "value1")
print(hash_table.get("key1"))  # Output: value1
print(hash_table.search("key1"))  # Output: True
hash_table.delete("key1")
print(hash_table.get("key1"))  # Output: None
