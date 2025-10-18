# Queue is Simple

# Write a program that implements a queue and demonstrates its core properties:
# FIFO (First In, First Out), and the enqueue, dequeue, and peek operations.
# You may use the built-in list class.

### 🇺🇦 Ukrainian version:

# Черга це просто
# Напишіть програму, яка реалізує чергу і демонструє її основні властивості:
# FIFO (First In, First Out), операції enqueue, dequeue, і peek.
# Клас list використовувати можна.


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
    # Write your code here
        return self.queue.append(item)

    def dequeue(self):
    # Write your code here
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
    # Write your code here
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]


# Demonstration of work
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()         # Front item: 1
q.dequeue()      # Dequeued: 1
q.dequeue()      # Dequeued: 2
q.peek()         # Front item: 3
q.dequeue()      # Dequeued: 3
q.dequeue()      # Queue is empty
