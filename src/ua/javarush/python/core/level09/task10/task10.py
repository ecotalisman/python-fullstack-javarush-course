# Roar

# Create a base class Animal with a method speak that returns the string "Rrrrr!".
# Then create a child class Dog that inherits from Animal and overrides the speak method,
# adding its own behavior to the parent class behavior using the super() method.

### 🇺🇦 Ukrainian version:

# Ричання.

# Створіть базовий клас Animal з методом speak, який повертає рядок "Ррррр!".
# Потім створіть дочірній клас Dog, який буде успадковувати від Animal та перевизначати метод speak,
# додаючи до поведінки батьківського класу власну поведінку з використанням методу super().

# Write your code here
class Animal:
    def speak(self):
        return "Ррррр!"

class Dog(Animal):
    def speak(self):
        animal = super().speak()
        return f"{animal} Гав!"

dog = Dog()
print(dog.speak())