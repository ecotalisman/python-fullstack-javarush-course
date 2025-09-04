# Custom Exception

# Create a custom exception InvalidAgeError that will be raised in the check_age function
# if the age is less than 0 or greater than 150. Handle this exception in a try-except block.

### 🇺🇦 Ukrainian version:

# Користувацьке виключення

# Створіть користувацьке виключення InvalidAgeError, яке буде викликатися у функції check_age,
# якщо вік менше 0 або більше 150. Обробіть це виключення в блоці try-except.

# Write your code here
class InvalidAgeError(ValueError):
    pass

def check_age(num):
    if not (0 <= num <= 150):
        raise InvalidAgeError(f"Invalid age: {num}. Allowed range is 0 to 150")

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
