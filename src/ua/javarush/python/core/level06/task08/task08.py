# Multiplicity

# Create an empty set.
# Ask the user for 5 numbers sequentially.
# For each number, create a separate set and add it to the initial set.
# Print the final result.

### 🇺🇦 Ukrainian version:

# Множинність

# Створіть порожню множину.
# Запитайте у користувача послідовно 5 чисел.
# Для кожного з них створюйте окрему множину та додавайте її до початкової.
# Виведіть отриманий результат на екран.

# Write your code here
s = set()
for el in range(5):
    num = (int(input("Enter a number: ")) )
    temp = {num}
    s.update(temp)

print(s)
