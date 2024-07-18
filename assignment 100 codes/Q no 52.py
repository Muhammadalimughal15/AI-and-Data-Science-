import re

# Get the email address from the user
email = input("Enter an email address: ")

# Use a regular expression to extract the username
pattern = r"(\w+)@\w+\.com"
match = re.match(pattern, email)

# If a match is found, print the username
if match:
    username = match.group(1)
    print("Username:", username)
else:
    print("Invalid email address")
