# Using the reduce() Method

# Write a class that controls its own serialization via the __reduce__() method
# so that only certain fields are preserved during serialization and deserialization.


### 🇺🇦 Ukrainian version:

# Використання методу reduce()

# Напишіть клас, який керує своєю серіалізацією за допомогою методу __reduce__(),
# щоб під час серіалізації та десеріалізації зберігалися лише певні поля.

# Write your code here
import pickle

class CustomClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __reduce__(self):
        return self.__class__, (self.name, self.age)

    def __repr__(self):
        return f"CustomClass(name={self.name}, age={self.age})"

obj = CustomClass("John", 25)

data = pickle.dumps(obj)
new = pickle.loads(data)
print(new)
