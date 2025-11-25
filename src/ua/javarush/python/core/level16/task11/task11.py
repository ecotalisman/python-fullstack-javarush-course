# Hash Table with Chaining

# Write a class that implements a hash table using separate chaining.
# Your class should include methods for inserting and retrieving elements.
# Also write a function to demonstrate the hash table in action.
# Resolve possible hash collisions using the chaining method.

### 🇺🇦 Ukrainian version:

# Хеш-таблиця без колізій

# Напишіть клас для реалізації хеш-таблиці з використанням ланцюжків (chaining).
# Ваш клас має включати методи для вставки та отримання елементів.
# Також напишіть функцію для демонстрації роботи хеш-таблиці.
# Можливу колізію хеш-функції потрібно вирішити методом ланцюжків.

# Write your code here

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
    # Write your code here
        index = self._hash_function(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def get(self, key):
    # Write your code here
        index = self._hash_function(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

def demonstrate_hash_table():
    ht = HashTable(10)
    ht.insert('apple', 1)
    ht.insert('banana', 2)
    ht.insert('grape', 3)
    ht.insert('apple', 4)

    print(ht.get('apple'))   # Output: 4
    print(ht.get('banana'))  # Output: 2
    print(ht.get('grape'))   # Output: 3
    print(ht.get('pear'))    # Output: None

demonstrate_hash_table()
