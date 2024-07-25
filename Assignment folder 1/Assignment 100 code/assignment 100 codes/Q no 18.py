import re

def password_check(passwords):
    valid_passwords = []
    for password in passwords.split(','):
        if len(password) < 6 or len(password) > 12:
            continue
        if (re.search("[a-z]", password) and 
            re.search("[0-9]", password) and 
            re.search("[A-Z]", password) and 
            re.search("[$#@]", password)):
            valid_passwords.append(password)
    return ','.join(valid_passwords)

passwords = input("Enter passwords separated by comma: ")
print(password_check(passwords))