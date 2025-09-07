# Dynamic Module Import

# Write a program that asks the user for the name of a module to import
# and the name of a function to call from that module.
# The program should dynamically import the module and call the specified function with any argument.
# To access a child element from the module, use the getattr function.

### 🇺🇦 Ukrainian version:

# Динамічний імпорт модуля

# Напишіть програму, яка запитує у користувача назву модуля для імпорту
# та ім'я функції для виклику з цього модуля.
# Програма повинна динамічно імпортувати модуль та викликати вказану функцію з будь-яким аргументом.
# Для отримання дочірнього елемента у модуля використовуйте функцію getattr

# Write your code here
module_name = input("Enter module name: ")
function_name = input("Enter function name: ")
argument = float(input("Enter a number: "))

module = __import__(module_name)
func = getattr(module, function_name)

print(func(argument))
