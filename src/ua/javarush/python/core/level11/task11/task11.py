# Operator Overloading for Comparison

# Write a class Person that represents a person with attributes name and age.
# Implement operator overloading for == and < to compare people by age.

### 🇺🇦 Ukrainian version:

# Перевантаження операторів порівняння

# Напишіть клас Person, який буде представляти людину з атрибутами name і age.
# Реалізуйте перевантаження операторів порівняння == і < для порівняння людей за віком.

# Write your code here
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

p1 = Person("A", 20)
p2 = Person("B", 20)
p3 = Person("C", 5)
print(p1 == p2)
print(p1 == p3)
print(p3 < p1)
print(p1 < p3)
