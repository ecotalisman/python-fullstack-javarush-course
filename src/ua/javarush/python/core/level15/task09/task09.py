# Binary Representation

# Write a program that takes an integer from the user,
# converts it to its binary representation, and shows how it would be stored in memory.
# The program should also display the number of bytes occupied by the number.

### 🇺🇦 Ukrainian version:

# Двійкове представлення

# Напишіть програму, яка приймає ціле число від користувача,
# перетворює його в двійкове представлення та показує, як воно буде зберігатися в пам’яті.
# У програмі також має бути відображено кількість байтів, займане числом.

# Write your code here
num = int(input("Enter the number: "))
num_form = format(num, 'b')
num_bytes = max(1, (num.bit_length() + 7) // 8)
print(num_form)
print(num_bytes)
