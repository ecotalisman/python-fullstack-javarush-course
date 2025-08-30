# Super Action

# Create two base classes BaseA and BaseB, each with an action() method.
# Create a derived class Derived with an overridden action() method that calls super().action().
# Call the action() method on an object of the Derived class and analyze the order of method calls.

### 🇺🇦 Ukrainian version:

# Супер-екшен.

# Створіть два базові класи BaseA і BaseB, кожен з яких має метод action().
# Створіть похідний клас Derived з перевизначеним методом action(), який викликає метод super().action().
# Викличте метод action() у об'єкта класу Derived і проаналізуйте порядок виклику методів.

# Write your code here
class BaseA:
    def action(self):
        print("class BaseA")

class BaseB:
    def action(self):
        print("class BaseB")

class Derived(BaseA, BaseB):
    def action(self):
        print("class Derived")
        super().action()

obj = Derived()
obj.action()
