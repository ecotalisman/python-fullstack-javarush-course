# Serialization of a dictionary into a string

# Write a program that serializes a dictionary into a string using the pickle module,
# and then deserializes this dictionary from the string.


### 🇺🇦 Ukrainian version:

# Серіалізація словника у рядок

# Напишіть програму, яка серіалізує словник у рядок з використанням модуля pickle,
# а потім десеріалізує цей словник із рядка.

# Example dictionary for serialization
import pickle

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}

# Write your code here
ser_data = pickle.dumps(data)
loaded_data = pickle.loads(ser_data)
print(loaded_data)
