# Serialization with yaml

# Write a program that serializes and deserializes a Python object using the yaml module.
# The object to be serialized will be a dictionary containing information about a movie:
# title, director, and release year.


### 🇺🇦 Ukrainian version:

# Серіалізація за допомогою yaml

# Напишіть програму, яка серіалізує та десеріалізує об'єкт Python з використанням модуля yaml.
# Об'єктом для серіалізації буде словник, що містить інформацію про фільм: назва, режисер і рік випуску.
# Напишіть тут ваш код

# Example dictionary with movie information
import yaml

film_info = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010
}

# Write your code here
yaml_string = yaml.dump(film_info)
loaded_data = yaml.load(yaml_string, Loader=yaml.FullLoader)
print(loaded_data)