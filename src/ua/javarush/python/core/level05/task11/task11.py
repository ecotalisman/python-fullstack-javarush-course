# Forest

# Write a program that creates a list of tree names, then uses a loop and the enumerate() function
# to display each element of the list along with its index.

### 🇺🇦 Ukrainian version:

# Ліс

# Напишіть програму, яка створює список з назв дерев, потім з використанням циклу та функції enumerate()
# виводить кожен елемент списку та його індекс.

# Write your code here
l = ["Maple", "Oak", "Spruce", "Willow", "Cherry tree", "Linden", "Poplar", "Ash", "Pine", "Birch"]
for index, element in enumerate(l):
    print(f"Index: {index}, Element: {element}")