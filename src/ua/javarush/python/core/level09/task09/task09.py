# Supercars

# Create a base class Vehicle that has attributes brand and model.
# Then create a child class Car that inherits from Vehicle and adds the attribute fuel_type.
# Use the super() method to call the constructor of the base class.

### 🇺🇦 Ukrainian version:

# Супермашини.

# Створіть базовий клас Vehicle, який буде мати атрибути brand і model.
# Потім створіть дочірній клас Car, який буде наслідувати від Vehicle і додавати атрибут fuel_type.
# Використовуйте метод super() для виклику конструктора базового класу.

# Write your code here
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

car = Car("BMW", "X5", "Diesel")
print(car.brand)
print(car.model)
print(car.fuel_type)