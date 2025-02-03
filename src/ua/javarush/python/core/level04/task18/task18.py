# Found a Cat

# Write a function create_cat_profile(name, age, breed="Unknown") that takes a name, age, and an optional "breed" parameter (default is "Unknown").
# The function should print the cat's profile in the format "Name: [name], Age: [age], Breed: [breed]".
# Then write a program that calls this function with different parameters.

### 🇺🇦 Ukrainian version:

# Знайшли кота

# Напишіть функцію create_cat_profile(name, age, breed="Невідомо"), яка приймає ім'я, вік і необов'язковий параметр "порода" (за замовчуванням "Невідомо").
# Функція повинна виводити профіль кота у форматі "Ім'я: [name], Вік: [age], Порода: [breed]".
# Потім напишіть програму, яка викликає цю функцію з різними параметрами.

# Write your code here
def create_cat_profile(name, age, breed='Невідомо'):
    print(f"Ім'я: {name}, Вік: {age}, Порода: {breed}")

create_cat_profile("Ruf", 5)
create_cat_profile("Pups", 3, "Німецька вівчарка")