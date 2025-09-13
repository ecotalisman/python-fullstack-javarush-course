# Using an Encoder

# Write a program that serializes a Python object containing date and time into a JSON string
# using a custom encoder to convert datetime objects into ISO string format.

# Write your code here

### 🇺🇦 Ukrainian version:

# Використання енкодера

# Напишіть програму, яка серіалізує об'єкт Python, що містить дату і час, у JSON-рядок
# з використанням користувацького кодера для перетворення об'єктів datetime у рядковий формат ISO.

# Напишіть тут ваш код
import json
from datetime import datetime, timezone


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


data = {
    "event": "Start",
    "timestamp": datetime(2020, 1, 1, 12, 0, tzinfo=timezone.utc)
}

json_str = json.dumps(data, cls=CustomEncoder, ensure_ascii=False, indent=4)
print(json_str)
