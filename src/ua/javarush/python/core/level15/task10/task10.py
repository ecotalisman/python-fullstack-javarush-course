# Converting a Number to Decimal

# Write a program that takes a binary integer from the user,
# converts it to its decimal representation, and shows how it would be stored in memory.
# The program should also display the number of bytes occupied by the number.

### 🇺🇦 Ukrainian version:

# Перетворюємо число в десяткове

# Напишіть програму, яка приймає двійкове ціле число від користувача,
# перетворює його в десяткове представлення і показує, як воно буде зберігатися в пам'яті.
# У програмі також має бути відображено кількість байтів, яке займає число.

# Write your code here
bits = input("Enter a binary number: ").strip()
if bits.startswith(('-', '+')):
    num = int(bits, 2)
    num_bytes = max(1, (num.bit_length() + 7) // 8)
else:
    w = len(bits)
    if set(bits) - {'0', '1'}:
        raise ValueError("Binary string must contain only 0 and 1")
    num = int(bits, 2)
    if w > 0 and bits[0] == '1':
        num -= 1 << w
    num_bytes = (w +7) // 8

print(num)
print(num_bytes)
