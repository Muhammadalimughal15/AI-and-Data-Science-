input_string = input("Enter a string: ")

digit_count = sum(char.isdigit() for char in input_string)
letter_count = sum(char.isalpha() for char in input_string)

print(f"Digit - {digit_count}")
print(f"Letter - {letter_count}")
