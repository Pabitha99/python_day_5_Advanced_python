# using regular expression validating bangladesh mobile number
import re
input="+8801234567890"
pattern="^[+]+[88]?[0-9]+[0]$"
if re.search(pattern,input):
    print(f"{input} is valid Bangladesh mobile number")
else:
    print(f"{input} is not valid Bangladesh mobile number")