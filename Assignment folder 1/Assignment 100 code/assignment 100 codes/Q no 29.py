def print_longest_string(str1, str2):
    """
    Accept two strings as input, determine the string with the maximum length,
    and print it to the console. If the two strings have the same length,
    print both strings line by line.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    """
    len1 = len(str1)  # Get the length of the first string
    len2 = len(str2)  # Get the length of the second string

    if len1 > len2:
        print("The longest string is:", str1)
    elif len2 > len1:
        print("The longest string is:", str2)
    else:
        print("Both strings have the same length:")
        print(str1)
        print(str2)

# Test the function
str1 = "Hello, World!"
str2 = "Python is awesome!"
print_longest_string(str1, str2)