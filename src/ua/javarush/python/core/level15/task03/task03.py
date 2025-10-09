# Singly Linked List

# Write a program that implements a singly linked list with methods for adding, deleting, and searching elements.
# Add several elements to the list, delete one of them, and search for an element by its value.

### 🇺🇦 Ukrainian version:

# Однозв'язний список

# Напишіть програму, яка реалізує однозв'язний список з методами додавання, видалення і пошуку елементів.
# Додайте декілька елементів у список, видаліть один з них і знайдіть елемент за значенням.

# Write your code here

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
    # Write your code here
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def remove(self, key):
    # Write your code here
        if not self.head:
            return False

        if self.head.value == key:
            self.head = self.head.next
            return True

        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == key:
                prev.next = curr.next
                return True
            prev, curr = curr, curr.next

        return False

    def find(self, key):
    # Write your code here
        current = self.head

        while current is not None:
            if current.value == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

# Test the LinkedList
sll = LinkedList()
sll.add(1)
sll.add(2)
sll.add(3)
sll.print_list()

sll.remove(2)
sll.print_list()

print(sll.find(3))  # Outputs: True
print(sll.find(2))  # Outputs: False
