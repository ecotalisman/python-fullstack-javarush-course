# Pets

# Write a function check_type to check whether the passed object is an instance of the Animal class or its subclasses.
# Use the isinstance() function to perform the check.
# Then create classes Animal, Dog, and Cat, and test several objects.

### 🇺🇦 Ukrainian version:

# Домашні тварини.

# Напишіть функцію check_type для перевірки, чи є переданий об'єкт екземпляром класу Animal або його підкласів.
# Використайте функцію isinstance() для виконання перевірки.
# Потім створіть класи Animal, Dog, Cat і перевірте декілька об'єктів.

# Write your code here
class Animal():
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_type(obj):
    return print(isinstance(obj, Animal))

animal = Animal()
dog = Dog()
cat = Cat()

check_type(animal)
check_type(dog)
check_type(cat)
check_type(10)