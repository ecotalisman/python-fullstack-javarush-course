# Fruity Mix

# Write a program that creates a set containing the names of several fruits.
# Then, the program should ask the user for the name of a fruit to remove and delete it from the set using the discard() method.
# The program should display the updated set.
# If the element is not found, the program should continue executing without an error.

### 🇺🇦 Ukrainian version:

# Фруктовиця

# Напишіть програму, яка створює множину, що містить назви декількох фруктів.
# Потім програма повинна запросити у користувача назву фрукта для видалення і видалити його з множини з використанням методу discard().
# Програма повинна вивести оновлену множину.
# Якщо елемент не знайдений, програма повинна продовжити виконання без помилки.

# Write your code here
fruits = {"Apple", "Banana", "Orange", "Grape", "Pineapple"}
while fruits:
    guess = input("Enter the name of a fruit to remove: ").strip()
    if guess in fruits:
        fruits.discard(guess)
        print(fruits)
    else:
        print(f"Try again! {fruits}")
