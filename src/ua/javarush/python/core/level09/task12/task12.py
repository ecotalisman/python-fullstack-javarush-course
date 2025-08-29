# Animal World

# Create a base class Animal with a method make_sound that returns the string "Uuuuuu!".
# Then create child classes Dog and Cat that override the make_sound method
# and use super() to call the parent class method.

### 🇺🇦 Ukrainian version:

# Тваринний світ.

# Створіть базовий клас Animal з методом make_sound, який буде повертати рядок "Ууууууу!".
# Потім створіть дочірні класи Dog та Cat, які будуть перевизначати метод make_sound
# і використовувати super() для виклику методу батьківського класу.

# Write your code here
class Animal:
    def make_sound(self):
        return "Ууууууу!"

class Dog(Animal):
    def make_sound(self):
        sound_dog = super().make_sound() + " Гав-гав!"
        return sound_dog

class Cat(Animal):
    def make_sound(self):
        sound_cat = super().make_sound() + " Мяу-мяу!"
        return sound_cat


# Examples of usage:

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Ууууууу! Гав-гав!
print(cat.make_sound())  # Ууууууу! Мяу-мяу!