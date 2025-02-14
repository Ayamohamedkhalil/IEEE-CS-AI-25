import random
import string
# Using "_" is refer to  name of variable isn't important 
password = ""
for _ in range(8):
    password += random.choice(string.ascii_letters + string.digits)  
print(password)
