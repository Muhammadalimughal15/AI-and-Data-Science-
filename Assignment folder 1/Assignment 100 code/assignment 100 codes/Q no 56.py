# Get an ASCII string from the user
ascii_string = input("Enter an ASCII string: ")

# Convert the ASCII string to a unicode string encoded by utf-8
unicode_string = ascii_string.encode("utf-8")

# Print the unicode string
print(unicode_string)