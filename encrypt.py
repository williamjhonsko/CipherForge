
#### **encrypt.py**
```python
from Crypto.Cipher import AES
import base64
import os

def pad(text):
    return text + (16 - len(text) % 16) * ' '

key = os.urandom(16)
cipher = AES.new(key, AES.MODE_ECB)
message = "Secret data"
encrypted = base64.b64encode(cipher.encrypt(pad(message)))

print(f"Encrypted message: {encrypted.decode()}")
print(f"Key: {base64.b64encode(key).decode()}")
