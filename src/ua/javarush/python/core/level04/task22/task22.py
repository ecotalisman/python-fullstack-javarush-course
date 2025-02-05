# Cat Profile

# Write a function create_cat_profile(name: str, age: int, **kwargs: str) -> None that takes the cat's name and age as required parameters,
# as well as any number of named parameters (such as breed, color, etc.).
# The function should print the cat's profile, including all provided parameters.

### 🇺🇦 Ukrainian version:

# Профіль кота

# Напишіть функцію create_cat_profile(name: str, age: int, **kwargs: str) -> None, яка приймає ім'я та вік кота як обов'язкові параметри,
# а також довільну кількість іменованих параметрів (наприклад, порода, колір тощо).
# Функція повинна виводити профіль кота, включаючи всі передані параметри.

# Write your code here
def create_cat_profile(name: str, age: int, **kwargs: str) -> None:
    print(name, age, kwargs)

create_cat_profile("Мурзик", 3, порода="Сіамський", колір="Чорний")
create_cat_profile("Барсик", 5, країна="Китай", хобі="Ловити мишей")