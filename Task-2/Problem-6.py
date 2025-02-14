import random
import string

password = ""
for _ in range(8):
    password += random.choice(string.ascii_letters + string.digits)  
print(password)
