# using regular expression validating e-mail address
import re
input="carla.abc@gmail.com"
pattern="^[a-z 0-9]?[a-z,0-9]+[@]\w+[.]+\w{2,3}$"
if re.search(pattern,input):
    print(f"{input} is valid")
else:
    print(f"{input} is not valid")


