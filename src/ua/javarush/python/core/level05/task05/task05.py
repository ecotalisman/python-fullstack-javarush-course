# Slices

# Write a program that creates a list with 10 elements,
# prints the elements from the third to the seventh (inclusive) using slices,
# and prints the last three elements of the list using negative indices.

### 🇺🇦 Ukrainian version:

# Зрізи

# Напишіть програму, яка створює список з 10 елементів,
# виводить елементи з третього по сьомий включно з використанням зрізів
# та виводить останні три елементи списку з використанням від'ємних індексів.

# Write your code here
l = list(n for n in range(10))
print(l[2:7])
print(l[-3:])