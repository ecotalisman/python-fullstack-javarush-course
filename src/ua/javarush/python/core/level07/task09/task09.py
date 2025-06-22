# Student – A Proud Title

# Write a program that creates a dictionary with information about a student (name and age).
# The program should:
# - Add a new element "university" to the dictionary.
# - Add the element "city" only if it doesn't already exist in the dictionary.
# - Add multiple new elements using the update() method.
# - Print the updated dictionary after each addition.

### 🇺🇦 Ukrainian version:

# Студент - це звучить гордо.

# Напишіть програму, яка створює словник з інформацією про студента (ім'я та вік).
# Програма повинна:
# Додати новий елемент "університет" у словник.
# Додати елемент "місто" тільки в тому випадку, якщо його ще немає у словнику.
# Додати кілька нових елементів за допомогою методу update().
# Вивести оновлений словник після кожного додавання.

# Write your code here
student_dict = {"name": "John", "age": 25}

student_dict["University"] = "Harvard"
print(student_dict)

if "city" not in student_dict:
    student_dict["city"] = "London"
print(student_dict)

student_dict.update(phone = "Samsung", merried = "Not")
print(student_dict)

