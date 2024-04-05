import re
input="Password1234@?qb"
pattern="^[A-Z a-z 0-9 /d?@#$!.]{16}$"
if re.search(pattern,input):
    print(f"{input} is valid password")
else:
    print(f"{input} is not valid password")
