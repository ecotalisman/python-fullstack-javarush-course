# Using super() and MRO

# Create classes A, B, C, and D, where B and C inherit from A, and D inherits from B and C.
# In each class, define a method method that prints the class name and calls super().method().
# Create an instance of class D and call the method method to understand the method resolution order (MRO).

### 🇺🇦 Ukrainian version:

# Використання super() і MRO

# Створіть класи A, B, C, і D, де B і C успадковують від A, а D успадковує від B і C.
# У кожному класі визначте метод method, який виводить ім'я класу і викликає метод super().method().
# Створіть екземпляр класу D і викличте метод method, щоб зрозуміти порядок виклику методів за MRO.

# Write your code here
class A:
    def method(self):
        print("A")
        
class B (A):
    def method(self):
        print("B")
        super().method()


class C(A):
    def method(self):
        print("C")
        super().method()
        
class D(B, C):
    def method(self):
        print("D")
        super().method()

obj = D()
obj.method()


