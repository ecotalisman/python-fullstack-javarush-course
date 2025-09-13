# Serialization with pickle

# Write a program that serializes and deserializes a Python object using the pickle module.
# The object to be serialized will be a dictionary containing information about a student:
# name, age, and student status.
# Write your code here


### 🇺🇦 Ukrainian version:

# Серіалізація за допомогою pickle

# Напишіть програму, яка серіалізує та десеріалізує об'єкт Python з використанням модуля pickle.
# Об'єктом для серіалізації буде словник, що містить інформацію про студента: ім'я, вік та статус студента.

# Object to serialize
import pickle

student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Write your code here
with open('data.pkl', 'wb') as file:
    pickle.dump(student_info, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
