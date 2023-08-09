import re
import sys

email = input("Email: ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z_]+\.(com|fr|dz|edu|net)$",email, re.IGNORECASE):
    print(f"{email} VALID")
else:
    print(f"{email} INVALID")
    sys.exit()

username, domain = email.split("@")
matches = re.search(r"^([a-zA-Z])_?([a-zA-Z])$",username)
if matches:
    username = matches.group(1) + " " + matches.group(2)

print(f"your name is : {username}")