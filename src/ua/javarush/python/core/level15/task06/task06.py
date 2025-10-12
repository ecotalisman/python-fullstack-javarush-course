# Stack — Not So Simple

# Write a program that implements a stack and demonstrates its core properties:
# LIFO (Last In, First Out), and the push, pop, and peek operations.

### 🇺🇦 Ukrainian version:

# Стек це не так вже й просто

# Напишіть програму, яка реалізує стек і демонструє його основні властивості:
# LIFO (Last In, First Out), операції push, pop, і peek.


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # Write your code here
    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]


# # Demonstration of work stack
stack = Stack()
print("Стек порожній:", stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)
print("Верхній елемент стека:", stack.peek())

print("Витягування елемента:", stack.pop())
print("Витягування елемента:", stack.pop())
print("Верхній елемент стека:", stack.peek())

print("Стек порожній:", stack.is_empty())
print("Витягування елемента:", stack.pop())
print("Стек порожній:", stack.is_empty())
