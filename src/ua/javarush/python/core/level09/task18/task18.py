# Method Overriding

# Create classes M, N, and O, where N and O inherit from M.
# In each class, define a method action that prints the class name
# and calls the parent class method using super().
# Check the order of method calls by creating an instance of class N and calling the action method.

### 🇺🇦 Ukrainian version:

# Перевизначення методу

# Створіть класи M, N та O, де N і O успадковують від M.
# У кожному класі визначте метод action, який виводить ім'я класу
# та викликає метод батьківського класу за допомогою super().
# Перевірте порядок виклику методів, створивши екземпляр класу N і викликавши метод action.

# Write your code here
class M:
    def action(self):
        print("M")

class N(M):
    def action(self):
        super().action()
        print("N")

class O(M):
    def action(self):
        super().action()
        print("O")

obj = N()
obj.action()