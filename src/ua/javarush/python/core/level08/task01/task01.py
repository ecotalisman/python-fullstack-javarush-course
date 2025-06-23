# System Functions

# Write a program that creates several objects of different types and
# uses the functions id(), hash(), and dir() to perform the following operations:
# Determine and display the unique identifiers of the objects using id().
# Display the hash values of hashable objects using hash().
# Display the list of attributes and methods of an object using dir().

### 🇺🇦 Ukrainian version:

# Системні функції.

# Напишіть програму, яка створює декілька об'єктів різних типів і
# використовує функції id(), hash(), і dir() для виконання наступних операцій:
# Визначити та вивести унікальні ідентифікатори об'єктів за допомогою id().
# Вивести хеш-значення хешованих об'єктів за допомогою hash().
# Вивести список атрибутів та методів об'єкта за допомогою dir().

# Write your code here
a = ["a", "b", "c"]
b = (1, 2, 3)
c = {"a": 1, "b": 2}
print(id(a))
print(id(b))
print(id(c))

print(hash(b))

print(dir(a))
print(dir(b))
print(dir(c))
