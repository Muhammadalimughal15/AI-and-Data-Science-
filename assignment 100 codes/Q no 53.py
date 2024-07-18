import re

# Get the email address from the user
email = input("Enter an email address: ")

# Use a regular expression to extract the company name
pattern = r"\w+@(\w+)\.com"
match = re.match(pattern, email)

# If a match is found, print the company name
if match:
    company_name = match.group(1)
    print("Company Name:", company_name)
else:
    print("Invalid email address")