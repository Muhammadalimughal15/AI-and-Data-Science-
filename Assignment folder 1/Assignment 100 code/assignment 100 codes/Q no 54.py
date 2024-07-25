import re

# Get the input from the user
input_string = input("Enter a sequence of words: ")

# Use a regular expression to extract the words composed of digits only
pattern = r"\b\d+\b"
words = re.findall(pattern, input_string)

# Print the words composed of digits only
print(words)
