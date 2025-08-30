# Base Classes

# Create two base classes Base1 and Base2, each with a describe() method.
# Create a derived class Combined that inherits from both base classes.
# Implement the describe() method in each base class.
# Call the describe() method on an object of the Combined class.

### 🇺🇦 Ukrainian version:

# Базові класи.

# Створіть два базові класи Base1 і Base2, кожен з яких має метод describe().
# Створіть похідний клас Combined, який наслідує від обох базових класів.
# Реалізуйте метод describe() в кожному базовому класі. Викличте метод describe() у об'єкта класу Combined.

# Write your code here
class Base1:
    def describe(self):
        print("Class Base1")

class Base2:
    def describe(self):
        print("Class Base2")

class Combined(Base1, Base2):
    pass

obj = Combined()
obj.describe()
