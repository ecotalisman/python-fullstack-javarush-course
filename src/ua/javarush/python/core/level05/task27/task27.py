# Sum of Tuples

# Write a program that creates a tuple containing several nested tuples with integers.
# The program should use a for loop to calculate the sum of all elements in the nested tuples and display the result.

### 🇺🇦 Ukrainian version:

# Сума кортежів

# Напишіть програму, яка створює кортеж, що містить декілька вкладених кортежів із цілих чисел.
# Програма повинна використовувати цикл for для обчислення суми всіх елементів у вкладених кортежах і вивести результат.

# Write your code here
t = list(range(10))
t = tuple([(t[i], t[i + 1], t[i + 2]) for i in range(1, 10, 3)])

total = 0
for sub_t in t:
    for num in sub_t:
        total += num

print(f"Sum of tuple:  {total}")
