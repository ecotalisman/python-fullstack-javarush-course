# Stack is Simple

# Write a program that implements a stack and demonstrates its core properties:
# LIFO (Last In, First Out), and the push, pop, and peek operations.
# You may use the built-in list class.

### 🇺🇦 Ukrainian version:

# Стек це просто

# Напишіть програму, яка реалізує стек і демонструє його основні властивості:
# LIFO (Last In, First Out), операції push, pop, і peek.
# Клас list використовувати можна.


class Stack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    # Write your code here
    def push(self, num):
        return self.container.append(num)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.container:
            return self.container[-1]
        else:
            return None


# Demonstration of work
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 2
print(stack.size())  # Output: 1
print(stack.is_empty()) # Output: False
stack.pop()
print(stack.is_empty()) # Output: True
