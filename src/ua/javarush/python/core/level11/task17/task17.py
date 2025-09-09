# Name Collision
import importlib

# Call the sqrt function from your custom math module.
# Call the sqrt function from the built-in math module.

### 🇺🇦 Ukrainian version:

# Перетин імен.

# Викличте функцію sqrt вашого модуля math.
# Викличте функцію sqrt вбудованого модуля math.

# Write your code here
import importlib.util
import math

spec = importlib.util.spec_from_file_location("my_math", "math.py")
my_math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(my_math)

print(math.sqrt(9))
my_math.sqrt(9)
