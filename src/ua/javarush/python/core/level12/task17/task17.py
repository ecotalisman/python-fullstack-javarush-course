# Serialization of a list to a file

# Write a program that serializes a list to a file using the pickle module,
# and then deserializes this list from the file.


### 🇺🇦 Ukrainian version:

# Серіалізація списку у файл

# Напишіть програму, яка серіалізує список у файл з використанням модуля pickle,
# а потім десеріалізує цей список з файлу.

# Example list for serialization
import pickle

data = [1, 2, 3, 'a', 'b', 'c']

# Write your code here
with open('list.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('list.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
