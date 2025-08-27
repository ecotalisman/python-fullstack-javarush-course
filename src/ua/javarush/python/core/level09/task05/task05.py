# Protect Yourself

# Create a class Car that has a public attribute brand and a protected attribute _model.
# Add methods to get and set the value of the protected attribute _model.
# Create an object of the Car class, set the attribute values, and print them.

### 🇺🇦 Ukrainian version:

# Захищайтеcь.

# Створіть клас Car, який буде мати публічний атрибут brand і захищений атрибут _model_.
# Додайте методи для отримання та встановлення значення захищеного атрибута _model.
# Створіть об'єкт класу Car, встановіть значення атрибутів та виведіть їх на екран.

# Write your code here
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model

auto = Car("BMW", "X5")
print(auto.get_model())

auto.set_model("X6")
print(auto.get_model())
