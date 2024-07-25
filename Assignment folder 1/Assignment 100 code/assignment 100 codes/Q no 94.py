import textwrap
input_string = input("Enter a string: ")
width = int(input("Enter the width: "))
print(textwrap.fill(input_string, width))