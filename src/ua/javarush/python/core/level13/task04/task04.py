# Using a Decoder

# Write a program that deserializes a JSON string into a Python object
# using a custom decoder to convert ISO strings into datetime objects.

# Write your code here

### 🇺🇦 Ukrainian version:

# Використання декодера

# Напишіть програму, яка десеріалізує JSON-рядок в об'єкт Python з використанням
# користувацького декодера для перетворення рядків ISO в об'єкти datetime.

# Напишіть тут ваш код
import json
from datetime import datetime


def custom_decoder(dct):
    if 'timestamp' in dct:
        dct['timestamp'] = datetime.fromisoformat(dct['timestamp'])
    return dct


json_str = '''
{
    "event": "Start",
    "timestamp": "2020-01-01T12:00:00+00:00"
}
'''

data = json.loads(json_str, object_hook=custom_decoder)
print(data)
