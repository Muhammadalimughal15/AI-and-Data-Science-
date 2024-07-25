input_string = input("Enter a string: ")
char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

for char, count in sorted_chars:
    print(f"{char} {count}")