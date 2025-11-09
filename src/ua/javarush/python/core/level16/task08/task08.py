# Hash Function for a Dictionary



# Write your own hash function that returns an integer from 0 to 10,000
# for a dictionary with arbitrary elements.

### 🇺🇦 Ukrainian version:

# Хеш-функція для словника

# Напиши свою хеш-функцію, яка повертає ціле число від 0 до 10к
# для словника з довільними елементами.

# Write your code here
import hashlib
import json
from typing import Any


def _canonical(obj: Any):
    if obj is None: return ["none"]
    if isinstance(obj, bool): return ["bool", obj]
    if isinstance(obj, (int, float, str)): return ["scalar", repr(obj)]
    if isinstance(obj, bytes): return ["bytes", obj.hex()]
    if isinstance(obj, (list, tuple)): return ["list", [_canonical(x) for x in obj]]
    if isinstance(obj, (set, frozenset)):
        items = [_canonical(x) for x in obj]
        return ["set", sorted(items, key=repr)]
    if isinstance(obj, dict):
        items = [(_canonical(k), _canonical(v)) for k, v in obj.items()]
        items.sort(key=lambda kv: repr(kv[0]))
        return ["dict", items]
    return ["repr", repr(obj)]

def custom_hash(dct: dict) -> int:
    canon = _canonical(dct)
    payload = json.dumps(canon, sort_keys=True, separators=(',', ':')).encode('utf-8')
    digest = hashlib.sha256(payload).digest()
    return int.from_bytes(digest, 'big') % 10_001

d = {1 : "France", 2 : "Italy", 3 : "Ukraine"}
print(custom_hash(d))

