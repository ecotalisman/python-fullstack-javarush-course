# Hash Function

# Write your own hash function that returns an integer from 0 to 10,000
# for a string of any length.

### 🇺🇦 Ukrainian version:

# Хеш-функція

# Напиши свою хеш-функцію, яка повертає ціле число від 0 до 10к для рядка довільної довжини.

# Write your code here
import hashlib


def custom_hash(key: str) -> int:
    h = hashlib.sha256(key.encode('UTF-8')).digest()
    return int.from_bytes(h, 'big') % 10_000

print(custom_hash("France"))
print(custom_hash("aplle"))
print(custom_hash(""))
