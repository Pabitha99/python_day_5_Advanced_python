# using regualar expression validating usa mobile number
import re
input="123-456-9802"
pattern="^([0-9]{3}?[- ])+([0-9]{3}?[- ])+([0-9]{4})$"
if re.search(pattern,input):
    print(f"{input} is valid USA mobile number")
else:
    print(f"{input} is not valid USA mobile number")