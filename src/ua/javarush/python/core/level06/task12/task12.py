# Replacement

# Write a program that creates a set containing the names of several fruits.
# The program should display the fruits on the screen.
# Then, the program should ask the user for an index (based on the display order) and a new fruit name for replacement.
# After that, find the fruit by index, replace it with the new name, and display the updated set.

### 🇺🇦 Ukrainian version:

# Заміна

# Напишіть програму, яка створює множину, що містить назви кількох фруктів.
# Програма повинна вивести фрукти на екран.
# Потім програма повинна запросити у користувача індекс (з урахуванням порядку виводу на екран) і нову назву фрукта для заміни.
# Після цього знайти фрукт за індексом, замінити його новою назвою і вивести оновлену множину.

# Write your code here
fruits = {"Apple", "Banana", "Orange"}
fruits_list = list(fruits)

for i, fruit in enumerate(fruits_list):
    print(f"{i}: {fruit}")

try:
    index = int(input(f"Enter the index of the fruit to replace (0-{len(fruits_list) - 1}): "))
    if  0 <= index < len(fruits_list):
        new_fruit = input("Enter the new fruit name: ").strip()

        old_fruit = fruits_list[index]
        fruits_list[index] = new_fruit

        fruits.remove(old_fruit)
        fruits.add(new_fruit)

        print("Updated set:", fruits)

    else:
        print("Incorrect index!")

except ValueError:
    print("Please enter a valid integer!")


