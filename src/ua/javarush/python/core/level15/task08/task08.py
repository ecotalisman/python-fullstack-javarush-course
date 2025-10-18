# Queue is Hard

# Write a program that implements a queue and demonstrates its core properties:
# FIFO (First In, First Out), and the enqueue, dequeue, and peek operations.

# Do not use the built-in list class.

### 🇺🇦 Ukrainian version:

# Черга це складно

# Напишіть програму, яка реалізує чергу та демонструє її основні властивості:
# FIFO (First In, First Out), операції enqueue, dequeue, і peek.

# Клас list використовувати не можна.

# Write your code here

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        # queue initialization
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # add an element
        new_node = Node(value)
        if not self.rear:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # remove and return an element
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        current = self.front
        self.front = current.next
        if self.front is None:
            self.rear = None

        current.next = None

        return current.value

    def peek(self):
        # return the first element without removing it
        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self.front.value

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        if current is None:
            print("None")
            return

        first = True
        while current is not None:
            if first:
                print(current.value, end="")
                first = False
            else:
                print(" <- ", current.value, sep="", end="")
            current = current.next
        print(" <- None")

        # Alternative: list-based display:

        # current = self.front
        # values = []
        # while current is not None:
        #     values.append(current.value)
        #     current = current.next
        # return values


# demonstration of functionality
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
